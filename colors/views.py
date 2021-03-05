from django.shortcuts import render
from .models import Color
from django.views.generic import ListView


class ColorListView(ListView):
	model = Color
	template_name = 'main.html'
