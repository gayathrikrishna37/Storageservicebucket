from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, BucketForm

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import UserCredentials,UserData,Bucket

import json

import random

from datetime import datetime



from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout







def get_unique_code(length=6, digits=True):

    start_range = 10 ** (length - 1)
    end_range = 10 ** length - 1
    existing_codes = set()  # Use a set for faster lookup
    
    while True:
        unique_code = random.randint(start_range, end_range)
        if unique_code not in existing_codes:
            existing_codes.add(unique_code)
            return unique_code

# Example usage


















def homepage(request):

    return render(request, 'crm/index.html')




def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)
        print("hello")

        if form.is_valid():

            user = form.save()
            user_id = user.id

# Now you can use user_id as needed
            print("User ID:", user_id)

            return redirect("my-login")


    context = {'registerform':form}

    return render(request, 'crm/register.html', context=context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                user_Credentials(request)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'crm/my-login.html', context=context)


def user_logout(request):

    auth.logout(request)
    UserCredentials.objects.all().delete()
    return redirect("")



@login_required(login_url="my-login")
def dashboard(request):
    user_credentials = UserCredentials.objects.all()
    for credential in user_credentials:
        print(credential.username)

    return render(request, 'crm/dashboard.html',{'user_credentials': user_credentials})
def bucket_view(request):
    return render(request, 'crm/bucket.html')





def user_Credentials(request):
    try:
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        print(user_id)
        
        user_credentials = UserCredentials.objects.create(
            userid=user_id,
            username=username,
            email=email
        )
    except Exception as e:
        print(e)
        


@csrf_exempt
def simple_post(request,userid,bucketid):
    if request.method == 'POST':
        credentials = []
        user_credentials = UserCredentials.objects.all()
        for credential in user_credentials:
            credentials.append(credential.userid)
            credentials.append(credential.username)
            credentials.append(credential.email)
        # Extract JSON data from the request body
        try:
            userid = userid
            bucketid = bucketid
            data = json.loads(request.body)
            print(data,userid,bucketid)
            
            
            if userid != None or bucketid != None or data != None:
                
                print("hello")
            else:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
                
                
            print(userid)
            print(credentials[0])
            if userid == credentials[0]:
                UserData.objects.create(userid=userid, bucketid=bucketid, data=data)
                return JsonResponse({'success': 'Data posted successfully'})
            else:
                return JsonResponse({'error' : 'invalid userid'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
        # Check if the required data is present
        
    else:
        # If request method is not POST, return a JSON response indicating an error
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)






def get_user_data(request, userid, bucketid):
    try:
        # Retrieve the data based on user id and bucket id
        user_data = UserData.objects.filter(userid=userid, bucketid=bucketid).values()
        
        # Check if data exists
        if user_data.exists():
            # Return the data as JSON response
            return JsonResponse({'data': list(user_data)}, status=200)
        else:
            # If data doesn't exist, return a JSON response with an appropriate message
            return JsonResponse({'message': 'Data not found'}, status=404)
    except Exception as e:
        # Handle any exceptions and return an error response
        return JsonResponse({'error': str(e)}, status=500)


# Import necessary modules
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bucket

def create_bucket(request):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST':
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket_name = form.cleaned_data['bucketName']
            description = form.cleaned_data['description']
            bucket_type = form.cleaned_data['bucketType']

            # Save the data to the database
            new_bucket = Bucket.objects.create(
                bucket_name=bucket_name,
                description=description,
                bucket_type=bucket_type,
                creation_date = formatted_datetime,
                updation_date = formatted_datetime,
                bucket_id= get_unique_code()             # You can adjust this as needed
            )

            # Optionally, you can redirect to a success page or show a modal
            return redirect(dashboard)

    else:
        form = BucketForm()

    return render(request, 'create_bucket.html', {'form': form})