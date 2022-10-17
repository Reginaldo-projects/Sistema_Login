from colorama import init, Fore, Back, Style
init(autoreset=True)

#Criando função para verificar se existe usuário no arquivo usuario.txt

def verificar_usuarios (login, senha, acesso):
    novousuario = []
    try:
        with open('Usuarios.txt', 'r+', encoding='utf-8', newline='') as arquivo:
                for lin in arquivo:
                    lin = lin.strip(",")
                    novousuario.append(lin.split())
                for usuario in novousuario:
                    nome = usuario[0]
                    novasenha = usuario[1]
                    tipoacesso = usuario[2]
                    if login == nome and acesso == tipoacesso and senha == novasenha:
                        return True

    except FileExistsError:
        return False
    arquivo.close()
# Incluindo novos usuários no arquivo txt.
#login='rodrigo'
#senha = '123457'
#acesso='basico'
#criadopor = 'reginaldo'
#verificando usuários
#user = verificar_usuarios(login,senha, acesso)
#print(user)
#verificando o usuário existe
#if user == True:
#    print(Fore.RED+'Usuário já existe')
#incluindo o novo usuário
#else:
#    with open('Usuarios.txt','a+', encoding='utf-8',newline='')as arquivo:
#        arquivo.writelines(f'{login} {senha} {acesso} {criadopor}\n')
#        print(Fore.GREEN+'Cadastro realizado com sucesso')
#    arquivo.close()

