from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404
# # Create your views here.
# from .models import Author,Books


def allbook(request, c_slug=None):

    return render(request,'home.html')

