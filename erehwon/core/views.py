from django.shortcuts import render
from django.views.generic import TemplateView


def homepage(request):
    """
    The Homepage view.
    """
    return render(request, 'index.html')
