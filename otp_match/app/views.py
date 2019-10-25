from django.shortcuts import render

# Create your views here.
from twilio.rest import Client

from .forms import otp_form
from .models import otpmodel
import random,math
def home(request):
    return  render(request,'registration/home.html')
def signup(request):
    if request.method == "POST":
        form = otp_form(request.POST or None)
        if form.is_valid():
            form.save()
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
            return  render(request,'registration/otp.html',context)
            return  HttpResponse('succsessfully send the otp')
            # return render('otp')
    else:
        form=otp_form()
        return render(request,'registration/registor.html',{'form':form})