
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Welcome to my awsome eCart</h1>")