from django.http import HttpResponse
import time

now = time.time()

def epoch(request):
    return HttpResponse(now)