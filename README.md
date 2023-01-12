# Arius-Sistemas-Backup-NFCE-v3.0
Arius Sistemas Backup NFCE  - Realiza backups dos arquivos xml com informações ficais de venda da empresa, ou seja, salva uma cópia do cupom fiscal "Nota fiscal do Consumidor Eletrônica" NFCE

# Arius_backup_NFCE - feito Para usuários do sistema Arius
## Caso tenha interesse entre em contato que eu te explico como funciona

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="https://raw.githubusercontent.com/leandroSJ/Arius-Sistemas-Backup-NFCE-v4.0/main/icon/backup-nfce.png" alt="Tela do cmd windows">

> Programa desenvolvido para atender uma demanda local, com objetivo de consumir poucos recursos da máquina, projetado por Leandro SJ "Estudante e amante da tecnologia". É verdade que já existe soluções para esses problemas de backup como o próprio app do google drive, mas ele tem um pequeno defeito que é consumir muitos recursos das máquinas em que ele precisa ficar sincronizado, por isso sentir a necessidade de criar uma solução simples, rápida e prática.
### O que o arius_backup_nfce faz?

- [x] Faz uma varredura na rede do servidor através do loop >> for root, subFolder, filename in os.walk(server)
- [x] Consulta cada pasta e subpastas através do loop >> for folder in subFolder:
- [x] Verifica se existe alguma pasta com a data do dia anterior no formato AAAA-MM-DD. com a condição >> if self.last_day in folder:
- [x] Se encontrar o arquivo inicia o processo de cópia >> shutil.copytree(self.server_file, self.hd_file)
- [x] Compacta o arquivo  no formato 7zip no local em que foi copiado >> shutil.make_archive(name_archive, extension, local)   
- [x] remove a pasta que ficou sem compactação >> shutil.rmtree(self.hd_file)
- [x] Envia a Pasta compactada ao Google Drive >> archivo.Upload()
- [x] Copia arquivos de configuração do servidor KW, e Servidor ARIUS RETAGUARDA. para local designado pelo usuário no arquivo configurar-bakckup.yml

## 💻 Requisitos
[x] Windows 8 ou superior
[x] Python 3 ou superior

## 💻 Pré-instalação
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Instale a versão mais recente do `Python` se você não tem instalado em https://www.python.org/
* Baixe uma ide eu recomendo o VisualStudio Code por ser mais fácil de configurar você pode baixar em https://code.visualstudio.com/Download
* Atualize a versão do pip Abra o cmd do windows e digite `python -m pip install --upgrade pip` "o pip é um gerenciador de pacotes com ele você consegue baixar as dependências do python"

* Ative seu ambiente virtual abrindo o Windows Power shell como ADM e execute esse comando `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
digite S para aceitar e pronto.
* Agora basta abrir a pasta do projeto no vscode e executar no terminal o arquivo `Activate.ps1` localizado em `env\Scripts\Activate.ps1`
digite esse comando para ativar o ambiente: c:\backup_nfce\env\Scripts\Activate.ps1
* Atualize o pip `python -m pip install --upgrade pip` se ja estiver atualizado ele vai informar que ja foi atualizado.
* mude 

## 🚀 Instalando <Backup_NFCE>

Caso você não tenha muito conhecimento e não saiba como preparar um ambiente virtual python, siga essas etapas:

baixe o python: https://www.python.org/ftp/python/3.11.1/python-3.11.1-embed-amd64.zip

após fazer o download clique para instalar, na hora da instalação marque a 1ª caixinha [] para adicionar o python ao path do windows após concluir a instalação

Baixe a pasta Arius-Sistemas-Backup-NFCE-v4.0
após concluir o download abra o explorador de arquivos altere o nome dela para `backup_nfce` e copie ela para o disco C:\

-> entre na pasta `backup_nfce` > Acesse a pasta `dist`
abra a pasta `backup-nfce-v4.0-2023`nessa pasta você vai encontrar o arquivo executável `backup-nfce-v4.0-2023.exe`

clique com o botão direito em cima deste arquivo e escolha a opção `enviar para > Area de trabalho`

agora vá para a pasta  `config`localizada em C:\backup_nfce\config
abra o arquivo `arius_path.yaml` com o bloco de notas e altere o local onde o servidor faz o backup dos arquivos xml. Se precisar de ajuda manda uma mensagem para mim no email leandrosj@proton.me que eu estou disposto a ajudar.


<img src="https://raw.githubusercontent.com/leandroSJ/Arius-Sistemas-Backup-NFCE-v4.0/main/icon/Captura de tela de 2023-01-11 23-02-15.png" alt="Tela do cmd windows">

depois de definir os paths corretamente teste o programa. clique para executar o backup-nfce-v4.00-2023.exe que está na sua área de trabalho e veja o resultado.
```

## 📫 Contribuindo para <Backup_NFE>
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com <nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
