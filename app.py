import PySimpleGUI as sg
from usuarios import*

#janela login
def login_inicial ():
    #tema
    sg.theme("DarkBlue2")
    sg.set_global_icon('favicon.ico')

    layout = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario',font='Arial',size=(26,1),text_color='white')],
        [sg.Text('Senha')],
        [sg.Input(key='senha',password_char='*',font='Arial',size=(26,1),text_color='white')],
        [sg.Button('login',size=(8, 1),button_color=('white', 'green')),sg.Button('Cancelar',size=(8, 1),button_color=('white', 'red')),sg.Button('Cadastrar',size=(8, 1),button_color=('white', 'blue'))],
        [sg.Text('', key='mensagem',font='Arial',text_color='white')],
    ]
    return sg.Window('Tela de Login',size=(280, 180), margins=(10,0),layout=layout, finalize=True,)

#janela login adm
def login_adm ():
    layout = [
        [sg.Text('Administrador', text_color='white')],
        [sg.Input(key='administrador',text_color='white')],
        [sg.Text('Senha')],
        [sg.Input(key='senhaadm',password_char='*',text_color='white')],
        [sg.Button('Entrar',size=(8, 1),button_color=('white', 'green')), sg.Button('Voltar',size=(8, 1),button_color=('white', 'blue'))],
        [sg.Text('',key='mensagem')]

    ]

    return sg.Window('Senha Administrador',size=(280, 150), margins=(10,0),layout=layout,finalize=True)

#janela de cadastro
def login_cadastrar ():
    layout = [
        [sg.Text('Administrador')],
        [sg.Input(key='novousuario',text_color='white')],
        [sg.Text('Digite a senha')],
        [sg.Input(key= 'novasenha',password_char='*',text_color='white')],
        [sg.Radio('basico',1,key='basico'),sg.Radio('administrador',1,key='adm')],
##        [sg.Checkbox('Usuário Básico',key='basico'),sg.Checkbox('Administrador',key='adm')],
        [sg.Button('Cadastrar',button_color=('white', 'green'),size=(8, 1)),sg.Cancel('Sair',button_color=('white', 'red'),size=(8, 1))],
        [sg.Text('',key='mensagem',font='Arial',text_color='white')]
    ]
    return sg.Window('Tela de Cadastro',layout=layout, finalize=True)


#ocultando as janelas
janela1,janela2, janela3 = login_inicial(),login_adm().hide(),login_cadastrar().hide()
#faça até
while True:
    #sair do sistema
    window, evento, valores = sg.read_all_windows()
    if window ==janela1 and evento  == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    #verificando login
    if window == janela1 and evento == 'login':
        #loop for para passar verificar usuários básicos e Administrador
        for ver in range(0,2):
            usuario = valores['usuario']
            senha = valores['senha']
            log1 = verificar_usuarios(usuario, senha,acesso="Basico")
            log2 = verificar_usuarios(usuario, senha, acesso="Administrador")
            if log1 ==True or log2 == True:
               log=True
            else:
                log=False
        if log == True:
            janela1['mensagem'].update('Login feito com sucesso')
        else:
            sg.popup('Atenção', 'senha ou usuário incorreto')
#definindo o botão cadastrar,ocultando a janela1 e criando a janela2
    if window ==janela1 and evento == 'Cadastrar':
        janela1.hide()
        janela2=login_adm()
#definindo o botão voltar para a janela1
    if window == janela2 and evento == sg.WIN_CLOSED or evento == 'Voltar':
        janela1.un_hide()
        janela2.hide()
        janela1['mensagem'].update('')
#abrindo a tela de login adm
    elif window == janela2 and evento == 'Entrar':
        tpoacesso ='Administrador'
        usuarioadm = valores['administrador']
        admsenha = valores['senhaadm']
        #velidadno login no arquivo usuario.txt
        adm = verificar_usuarios(usuarioadm,admsenha,tpoacesso)
        if adm == True:
            janela2['mensagem'].update('Acesso autorizado')
            janela2.hide()
            janela3 = login_cadastrar()
            janela1.hide()
            usuarioadm = usuarioadm
#retorno para usuário que não possui cadastro
        else:
            sg.popup('Atenção','A senha ou usuário está incorreto ou certifique que você é um usuário Administrador')
#definindo o botao sair,ocultando a janela3 e exibindo a janela1
    if window == janela3 and evento == sg.WIN_CLOSED or evento == 'Sair':
            janela3.hide()
            janela1.un_hide()
            janela3['mensagem'].update('')
            janela1['mensagem'].update('')
#cadastrando novos usuarios e validando acesso
    if window == janela3 and evento == 'Cadastrar':
        novoacesso = valores['novousuario']
        novasenha = valores['novasenha']
        tipoacesso2 = valores['adm']
        tipoacesso = valores['basico']
        if tipoacesso == False and tipoacesso2 == False or novasenha=="" or novoacesso=="":
            sg.popup('Preencha todos os campos para prosseguir',title='Atenção')
        else:
            if tipoacesso == True:
                tipoacesso = "Basico"
            else:
                tipoacesso ="Administrador"
            novoacesso = valores['novousuario']
            novasenha = valores['novasenha']
            novo = verificar_usuarios(novoacesso,novasenha,tipoacesso)
            if novo == True:
                sg.popup('Usuário já existe nos registros')
            else:
                with open('Usuarios.txt', 'a+', encoding='utf-8', newline='') as arquivo:
                    arquivo.writelines(f'\n{novoacesso} {novasenha} {tipoacesso} {usuarioadm}')
                    janela3['mensagem'].update('Cadastro realizado com Sucesso')
                    arquivo.close()
#Fim



