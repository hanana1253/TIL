from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
students_list = ['이한결']
def index(request):
    context = {
      'user_first_name': 'Hangyul',
      'user_last_name': 'Lee',
    }
    return render(request, 'index.html', context)

def login(request):
    return HttpResponse('login page')

def signout(request):
    return HttpResponse('Bye')

def verify(request):
    if request.method == 'POST':
        context = {'studentname': request.POST['studentname'], 'is_student': False }
        if context['studentname'] in students_list:
            context['is_student'] = True
    return render(request, 'verify.html', context)