from django.shortcuts import render, redirect
from GadgetSurvey.models import Gadget_Survey

from django.contrib.auth.decorators import login_required

# Create your views here.


def start(request):
    return redirect(to='/gadgetsurvey/login/')


def login(request):
    return render(request,'GadgetSurvey/loginPage.html')


@login_required(login_url='/gadgetsurvey/login/')
def home(request):
    if(request.POST):
        gadget_survey = Gadget_Survey()
        gadget_survey.currentMobile = request.POST.get('currentMobile')
        gadget_survey.current_Laptop_Pc= request.POST.get('currentLaptop')
        gadget_survey.future_device = request.POST.get('future_optradio')
        gadget_survey.future_device_description = request.POST.get('futureWhy')
        gadget_survey.likes_device = request.POST.get('optradio')
        gadget_survey.likes_device_description = request.POST.get('currentWhy')
        gadget_survey.user = request.user;
        gadget_survey.save()
        return render(request,'GadgetSurvey/afterSurvey.html',context={'survey':'1'})
    else:
        gadget_survey = Gadget_Survey.objects.get(user = request.user)
        if gadget_survey is None:
            return render(request,'GadgetSurvey/home.html')
        else:
            return render(request,'GadgetSurvey/afterSurvey.html',context={'survey':'2'})


def afterSurvey(request):
    return render(request,'GadgetSurvey/afterSurvey.html')

#
# def submitSurvey(request):
