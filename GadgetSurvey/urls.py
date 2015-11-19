from django.conf.urls import url

urlpatterns =[
    url(r'^home/$','GadgetSurvey.views.home'),
    url(r'^afterSurvey','GadgetSurvey.views.afterSurvey'),
    url(r'^login/$','GadgetSurvey.views.login'),
    url(r'^submitSurvey/$','GadgetSurvey.views.submitSurvey'),
    url(r'','GadgetSurvey.views.start'),
]