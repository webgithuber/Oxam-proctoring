from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Candidate , Image
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.base import ContentFile
import datetime
import base64
import json
from PIL import Image as pil
from io import BytesIO
import boto3
from exam import settings


#adds Cross-Origin Resource Sharing (CORS) headers to an HTTP response.
def allow_cors(view_func):
    def wrapped_view(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "https://www.hackerearth.com"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    return wrapped_view


#save user data to database
@allow_cors
@csrf_exempt
def starttest(request):
    print("start test")
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        code = data.get('code')
        if name and email and code:
            if Candidate.objects.filter(email=email,activation_code=code).count()==0:
                #save the user to data base
                Candidate(name=name,email=email,activation_code=code).save()
            return JsonResponse({'status': 'success'})
        else:
           return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})
    
#save image in data base in string form
@allow_cors
@csrf_exempt
def saveimg(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            image_data = data.get('image')
            email = data.get('email')
            code = data.get('code')
            today=datetime.datetime.now()
            
            
            if image_data:
                # Save image id to django-database data to the database
                image_model = Image(activation_code=code, email=email,created_at=today)
                image_model.save()
                id=Image.objects.get(activation_code=code, email=email,created_at=today).id
                
                #create an instance of the S3 client 
                s3 = boto3.client('s3',aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                #key value
                filename = 'img.'+str(id)+'.png'

                # Remove the data URL header from the base64-encoded string
                image_data = image_data[image_data.index(',')+1:]
                # Decode the base64-encoded string to obtain the binary image data
                binary_data = base64.b64decode(image_data)
                #store the image in S3 bucket
                s3.put_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=filename, Body=binary_data)
                
            return JsonResponse({'status': 'success'})
        else:
            raise Exception("Invalid request method.")
    except Exception as e:
        print("Error occurred: ", str(e))
        return JsonResponse({'status': 'error'})
    


#fetch image of particular id and decode it from string-encoded-image and return httpresponse
def show_image(request, image_id):
    if not request.user.is_authenticated:
        return redirect("dashboard:admin_login")
    #create an instance of the S3 client 
    s3 = boto3.client('s3',aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    filename = 'img.'+str(image_id)+'.png'
    #fetch image from S3 bucket
    response = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=filename)
    image_content = response['Body'].read()

    img=pil.open(BytesIO(image_content))
    image_buffer = BytesIO()
    img.save(image_buffer, format='PNG')
    #return an image in PNG format
    response = HttpResponse(image_buffer.getvalue(), content_type='image/png')
    return response
    
    

#fetch list of all user who attempted test
def list(request):
    if not request.user.is_authenticated:
        return redirect("dashboard:admin_login")
    candidates=Candidate.objects.all()
    return render(request,"dashboard/list.html",{"candidates":candidates,"home":1})



#fetch all images for single user for particular test/exam
def detail(request,email,code):
    if not request.user.is_authenticated:
        return redirect("dashboard:admin_login")
    images=Image.objects.filter(email=email,activation_code=code)
    return render(request,"dashboard/candidate.html",{"images":images})



def admin_login(request):
    error=''
    if request.user.is_authenticated:
        return redirect("dashboard:list")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("dashboard:list")
            else:
               error="Invalid username or password."
        else:
           error="Invalid username or password."
    return render(request,'dashboard/admin_login.html',{"error":error})




def logout_request(request):
    if not request.user.is_authenticated:
        return redirect("dashboard:admin_login")
    logout(request)
    return redirect('dashboard:admin_login')

    
