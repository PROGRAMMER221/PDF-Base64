from django.shortcuts import render, redirect
import pyshorteners as short
from .models import file
from django.conf import settings as st
import pyshorteners as pys

# Create your views here.
def IndexView(request):
    context = {
        'file': file.objects.all()
    }
    return render(request, 'index.html', context)

def Action(request):
    f = file()
    if request.method == 'POST':
        var = request.FILES['file_value']
        f.file = var
        url = request.build_absolute_uri(st.MEDIA_URL) + str(f.file)
        short_url = pys.Shortener(domain='https://0x0.st').nullpointer.short(url)
        f.tiny_url = short_url
        f.save()

    return redirect('/')