from django.urls import  path 
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path('delete/<int:list_id>' , delete , name='delete'),

]
