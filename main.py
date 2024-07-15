from PySimpleGUI import PySimpleGUI as sg 

#layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login ?')],
    [sg.Button('Entrar')]
] 
#janela
janela = sg.Window('Tela de login', layout)
#ler os eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'admin' and valores['senha'] == '0103':
            print('Bem-vindo a aplicação')

# LEIA O README.MD
