from django.urls import path , include
from dashboard import views as dashboard_views
app_name = "dashboard"
urlpatterns = [
    path('admin-login',dashboard_views.admin_login , name='admin_login'), #admin-login
    path('candidate-list',dashboard_views.list , name='list'),            #show candidate how gave the test
    path('start-test',dashboard_views.starttest , name='start-test'),     #when user submit form
    path('save-img',dashboard_views.saveimg , name='save-img'),           #Image saved at every 3 minute
    path('logout',dashboard_views.logout_request , name='logout'),        #admin-logout
    path('<int:image_id>',dashboard_views.show_image , name='show_image'),#getting image from id
    path('<str:email>/<str:code>',dashboard_views.detail , name='detail'),#showing dashboard of particular user

]