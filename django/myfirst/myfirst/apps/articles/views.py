from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

# """to run the program in gitpod use python3 manage.py runserver"""

def test(request):
    return HttpResponse('Test Page')

