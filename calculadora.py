
print('calculadora de anúncio')

def calculo(valor_x):
    click=float(valor_x) * 0.12
    comp=float(click*0.15)
    valor_y=float(comp)*40
    return valor_y

valor=(input('digita o valor do investimento:'))
v1=float(valor)
v2=float()
v3=float()
v4=float()

valor*30
v2 = calculo(v1)
v3 = calculo(v2)
v4 = calculo(v3)
max_v=float(v1+v2+v3+v4)
print('Alcance máximo de visualizações:{}'.format(max_v))





