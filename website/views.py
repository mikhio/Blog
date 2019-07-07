from django.http import HttpResponse

def main (request):
    return HttpResponse('<h1>This is main page.<h1/>')
