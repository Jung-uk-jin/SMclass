
from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('write/',views.write,name='write'),

]
