from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('charts',views.charts,name='charts'),
    path('documentation',views.charts,name='documentation'),
    path('dropdowns',views.charts,name='dropdowns'),
    path('icons',views.charts,name='icons'),
    path('login',views.charts,name='login'),
    path('register',views.charts,name='register'),
    path('tables',views.charts,name='tables'),
    path('typography',views.charts,name='typography'),
    path('buttons',views.buttons,name='buttons'),
    path('forms',views.forms,name='forms'),



    
]
