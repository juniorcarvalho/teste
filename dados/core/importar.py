import rows
from dados.core.models import Empreendimento, Cliente, Unidade
from types import SimpleNamespace
import datetime

def importar_csv(arquivo):
    if arquivo is None:
        raise ValueError('Informe o nome do arquivo CSV.')

    try:
        tabela = rows.import_from_csv(arquivo)
    except Exception as e:
        raise Exception(e)

    cod_empreendimento = 0
    cod_cliente = 0
    cod_unidade = 0

    for n in tabela:
        e = empreendimento(n)
        c = cliente(n)
        u = unidade(n)
        t = titulo(n)

        if cod_empreendimento != n.cdempreend:
            ep = Empreendimento()
            ep.codigo = e.codigo
            ep.nome = e.nome
            ep.endereco = e.endereco
            ep.bairro = e.bairro
            ep.cep = e.cep
            ep.cidade = e.cidade
            ep.categoria = e.categoria
            ep.save()

        if cod_cliente != n.codigo_cliente:
            cl = Cliente()
            cl.codigo = c.codigo
            cl.nome = c.nome
            cl.nascimento = c.nascimento
            cl.cpf = c.cpf
            cl.ie = c.ie
            cl.sexo = c.sexo
            cl.estadocivil = c.estadocivil
            cl.endereco = c.endereco
            cl.bairro = c.bairro
            cl.complemento = c.complemento
            cl.cep = c.cep
            cl.cidade = c.cidade
            cl.conjuge = c.conjuge
            cl.cpf_conjuge = c.cpf_conjuge
            cl.nascimento_conjuge = c.nascimento_conjuge
            cl.save()

        if cod_unidade != n.nuunidade:
            un = Unidade()
            un.codigo = u.codigo
            un.tipo_imovel = u.tipo_imovel
            un.area = u.area
            un.save()

        cod_empreendimento = n.cdempreend
        cod_cliente = n.codigo_cliente
        cod_unidade = n.nuunidade



def empreendimento(data):
    return SimpleNamespace(
        codigo=str(data.cdempreend),
        nome=data.nome_empreendimento,
        endereco=data.end_empreend,
        bairro=data.bairro_empreend,
        cep=data.cep_empreend,
        cidade=data.municipio_empreend,
        categoria=data.categoria,
    )


def cliente(data):
    if data.datanascimento.strip() != '':
        data1 = datetime.datetime.strptime(data.datanascimento.strip(), '%d-%m-%Y')
    else:
        data1 = None

    if data.datanascimentoconjuge.strip() != '':
        data2 = datetime.datetime.strptime(data.datanascimentoconjuge.strip(), '%d-%m-%Y')
    else:
        data2 = None

    return SimpleNamespace(
        codigo=data.codigo_cliente,
        nome=data.nome_cliente,
        nascimento=data1,
        cpf=data.nucpf,
        ie=data.nuincrest,
        sexo=data.flsexo,
        estadocivil=data.estadocivil,
        endereco=data.endcliente,
        complemento=data.compcliente,
        bairro=data.bairrocliente,
        cep=data.cep_cliente,
        cidade=data.municipiocliente,
        conjuge=data.conjuge,
        cpf_conjuge=data.nucpfconjuge,
        nascimento_conjuge=data2,
    )


def unidade(data):
    return SimpleNamespace(
        codigo=data.nuunidade,
        tipo_imovel=data.tipoimovel,
        area=data.area,
    )


def titulo(data):
    return SimpleNamespace(
        nro_titulo=data.titulo,
        parcela=data.parcela,
        indice_correcao=data.indice_correcao,
        tipo_correcao=data.tipocorrecao,
        data_aniversario=data.dataaniversario,
        perc_juros=data.percentual_juros,
        tipo_juros=data.tipojuros,
        vencimento=data.datavencimento,
        valor_original=data.valororiginalparcela,
        saldo_devedor=data.saldodevedorparcela,
        tipo_baixa=data.tipo_baixa,
        data_baixa=data.databaixa,
        valor_bruto=data.valorbruto,
        valor_desconto=data.valordesconto,
        valor_liquido=data.valorliquido,
        juros=data.jurosmora,
        multa=data.multamora,
        valor_correcao=data.correcaomonetaria,
        juros_prices_ac=data.jurospricesac,
        data_distrato=data.datadistrato,
        valor_contrato_total=data.valor_contrato_total,
        mes_base=data.mes_base,
    )
