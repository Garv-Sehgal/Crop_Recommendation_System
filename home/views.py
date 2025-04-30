from django.shortcuts import render 
import joblib
import pandas as pd
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout


mp = joblib.load('./models/modelpickle')
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'index.html')
    # return HttpResponse(" This is Homepage")

def services(request):
    return render(request, 'services.html')
    
def form(request):
    return render(request, 'form.html')

def dataset(request):
    return render(request, 'dataset.html')

def model(request):
    return render(request, 'model.html')

def about(request):
    return render(request, 'about.html') 

# -------------> Sign UP
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def predict(request):
    print(request)  
    if request.method == "POST":
        print("Hello ----- world Hello world ")
        try:
            temp = {
                'N': int(request.POST.get('N', 0)),
                'P': int(request.POST.get('P', 0)),
                'K': int(request.POST.get('K', 0)),
                'temperature': float(request.POST.get('temperature', 0)),
                'humidity': float(request.POST.get('humidity', 0)),
                'ph': float(request.POST.get('ph', 0)),
                'rainfall': float(request.POST.get('rainfall', 0))
            }
            
            # Validation for range based on the provided ranges
            error_messages = []
            if not (0 <= temp['N'] <= 140):
                error_messages.append("Nitrogen value should be between 0 and 140.")
            if not (5 <= temp['P'] <= 145):
                error_messages.append("Phosphorus value should be between 5 and 145.")
            if not (5 <= temp['K'] <= 205):
                error_messages.append("Potassium value should be between 5 and 205.")
            if not (0 <= temp['temperature'] <= 45):
                error_messages.append("Temperature value should be between 0 and 45.")
            if not (14 <= temp['humidity'] <= 100):
                error_messages.append("Humidity value should be between 14 and 100.")
            if not (3.5 <= temp['ph'] <= 9.9):
                error_messages.append("pH value should be between 3.5 and 9.9.")
            if not (20 <= temp['rainfall'] <= 298):
                error_messages.append("Rainfall value should be between 20 and 298.")
            
            if error_messages:
                for msg in error_messages:
                    messages.error(request, msg)
                return render(request, 'form.html')
            
            testdf = pd.DataFrame({'X': temp}).transpose()
            predictedCrop = mp.predict(testdf.values)[0]
            context = {'PredictedCrop': predictedCrop}
            return render(request, 'form.html', context)
        
        except ValueError:
            messages.error(request, "Invalid input! Please enter numeric values only.")
            return render(request, 'form.html')
    
    return render(request, 'form.html')
