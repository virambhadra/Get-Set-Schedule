from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from .forms import *


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
    form = Bar(connection.introspection.table_names())
    #print(connection.introspection.table_names())
    # form = [str(Foo(prefix=i)) for i in range(4)]
    # form = '\n'.join(form)
    #print(form)
    return render(request,'makett.html',{'form':form})



def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


