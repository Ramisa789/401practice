#this file routes the url 

from django.urls import path
from api.views import update_teacher, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('teachers/<int:id>/', update_teacher, name='update_teacher'),
]