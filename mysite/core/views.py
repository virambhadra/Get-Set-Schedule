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
import difflib


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
    submitbutton= request.POST.get("submit")

    profession = ''
    stream = ''
    hobbies = ''

    form = main_form(request.POST or None)
    if form.is_valid():
        profession = form.cleaned_data.get('profession')
        stream = form.cleaned_data.get('stream')
        hobbies = form.cleaned_data.get('hobbies')
        timetable = match(profession,stream)
        #print(timetable)
        request.session['timetable'] = timetable 
        return redirect('yourtt')
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
    timetable = request.session['timetable']
    time = ['6am','7am','8am','9am','10am','11am','12am','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm']
    request.session['time'] = time 

    table = list(zip(time,timetable))
    #print(table)
    return render(request,'yourtt.html',{'table':table})

def edittt(request):
    submitbutton= request.POST.get("submit")

    on_6am = ''
    on_7am = ''
    on_8am = ''
    on_9am = ''
    on_10am = ''
    on_11am = ''
    on_12am = ''
    on_1pm = ''
    on_2pm = ''
    on_3pm = ''
    on_4pm = ''
    on_5pm = ''
    on_6pm = ''
    on_7pm = ''
    on_8pm = ''
    on_9pm = ''

    time = ['on_6am','on_7am','on_8am','on_9am','on_10am','on_11am','on_12am','on_1pm','on_2pm','on_3pm','on_4pm','on_5pm','on_6pm','on_7pm','on_8pm','on_9pm']
    timetable = request.session['timetable']
    initial = dict(zip(time,timetable))
    form = am_pm(request.POST or None,initial=initial)
    if form.is_valid():
        on_6am = form.cleaned_data.get('on_6am')
        on_7am = form.cleaned_data.get('on_7am')
        on_8am = form.cleaned_data.get('on_8am')
        on_9am = form.cleaned_data.get('on_9am') 
        on_10am = form.cleaned_data.get('on_10am')
        on_11am = form.cleaned_data.get('on_11am')
        on_12am = form.cleaned_data.get('on_12am')
        on_1pm = form.cleaned_data.get('on_1pm')
        on_2pm = form.cleaned_data.get('on_2pm')
        on_3pm = form.cleaned_data.get('on_3pm')
        on_4pm = form.cleaned_data.get('on_4pm')
        on_5pm = form.cleaned_data.get('on_5pm')
        on_6pm = form.cleaned_data.get('on_6pm')
        on_7pm = form.cleaned_data.get('on_7pm')
        on_8pm = form.cleaned_data.get('on_8pm')
        on_9pm = form.cleaned_data.get('on_9pm')
        table = [on_6am,on_7am,on_8am,on_9am,on_10am,on_11am,on_12am,on_1pm,on_2pm,on_3pm,on_4pm,on_5pm,on_6pm,on_7pm,on_8pm,on_9pm]
        request.session['timetable'] = table
        return redirect('yourtt')
    '''submitbutton= request.POST.get("submit")

    profession = ''
    stream = ''
    hobbies = ''

    form = main_form(request.POST or None)
    if form.is_valid():
        profession = form.cleaned_data.get('profession')
        stream = form.cleaned_data.get('stream')
        hobbies = form.cleaned_data.get('hobbies')
        timetable = match(profession,stream)
        #print(timetable)
        request.session['timetable'] = timetable 
        return redirect('yourtt')'''
    return render(request,'edittt.html',{'form':form})

def myconnect(request):
    return render(request,'myconnect.html')

def addconn(request):
    form = Bar(['Username'])
    return render(request,'addconn.html', {'form':form})

def deleteconn(request):
    form = Bar(['Username'])
    return render(request,'deleteconn.html',{'form':form})

def match(profession,stream):
    df = pd.read_csv(r'mysite/static/data.csv')
    col_mapping = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]
    col_mapping_dict = {c[0]:c[1] for c in enumerate(df.columns)}
    profcard = df.iloc[:,:2]
    profcard=profcard.values.tolist()
    pf = []
    for i in range(len(profcard)):
        a = '_'.join(profcard[i]).replace(' ','_')
        pf.append(a)
        test = [profession,stream]
    i = pf.index(difflib.get_close_matches('_'.join(test).replace(' ','_'),pf)[0])
    z = df.iloc[i,:]
    z = list(z)
    return z[2:]