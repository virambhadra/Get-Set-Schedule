from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from .forms import *
import pandas as pd
import json
from django.http import HttpResponse, HttpResponseRedirect
'''from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest
'''

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


def makett(request):
    # connection.introspection.table_names()
    form = Bar(['Name','Profession','Stream','Hobbies'])
    
    #print(connection.introspection.table_names())
    # form = [str(Foo(prefix=i)) for i in range(4)]
    # form = '\n'.join(form)
    #print(form)
    return render(request,'makett.html',{'form':form})



def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


def ttdivision(request):
    form = base_form()
    if request.method == 'POST': # If the form has been submitted...
        form = base_form(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print(form.cleaned_data['my_form_field_name'])

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form =base_form() # An unbound form
        return render(request,'ttdivision.html',{'form':form})


def tt(request):
    data = pd.read_csv(r'mysite/static/Book1.csv')
    DataFrame = pd.DataFrame(data, columns= ['time','event'])
   # DataFrame = DataFrame.to_html()
    print(DataFrame)
    return render(request,'tt.html',{'DataFrame': DataFrame })


def Table(request):
    df = pd.read_csv('mysite/static/Final year project (Responses) - Form Responses 1.csv')
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'table.html', context)

'''def friend(request):
    return render(request,'friend.html')
'''
def yourtt(request):
    return render(request,'yourtt.html')

def edittt(request):
    form = Bar(['6am','7am','8am','9am','10am','11am','12am','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm'])
    return render(request,'edittt.html',{'form':form})

def myconnect(request):
    return render(request,'myconnect.html')

def addconn(request):
    form = Bar(['Username'])
    return render(request,'addconn.html', {'form':form})

def deleteconn(request):
    form = Bar(['Username'])
    return render(request,'deleteconn.html',{'form':form})
