from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
class MyTemplateView(TemplateView):
    template_name = "my_template.html"