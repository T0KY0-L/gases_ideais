from time import sleep
print('Este é um programa que realiza o cálculo da equação dos gases ideais!')
sleep(2)
print(' Insira: \n[1] - Pressão \n[2] - Volume \n[3] -Nº de mole \n[4] - Temperatura')
sleep(2)
esc1 = input('Sua escolha:')
sleep(1.2)
print('Deseja trabalhar com o volume em L (0.082) ou m3 (8.31)?')
sleep(1.2)
esc2 = input('Sua escolha:')
sleep(1.2)
print('Temperatura em \n[5] - Celcius->Kelvin \n[6] - Kelvin->Celcius \n[7] - Kelvin ')
esc3 = input('Sua escolha:')
sleep(1.2)
pa = 101.325
if esc1 == '1' and esc3 == '5':
    print('[Cálculo de Pressão]')
    print('Informe os dados abaixo')
    sleep(1.2)
    n = float(input('Número de moles:'))
    t = float(input('Temperatura:'))
    v = float(input('Volume:'))
    if esc2 == 'm3':
        con = t+273
        reso = (n * 8.31 * con) / v
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}Pa.')
    elif esc2 == 'L':
        con = t+273
        reso = (n * 0.082 * con) / v
        resof = reso*pa
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}atm <-> {resof:.2f}Pa.')
elif esc1 == '1' and esc3 == '6':
    print('[Cálculo de Pressão]')
    print('Informe os dados abaixo')
    sleep(1.2)
    n = float(input('Número de moles:'))
    t = float(input('Temperatura:'))
    v = float(input('Volume:'))
    if esc2 == 'm3':
        con = t - 273
        reso = (n * 8.31 * con)/v
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}Pa.')
    elif esc2 == 'L':
        con = t - 273
        reso = (n * 0.082 * con)/v
        resof = reso * pa
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}atm <-> {resof:.2f}Pa.')
elif esc1 == '1' and esc3 == '7':
    print('[Cálculo de Pressão]')
    print('Informe os dados abaixo')
    sleep(1.2)
    n = float(input('Número de moles:'))
    v = float(input('Volume:'))
    if esc2 == 'm3':
        reso = (n * 8.31 * 273)/v
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}Pa.')
    elif esc2 == 'L':
        reso = (n * 0.082 * 273)/v
        resof = reso*pa
        print(f'De acordo aos dados inseridos, o valor da pressão é de {reso:.2f}atm <-> {resof:.2f}Pa.')
else:
    print('Os dados foram inseridos incorretamente, por favor tente novamente.')

if esc1 == '2' and esc3 == '5':
    print('[Cálculo de Volume]')
    print('Informe os dados abaixo')
    n = float(input('Número de Moles:'))
    t = float(input('Temperatura:'))
    p = float(input('Pressão:'))
    if esc2 == 'L':
        con = t + 273
        reso = (n * 0.082 * con)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}L.')
    elif esc2 == 'm3':
        con = t + 273
        reso = (n * 0.082 * con)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}m3.')
elif esc1 == '2' and esc3 == '6':
    print('[Cálculo de Volume]')
    print('Informe os dados abaixo')
    n = float(input('Número de moles:'))
    t = float(input('Temperatura:'))
    p = float(input('Pressão:'))
    if esc2 == 'L':
        con = t - 273
        reso = (n * 0.082 * con)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}L.')
    elif esc2 == 'm3':
        con = t - 273
        reso = (n * 8.31 * con)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}m3.')
elif esc1 == '2' and esc3 == '7':
    print('[Cálculo de Volume]')
    print('Informe os dados abaixo')
    n = float(input('Número de moles:'))
    p = float(input('Pressão:'))
    if esc2 == 'L':
        reso = (n * 0.082 * 273)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}L.')
    elif esc2 == 'm3':
        reso = (n * 8.31 * 273)/p
        print(f'De acordo aos dados inseridos, o valor do volume é de {reso:.2f}m3.')
else:
    print('Os dados foram inseridos incorretamente, tente novamente.')

if esc1 == '3':
    print('[Cálculo de Número de moles]')
    print('Informe os dados abaixo')
    mm = float(input('Massa molar:'))
    ms = float(input('Massa da substância:'))
    print(f'De acordo aos dados inseridos, o valor do nº de moles é de {mm*ms}moles.')
else:
    print('Os dados foram inseridos incorretamente, tente novamente.')

if esc1 == '4':
    print('[Cálculo de Temperatura]')
    print('Informe os dados abaixo')
    n = float(input('Número de mole:'))
    p = float(input('Pressão:'))
    v = float(input('Volume:'))
    if esc2 == 'L':
        reso = (p*v)/(n*0.082)
        print(f'De acordo aos dados inseridos, o valor da temperatura é de {reso:.2f}K')
    elif esc2 == 'm3':
        reso = (p*v)/(n*8.31)
        print(f'De acordo aos dados inseridos, o valor da temperatura é de {reso:.2f}K')
else:
    print('Os dados foram inseridos incorretamente, tente novamente.')