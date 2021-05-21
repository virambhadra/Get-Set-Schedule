from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ttdivision/',views.ttdivision,name='ttdivision'),
    path('signup/', views.signup, name='signup'),
    path('tt/', views.tt, name='tt'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('makett/',views.makett,name='makett'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('table/',views.Table,name='table'),
    path('yourtt/',views.yourtt,name='yourtt'),
    path('edittt/',views.edittt, name='edittt'),
    path('myconnect/',views.myconnect, name='myconnect'),
    path('addconn/',views.addconn, name='addconn'),
    path('deleteconn/',views.deleteconn, name='deleteconn'),
    
]
