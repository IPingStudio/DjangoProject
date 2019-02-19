from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is HttpResponse!")

def detail(request, question_id):
    return HttpResponse("You`re looking at qustion %s." % question_id)

def results(request, question_id):
    response = "You`er looking at the results of question %s."
    return HttpResponse(response % question_id)
