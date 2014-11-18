# Create your views here.
from django.http import HttpResponse

from projects_app.models import Project

def home(request):
    return HttpResponse("You're looking at question %s.")
