import random
import locale
from datetime import datetime
import sys

# Caracteres que compõem a senha
pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '%', '&', '!']

password = ""

# Determinando o local para pt-Bt
locale.setlocale(locale.LC_ALL, 'pt-Br.utf-8')

# Determinar os valores de data e hora
data_atual = datetime.today()
data_completa = data_atual.strftime('%d.%m.%y %H%M%S')
data_texto = data_atual.strftime('%d/%m/%y às %H:%M:%S')

# Criar arquivo com os dados de acesso
def criar_arquivo():
    try:
        arquivo = open(f'{cadastro} {data_completa}.txt', 'a')
        arquivo.write(f'Seus dados de acesso para {cadastro} são: \n\n')
        arquivo.write(f'Login: {login} \nSenha: {password}')
        arquivo.write(f'\n\nDados gerados em {data_texto}.')
        arquivo.write('\n\nSenha gerada pela biblioteca "random".\nPrograma desenvolvido em Python por Christian Oliveira.')
    except:
        print('Não foi possível criar o arquivo com os dados informados. \nFavor entrar em contato com o adminstrador do sistema! \nCódigo de erro: Errx001')

# Entrada de dados
cadastro = input('Digite o nome do site/programa para qual será a senha será gerada: ')
login = input('Digite o login para qual a senha será gerada: ')
qty_caracteres = int(input('Digite a quantidade de caracteres desejados: '))

# Execução do programa
try:
    for x in range(qty_caracteres):
        password = password + random.choices(pass1)[0]

    print('Confirme os dados de acesso:\n')
    print(f'Site/Programa: {cadastro}\nLogin: {login}\nSenha: {password}\n')
    confirm = input('Deseja gravar o arquivo? (S/N): ')

    if confirm == 's' or confirm == 'S':
        try:
            criar_arquivo()
            print(f'O arquivo contendo os dados de acesso para {cadastro} foi exportado com sucesso!')
        except:
            print('Não foi possível criar o arquivo com os dados informados. Favor entrar em contato com o adminstrador do sistema! \nCódigo de erro: Errx003')
    else:
        print('Os dados não foram gravados.\nO programa será encerrado...')
        sys.exit()
except:
    if confirm != 's' or confirm != 'S':
        sys.exit()
    else:
        print('Não foi possível gerar a senha com os dados informados. Favor entrar em contato com o administrador do sistema!. \nCódigo de erro: Errx002')
