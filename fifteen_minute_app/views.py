from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from models import Volunteer

from send_emails import send_welcome_email

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['fullName', 'emailAddr', "phoneNumber",
        "addr1", "addr2", "city", "state", "zipcode",
        ]

    # fullname = forms.CharField(label='Your name', max_length=100)


def index(request):
    return HttpResponse("Let's get it going")


def signupform(request):
    if request.method == "GET":
        form = VolunteerForm()
        return render(request, 'signup.html', {"form": form})
    else:
        # Read form values  
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            send_welcome_email(volunteer.emailAddr) 
            return HttpResponse("Thank you {0}!".format(volunteer.fullName))
        else:
            return render(request, 'signup.html', {"form": form})
        

def signupcomplete(request):
    return HttpResponse("Let's get it going. I'm all signed up.")
