from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'account/welcome.html'