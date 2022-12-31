from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def say_hello(request):
    content = "<h1>Hello</h1> This is hello page"
    return HttpResponse(content)
# Create your views here.

def home(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        return HttpResponse("POST method: Welcome to the HOME page")

def method(request):
    path = request.path
    method = request.method
    content='''
<center><h2>Testing Django Request Response Objects</h2>
<p>Request path : " {}</p>
<p>Request Method :{}</p></center>
'''.format(path, method)
    return HttpResponse(content)

def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def query(request):
    name = request.GET['name']
    age = request.GET['age']
    return HttpResponse("Name:{} Age:{}".format(name, age))

def showform(request):
    return render(request, 'form.html')

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse('Name:{} UserID:{}'.format(name, id))

def getdrink(request, name):
    return HttpResponse('Name of drink: {}'.format(name))