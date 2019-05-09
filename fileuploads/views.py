from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    

    if request.method == 'POST':

        uplaodedFile = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uplaodedFile.name, uplaodedFile) #returns actual uploaded file name which means if uploaded file existed and it's overwritten, it will return overwritten name

    return render(request, 'index.html', context={'content': 'File Uploaded Successfully!'})