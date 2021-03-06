# Generated by Django 2.1.2 on 2018-10-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=50)),
                ('ie', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1)),
                ('estadocivil', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('conjuge', models.CharField(max_length=50)),
                ('cpf_conjuge', models.CharField(max_length=50)),
                ('nascimento_conjuge', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_titulo', models.IntegerField()),
                ('parcela', models.IntegerField()),
                ('indice_correcao', models.CharField(max_length=50)),
                ('tipo_correcao', models.CharField(max_length=50)),
                ('data_aniversario', models.DateField(blank=True, null=True)),
                ('perc_juros', models.FloatField()),
                ('tipo_juros', models.CharField(max_length=10)),
                ('vencimento', models.DateField(blank=True, null=True)),
                ('valor_original', models.FloatField()),
                ('saldo_devedor', models.FloatField()),
                ('tipo_baixa', models.CharField(max_length=20)),
                ('data_baixa', models.DateField(blank=True, null=True)),
                ('valor_bruto', models.FloatField()),
                ('valor_desconto', models.FloatField()),
                ('valor_liquido', models.FloatField()),
                ('juros', models.FloatField()),
                ('multa', models.FloatField()),
                ('valor_correcao', models.FloatField()),
                ('juros_prices_ac', models.FloatField()),
                ('data_distrato', models.DateField(blank=True, null=True)),
                ('valor_contrato_total', models.FloatField()),
                ('mes_base', models.CharField(max_length=6)),
                ('cliente', models.ForeignKey(on_delete=False, to='core.Cliente')),
                ('empreendimento', models.ForeignKey(on_delete=False, to='core.Empreendimento')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('tipo_imovel', models.CharField(max_length=50)),
                ('area', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='titulo',
            name='unidade',
            field=models.ForeignKey(on_delete=False, to='core.Unidade'),
        ),
    ]
