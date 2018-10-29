from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from dados.core import importar
from dados.core.models import Titulo


def index(request):
    context = {}
    if request.method == 'POST':
        if not 'sql1' in request.POST and not 'sql2' in request.POST and request.FILES['arquivo']:
            myfile = request.FILES['arquivo']
            if myfile is not None:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = os.path.join(settings.MEDIA_ROOT, filename)
                importar.importar_csv(uploaded_file_url)
            context['filename'] = uploaded_file_url

        if 'sql1' in request.POST:
            context['result_sql_1'] = Titulo.objects.raw(
                'select id,data_distrato, count(*) as tot from core_titulo group by data_distrato')

        if 'sql2' in request.POST:
            context['result_sql_2'] = Titulo.objects.raw(
                'select id,nro_titulo,sum(valor_original) as total_contrato,sum(valor_liquido) as total_pago,sum(saldo_devedor) as saldo_devedor from core_titulo group by 2'
            )

    return render(request, 'index.html', context=context)
