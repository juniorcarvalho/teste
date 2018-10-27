from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from dados.core import importar


def index(request):
    context = {}
    if request.method == 'POST' and request.FILES['arquivo']:
        myfile = request.FILES['arquivo']
        if myfile is not None:
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = os.path.join(settings.MEDIA_ROOT, filename)
            importar.importar_csv(uploaded_file_url)
        context['filename'] = uploaded_file_url
    return render(request, 'index.html', context=context)
