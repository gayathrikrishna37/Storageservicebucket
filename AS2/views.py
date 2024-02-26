from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import UserCredentials,UserData

import json





from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


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

    return render(request, 'crm/dashboard.html')
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
def post_user_data(request, userid, bucketid):
    print('hello')
    credentials = []
    user_credentials = UserCredentials.objects.all()
    for credential in user_credentials:
        credentials.append(credential.userid)
        credentials.append(credential.username)
        credentials.append(credential.email)
        
    print(credentials)
    # if request.method == 'POST':
    #     try:
    #         post_data = json.loads(request.body)
    #         userid = userid
    #         bucketid = bucketid
            
    #         if userid is None or bucketid is None or post_data is None:
    #             return JsonResponse({'error': 'userid, bucketid, and data fields are required'}, status=400)
    #         if userid == credentials[0]:
    #             print('done')
    #             UserData.objects.create(userid=userid, bucketid=bucketid, data=post_data)
    #             return JsonResponse({'success': 'Data posted successfully'})
    #     except json.JSONDecodeError:
    #         return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    # else:
    #     return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

# Return a default JsonResponse if none of the conditions were met
    return JsonResponse({'error': 'Something went wrong'}, status=400)


@csrf_exempt
def simple_post(request,userid,bucketid):
    if request.method == 'POST':
        # Extract JSON data from the request body
        try:
            userid = userid
            bucketid = bucketid
            data = json.loads(request.body)
            print(data,userid,bucketid)
            
            
            if userid is None or bucketid is None or data is None:
                return JsonResponse({'success': 'ok daaaa'}, status=200)
                
         
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
        # Check if the required data is present
        
    else:
        # If request method is not POST, return a JSON response indicating an error
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def process_data(data):
    # Here, you can perform any processing on the received data
    # For example, you might save it to the database, perform calculations, etc.
    return data