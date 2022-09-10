# Arius-Sistemas-Backup-NFCE-v3.0

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="https://raw.githubusercontent.com/leandroSJ/arius_backup_nfce_v2.0/master/windows/icon/log.png" alt="Imagem de log">

> Programa desenvolvido para atender uma demanda local, com objetivo de consumir poucos recursos da máquina, projetado por Leandro de Jesus
"Estudante e amante da tecnologia". É verdade que já existe soluções para esses problemas de backup como o próprio app do google drive, mas
ele tem um pequeno defeito que é consumir muitos recursos das máquinas em que ele precisa ficar sincronizado, por isso sentir a necessidade
de criar uma solução simples, rápida e prática.

### O que o Arius-Sistemas-Backup-NFCE-v3.0 faz?

- [x] Faz uma varredura na rede do servidor através do loop #>> `for root, subFolder, filename in os.walk(server)`
- [x] Consulta cada pasta e subpastas através do loop #>> `for folder in subFolder:`
- [x] Verifica se existe alguma pasta com a data do dia anterior no formato AAA-MM-DD. com a condição #>> `if self.last_day in folder:`
- [x] Se encontrar o arquivo inicia o processo de cópia #>> `shutil.copytree(self.server_file, self.hd_file)`
- [x] Copacta o arquivo  no formato .7zip no local em que foi copiado #>> `shutil.make_archive(name_archive, extension, local)`
- [x] remove a pasta que ficou sem compactação #>> `shutil.rmtree(self.hd_file)`
- [x] Envia a Pasta compactada ao Google Drive #>> `archivo.Upload()`
- [x] Copia arquivos de configuração do servidor KW, e Servidor ARIUS RETAGUARDA. para local designado pelo usuário no arquivo
`arius_path.yml`

## 💻 Pré-instalação
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Instale a versão mais recente do `Python` se você não tem instalado em https://www.python.org/
* Instale o ambiente virtual `pip install virtualenv`
* Crie um ambiente virtual `python -m venv nome_do_ambiente`
* Ative seu ambiente virtual abrindo o Windows Power shell como ADM e execute esse comando `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` digite S para aceitar e pronto.
* Agora basta abrir a pasta do projeto e executar no terminal o arquivo `Activate.ps1` localizado em `nome_do_ambiente\bin\Activate.ps1`
* Atualize o pip `python -m pip install --upgrade pip`

## 🚀 Instalando Arius-Sistemas-Backup-NFCE-v3.0

Para instalar o <Arius-Sistemas-Backup-NFCE-v3.0>, siga estas etapas:
 
 `Em breve terá um video explicando  e mostrando na prática`
 Suponho que já estar com seu ambiente todo preparado para instalar novos Pacotes

 Vamos instalar todas as pendências:

 pip install -r requirements.txt

 Execute o arquivo `quickstart.py` ele vai ser responsável por fazer sua autenticação
 no Google Drive Faça login com sua conta Google caso apareça algum aviso informando que
 O Google não verificou este app clique em avançar e em seguida clique em 
 `Acessar Backup NFCE (não seguro)`

 Tenha calma não se assuste, o processo de autenticar uma aplicação que consome as apis
 do Google tem muita burocracia e exigências então eu optei por não fazer isso agora, por
 isso eles dizem que a aplicação não é segura.
 
 continue e faça login com seu e-mail e senha
 Agora perceba que um novo arquivo foi gerado com o nome credentials.json esse arquivo será
 responsavel por fazer a autenticação a cada vez que você executar a aplicação.

 Agora abra a pasta <config> e dite o arquivo `arius_path.yml`

filial_nome: Nome_do_Arquivo
filial_server_local: link_do_arquivo na rede ex: -> C:\\users\meu_caminho
filial_hd_local: local_onde_quer_copiar
filial_compact: mesmo_local_para_compactar
filial_filePath: mesmo_local_para_linkar_o_arquivo
filial_googlePath: mesmo_local_para_mandar_para_google_drive
filial_link_drive: Código da pasta -> entre na pasta do google drive e veja na url o código da
pasta está sempre após o /folders/Código_da_pasta Geralmente é um monte de caracteres aleatório

Abra o arquivo `arius_path.yml` você verá um exemplo comentado com # ai talvez entenda melhor

Feito isso basta executar seu programa se você tiver feito tudo certo ele vai iniciar o processo de
Backup Em modo CLI e você pode acompanhar o processo que ele está executando

## 📫 Contribuindo para <Arius-Sistemas-Backup-NFCE-v3.0>
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os 
contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado---> Para contribuir com
<nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.
6. Qualquer dúvida entra em conta via e-mail: leandro.dejesus@outlook.com.br coloca no assunto arius_backup_nfce_v3.0

Como alternativa, consulte a documentação do GitHub em 
[como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
Desenvolvido com Python3, faça uma versão deste programa em sua linguagem de programação.
