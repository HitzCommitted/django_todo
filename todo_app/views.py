from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def addTask(request):
    # return render(request, "addTask.html")
    return HttpResponse("The form is submitted successfully.")
