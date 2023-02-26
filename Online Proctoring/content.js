var Name=''
var Email=''
var Code=''

//Creating form to be filled user giving test
const form = document.createElement("form");
form.style.position = "fixed";
form.style.top = "0";
form.style.left = "0";
form.style.right = "0";
form.style.bottom = "0";
form.style.backgroundColor = "#f9f9f9";
form.style.padding = "20px";
form.style.zIndex = "9999";
form.style.display = "flex";
form.style.flexDirection = "column";
form.style.alignItems = "center";

//Creating heading element of form
const heading = document.createElement("h1");
heading.textContent = "Fill the Details";
heading.style.fontSize = "32px";
heading.style.marginBottom = "20px";
form.appendChild(heading);

//Creating name-input element of form
const nameLabel = document.createElement("label");
nameLabel.textContent = "Name:";
nameLabel.style.marginBottom = "10px";
const nameInput = document.createElement("input");
nameInput.setAttribute("type", "text");
nameInput.setAttribute("name", "name");
nameInput.style.padding = "10px";
nameInput.style.borderRadius = "4px";
nameInput.style.border = "1px solid #ccc";
nameInput.style.marginBottom = "20px";
nameInput.style.width = "200px";
form.appendChild(nameLabel);
form.appendChild(nameInput);

//Creating email-input element of form
const emailLabel = document.createElement("label");
emailLabel.textContent = "Email:";
emailLabel.style.marginBottom = "10px";
const emailInput = document.createElement("input");
emailInput.setAttribute("type", "email");
emailInput.setAttribute("name", "email");
emailInput.style.padding = "10px";
emailInput.style.borderRadius = "4px";
emailInput.style.border = "1px solid #ccc";
emailInput.style.marginBottom = "20px";
emailInput.style.width = "200px";
form.appendChild(emailLabel);
form.appendChild(emailInput);

//Creating activationCode-input element of form
const codeLabel = document.createElement("label");
codeLabel.textContent = "Invitation Code:";
codeLabel.style.marginBottom = "10px";
const codeInput = document.createElement("input");
codeInput.setAttribute("name", "code");
codeInput.style.padding = "10px";
codeInput.style.borderRadius = "4px";
codeInput.style.border = "1px solid #ccc";
codeInput.style.marginBottom = "20px";
codeInput.style.width = "200px";
form.appendChild(codeLabel);
form.appendChild(codeInput);

//Creating submit button of form
const submitButton = document.createElement("button");
submitButton.textContent = "Submit";
submitButton.style.backgroundColor = "#4CAF50";
submitButton.style.color = "white";
submitButton.style.padding = "14px 20px";
submitButton.style.marginTop = "20px";
submitButton.style.border = "none";
submitButton.style.borderRadius = "4px";
submitButton.style.cursor = "pointer";
form.appendChild(submitButton);
document.body.appendChild(form);


// Event triggered on clicking submit button of form and make API call to the server save detail of user giving test.
submitButton.addEventListener("click", function(event) {
event.preventDefault();
const name = nameInput.value;
const email = emailInput.value;
const code = codeInput.value;
Name=name;
Email=email;
Code=code;

const xhr = new XMLHttpRequest();
xhr.open('POST', 'http://127.0.0.1:8000/start-test', true);
xhr.setRequestHeader('Content-Type', 'application/json');

if (name.trim() !== '' && email.trim() !== '' && code.trim() !== '') {
xhr.send(JSON.stringify({name:name,email:email,code:code}));
window.alert("Test started! Good luck!");
form.remove();
} 
else {
window.alert("Fill all field values!"); 
}
});
      


// Creating video element and asking permission to allow
const video = document.createElement('video');
video.autoplay = true;
video.style.position = 'fixed';
video.style.bottom = '0';
video.style.right = '0';
video.style.width='200px';
video.style.height='200px';
if (navigator.mediaDevices.getUserMedia) {
navigator.mediaDevices.getUserMedia({ video: true })
.then(function (stream) {
video.srcObject = stream;
})
.catch(function (err0r) {
console.log("Error: " + err0r);
});
}
document.body.appendChild(video);


// This function make API call to the server to save image at every 3 minute of time interval
setInterval(function() {
const canvas = document.createElement('canvas');
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
const ctx = canvas.getContext('2d');
ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
const dataURL = canvas.toDataURL('image/png');
const xhr = new XMLHttpRequest();
xhr.open('POST', 'http://127.0.0.1:8000/save-img', true);
xhr.setRequestHeader('Content-Type', 'application/json');
try {
xhr.send(JSON.stringify({image:dataURL,email:Email,code:Code}));
console.log(Email,Code);
} 
catch (error) {
console.error(error.message);
}
}, 1 * 60 * 1000);


  