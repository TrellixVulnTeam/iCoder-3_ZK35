from django.urls import path
from .views import *

app_name = 'colors'

urlpatterns = [
	path('', ColorListView.as_view(), name='color_view')
]