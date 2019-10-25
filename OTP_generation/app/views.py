from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from app.forms import otp_form
from app.models import otp
from django.contrib.auth.models import User
from twilio.rest import Client
import math, random
def home(request):
    count=User.objects.count()
    return render(request, 'registration/home.html', {'count':count})
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            # request.session.get_expiry_age(1500)
            form.save()
            return HttpResponse('succsessfull')
            # return render('/home')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
def logins(request):
    return render(request,'registration/loginresult.html')
def register(request):
    if request.method == "POST":
        form = otp_form(request.POST or None)
        if form.is_valid():
            account_sid = 'AC3a846e5983cc3d62b4c303813b605241'
            auth_token = 'd66ca53f3f3ada42adf222a420a70fda'
            client = Client(account_sid, auth_token)
            digits = "0123456789"
            OTP = ""
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]

            message = client.messages \
                .create(
                body='dont share with any one' + " " + OTP,
                from_='+12056276621',
                to='+91-9533558978'
            )
            context={
                'message':message,
                'otp':OTP
            }
            print(message.sid)
            print(OTP)
            return  render(request,'registration/otp.html',context)
            return  HttpResponse('succsessfully send the otp')
            # return render('otp')
    else:
        form=otp_form()
        return render(request,'registration/signup.html',{'form':form})
# def otp_view(request):
    # n = request.GET.get('n1')
    # print(n)
    # context = {'n': n}
    # return render(request,'registration/otp.html',context)
# def otp_view(request):
#     if request.method=='POST':
#         form =otp_form (request.POST)
#         if form.is_valid():
#             request.session['phone_number'] = form.cleaned_data['phone_number']
#             request.session['country_code'] = form.cleaned_data['country_code']
#             authy_api.phones.verification_start(
#             form.cleaned_data['phone_number'],
#             form.cleaned_data['country_code'],
#             via=form.cleaned_data['via']
#             )
#             return redirect('token_validation')
#     else:
#     form=VerificationForm()
#     return render(request,'registration/otp.html',{'form':form})
# def dbl(request):
#     list = otp.objects.values_list('id', flat=True)
#     for row in list:
#         query = otp.objects.filter(id=row).values('otp')
#         a = query[0]['otp']
#         otp.objects.filter(id=row).update(otp=a)
#     message = {"message": 'data updated successfully'}
#     return HttpResponse(message)