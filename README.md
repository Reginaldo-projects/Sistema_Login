


<h1 align="center">💻Sistema de Login</h1>
<br/>
<br/>
<!--<a align="center"> <img src="./img/Logo_regis.svg" alt="portfolio" width="80" height="400"/> </a>## -->

### Tópicos 

- 🏷[Descrição](#descrição)

- 💻[Resultado](#resultado)

- 🗳[Link](#link)

- 📌[Licença](#licença)

- 👍[Autor](#autor)




## 🏷 Descrição 

<p align="justify">
Tela de Login criada com PySimpleGUi uma pacote de interface gráfica, onde foi desenvolvido a logíca de verificação de acesso e tipo de acesso

</p>


## 💻 Resultado

<p align="justify">
Função para validação de usuários
</p>
</br>
<pre>
<code>
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
</code>
</pre>
</br>
<p align="justify">
Tela inicial , autenticação com usuário e senha.
</p>
</br>
<a align="center"> <img src="./img/Tela_inicial.png" alt="portfolio" width="180" height="120"/> </a> 

##
</br>
<p align="justify">
Tela login administrador , nessa tela apenas usuários com cadastro Administrador pode cadastrar novos usuários.
</p>
</br>
<a align="center"> <img src="./img/Tela_login_adm.png" alt="portfolio" width="180" height="120"/> </a> 

##

</br>
<p align="justify">
Tela de cadastro , Tela com acesso apenas para administradores ,nessa tela será possivel incluir novos usuários básicos ou administrador.
</p>
</br>
<a align="center"> <img src="./img/Tela_cadastro.png" alt="portfolio" width="180" height="120"/> </a> 


## 🗳 Link
 
 <p>Projeto <a href="https://github.com/Reginaldo-projects/Sistema_Login/blob/main/app.py" target="_blank">aqui</a>.</p>




## 📌 Licença

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Reginaldo-projects/Sistema_Login/blob/main/LICENSE)


 ---

## 👍 Autor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Reginaldo-projects">
        <img src="https://avatars.githubusercontent.com/u/112530481" width="100px;" alt="projects"/><br>
        <sub>
          <b>Reginaldo Barbosa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

 
