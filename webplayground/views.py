
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name= "webplayground/home.html"
    
class SamplePageView(TemplateView):
    template_name = "webplayground/sample.html"