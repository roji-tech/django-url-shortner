from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import uuid
from .models import Url

# Create your views here.


def index(request):
    return render(request, "index.htm")


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:6]
        short_url = Url(link=link, uuid=uid)
        short_url.save()
        return HttpResponse(uid)


def go_to_url(request, uid):
    try:
        url_details = Url.objects.get(uuid=uid)
    except:
        url_details = Url()

    if url_details.link.startswith("https://"):
        new_link = url_details.link
        return HttpResponseRedirect(new_link)

    elif url_details.link.startswith("http://"):
        new_link = url_details.link
        return HttpResponseRedirect(new_link)

    else:
        new_link = 'https://' + url_details.link
        return HttpResponseRedirect(new_link)
