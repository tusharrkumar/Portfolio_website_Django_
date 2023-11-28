from django.shortcuts import render

# Create your views here.

def skill(request):
    context = {'skill': 'active'}
    return render(request, 'edu/skill.html',context)

def project(request):
    context = {'project': 'active'}
    return render(request, 'edu/project.html',context)