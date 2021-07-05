

def exibir_menu():
    print('Escolha opção:'
          ''
          '1. Cadastrar um anuncio'
          '2. Listar anuncios'
          '3. Procurar dados de anuncio'
          )

def cadastrar(anuncios):
     anuncio = input('Anuncio?')
     cliente = input('Cliente?')
     data_inicio = int(input('Data de início?'))
     data_fim = int(input('Data de início?'))
     investimento_dia = float(input('Investimento por dia:'))
     anuncios.append((anuncio,cliente,data_inicio,data_fim,investimento_dia))


def listar(anuncios):
    for anuncios in anuncios:
        anuncio,cliente,data_inicio,data_fim, investimento_dia = anuncios
        print(f'Anuncio:{anuncio},Cliente{cliente},Data de inicio{data_inicio},Data de Fim{data_fim},Investimento do dia:{investimento_dia}')

def buscar(anuncios)
    cliente_escolhido = input('Cliente?')
    for cliente in anuncios:
        cliente,data_inicio,data_fim, investimento_dia = anuncios
        if cliente == cliente_escolhido:
            print(f'Anuncio:{anuncio},Cliente{cliente},Data de inicio{data_inicio},Data de Fim{data_fim},Investimento do dia:{investimento_dia}')
            break
        else:
            print(f'Anuncio de cliente{cliente_escolhido} não encontrado')
