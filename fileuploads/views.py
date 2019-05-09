from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
# Create your views here.

def index(request):
    
    context = {}

    if request.method == 'POST':

        uplaodedFile = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uplaodedFile.name, uplaodedFile) #returns actual uploaded file name which means if uploaded file existed and it's overwritten, it will return overwritten name

    if request.method != 'POST':
        path = os.path.join(settings.BASE_DIR, 'media')
        files = os.listdir(path)
        context['data'] = files

    return render(request, 'index.html', context)