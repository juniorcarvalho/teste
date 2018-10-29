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
            sqltext=' select id, '+\
                    '        ifnull(data_distrato,"") as data_distrato, '+\
                    '        sum(1) as tot ' +\
                    'from core_titulo '+\
                    'group by data_distrato'
            context['result_sql_1'] = Titulo.objects.raw(sqltext)

        if 'sql2' in request.POST:
            sqltext = 'select c1.id, ' + \
                      '       c1.nro_titulo, ' + \
                      '       c1.valor_contrato_total as total_contrato, ' + \
                      '       (select sum(valor_original) from core_titulo as c2 ' + \
                      '        where c2.unidade_id=c1.unidade_id and ifnull(c2.data_baixa,0)<>0) as total_pago, ' + \
                      '        0 as total_pago_amortizado, ' + \
                      '        (select sum(c3.valor_original) from core_titulo as c3 ' + \
                      '         where c3.unidade_id=c1.unidade_id and ifnull(c3.data_baixa,0)=0) as saldo_devedor, ' + \
                      '        (select sum(c4.valor_original) from core_titulo c4 ' + \
                      '         where c4.unidade_id=c1.unidade_id and ifnull(c4.data_baixa,0)=0) as valor_inad, ' + \
                      '        (select ifnull(sum(current_date-c5.vencimento),0) from core_titulo c5 ' + \
                      '         where c5.unidade_id=c1.unidade_id and ifnull(c5.data_baixa,0)=0) as dias_inad ' + \
                      'from core_titulo c1' + \
                      ' group by 2'
            context['result_sql_2'] = Titulo.objects.raw(sqltext)

    return render(request, 'index.html', context=context)
