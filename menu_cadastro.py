import funcao_menu as f2

print('calculadora de anúncio')
def main():
    anuncios=[]

    while true:
        f2.exibir_menu()
        opcao=int(input('Opção?'))
        if opcao ==1:
            f2.cadastrar(anuncios)
        elif opcao ==2:
                f2.listar(anuncios)
        elif opcao==3:
            f2.buscar(anuncios)
        else:
            print('Opção inválida')




