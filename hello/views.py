from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader

def hello(request):
    return HttpResponse("Hello world!")
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())