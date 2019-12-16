from datetime import datetime, date, time

agora = datetime.now()
hoje = date.today()
depois = datetime.now()


agoraParsado = datetime.strftime(agora, '%d/%m/%Y %H:%M')
print(agoraParsado)

print(agora)
print(hoje)


dataString = datetime.strptime('31/07/2000', '%d/%m/%Y')
print(dataString)

if agora < depois:
    print('Iguar')
else:
    print('Divergente')


print(dataString.timestamp())

if agoraParsado < datetime.strftime(dataString, '%d/%m/%Y'):
    print('AgoraParsado maior')
else:
    print('dataString maior')

anoAtual = datetime.strptime('31/07/2019', '%d/%m/%Y')
aniversario = datetime.strptime('31/07/2000', '%d/%m/%Y')

if aniversario > anoAtual:
    print('Vote')
else:
    print('Aí sim')

if anoAtual > aniversario:
    print('Ano menor')

print(type(anoAtual))

lista_nums = [100, 200, 300, 400, 500, 600, 700, 800]
#
# for item in range(len(lista_nums)):
#     lista_nums[item] += 1000
# print(lista_nums)

def funcaoIterativa():
    for num in lista_nums:
        print(num)
def funcaoRecursiva(key):
    if key >= len(lista_nums):
        return 'end'
    print(lista_nums[key])
    return funcaoRecursiva(key+1)

print(funcaoRecursiva(0))
print(funcaoIterativa())

# Verificando se a entrada está dentro de um determinado periodo

carro_alugado_periodo = [('11/10/2019', '12/11/2019')]

dataInserida = str(input('Insira a data DD/MM/AA\n'))

dataFormatada = datetime.strptime(dataInserida, '%d/%m/%Y')

def verificaSeOCarroEstaAlugadoPorPeriodo(data):
    for periodo in carro_alugado_periodo:
        inicio = datetime.strptime(periodo[0], '%d/%m/%Y')
        fim = datetime.strptime(periodo[1], '%d/%m/%Y')
        print(inicio)
        print(data)
        print(fim)
        if inicio < data < fim:
            print('Tá alugado')

def verificaEntreDuasDatas(tupleData):
    dataIni = datetime.strptime(tupleData[0], '%d/%m/%Y')
    dataEnd = datetime.strptime(tupleData[1], '%d/%m/%Y')
    for periodo in carro_alugado_periodo:
        inicio = datetime.strptime(periodo[0], '%d/%m/%Y')
        fim = datetime.strptime(periodo[1], '%d/%m/%Y')
        # A verificação é a seguinte
        if inicio < dataIni < fim or inicio < dataEnd < fim or dataIni < inicio < dataEnd or dataIni < fim < dataEnd:
            print('Tá alugado entre o período')
        # if inicio < dataIni < fim or inicio < dataEnd < fim or dataIni < inicio < dataEnd or dataIni < fim < dataEnd:



verificaSeOCarroEstaAlugadoPorPeriodo(dataFormatada)

duas_datas = ('10/07/2019', '22/12/2019')
verificaEntreDuasDatas(duas_datas)


def verificaAluguelRecursivamente(dataTuple, index):
    initialDate = datetime.strptime(dataTuple[0], '%d/%m/%Y')
    endDate = datetime.strptime(dataTuple[1], '%d/%m/%Y')

    if index >= len(carro_alugado_periodo):
        return 'Finalizado'

    period = carro_alugado_periodo[index]
    inDate = datetime.strptime(period[0], '%d/%m/%Y')
    enDate = datetime.strptime(period[1], '%d/%m/%Y')
    if initialDate < inDate < endDate or initialDate < enDate < endDate or inDate < initialDate < enDate or inDate < endDate < endDate:
        print('Existe uma reserva')
    else:
        return verificaEntreDuasDatas(dataTuple, index+1)

verificaAluguelRecursivamente(duas_datas, 0)

# def verificaAluguelRecursivamenteComListaDeTupla(listTuple, indexTup, index):
#     initialDate = datetime.strptime(dataTuple[indexTup][0], '%d/%m/%Y')
#     endDate = datetime.strptime(dataTuple[indexTup][1], '%d/%m/%Y')
#
#     if index >= len(listTuple):
#         if index >= len(carro_alugado_periodo):
#             return 'Finalizado'
#
#     period = carro_alugado_periodo[index]
#     inDate = datetime.strptime(period[0], '%d/%m/%Y')
#     enDate = datetime.strptime(period[1], '%d/%m/%Y')
#     if initialDate < inDate < endDate or initialDate < enDate < endDate or inDate < initialDate < enDate or inDate < endDate < endDate:
#         print('Existe uma reserva')
#     else:
#         return verificaEntreDuasDatas(dataTuple, indexTup + 1, index + 1)
#
# verificaAluguelRecursivamenteComListaDeTupla([('10/10/2019', '10/11/2019'), ('10/01/2020', '10/11/2020')], 0, 0)
