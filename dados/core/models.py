from django.db import models


class Empreendimento(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)


class Cliente(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    cpf = models.CharField(max_length=50)
    ie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    estadocivil = models.CharField(max_length=10)
    endereco = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    conjuge = models.CharField(max_length=50)
    cpf_conjuge = models.CharField(max_length=50)
    nascimento_conjuge = models.DateField()


class Imovel(models.Model):
    codigo_unidade = models.CharField(max_length=10)
    tipo_imovel = models.CharField(max_length=50)
    area = models.FloatField()


class Titulo(models.Model):
    empreendimento = models.ForeignKey('Empreendimento', on_delete=False)
    imovel = models.ForeignKey('Imovel', on_delete=False)
    cliente = models.ForeignKey('Cliente', on_delete=False)
    nro_titulo = models.IntegerField()
    parcela = models.IntegerField()
    indice_correcao = models.CharField(max_length=50)
    correcao = models.CharField(max_length=50)
    data_aniversario = models.DateField()
    perc_juros = models.FloatField()
    tipo_juros = models.CharField(max_length=10)
    vencimento = models.DateField()
    valor_original = models.FloatField()
    saldo_devedor = models.FloatField()
    tipo_baixa = models.CharField(max_length=20)
    data_baixa = models.DateField()
    valor_bruto = models.FloatField()
    valor_desconto = models.FloatField()
    valor_liquido = models.FloatField()
    juros = models.FloatField()
    multa = models.FloatField()
    correcao = models.FloatField()
    juros_prices_ac = models.FloatField()
    data_distrato = models.DateField()
    valor_contrato_total = models.FloatField()
    mes_base = models.CharField(max_length=6)