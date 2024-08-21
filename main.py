from cinematica import *

while True:

    mostrar_menu()

    opcao = input('Opção dp usuario: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace(',','.'))
            h = float(input('Informe a altura em metros: ').replace(',','.'))
            print(f'Energia potencial: {calcular_ep(m, h):,.2f} J.')
            continue
        case '2':
            m = float(input('Informe a massa em kg: ').replace(',','.'))
            v = float(input('Informe a velocidade e, m/s: ').replace(',','.'))
            print(f'Energia cinetica: {calcular_ec(m, v):,.2f} J.')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opcao invalida.')
            continue