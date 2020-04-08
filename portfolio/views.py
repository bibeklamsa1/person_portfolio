from django.shortcuts import render
from .models import Project
# Create your views here.
def portfolio(req):

    projects = Project.objects.all()

    return render(req,"portfolio.html",{'projects':projects})