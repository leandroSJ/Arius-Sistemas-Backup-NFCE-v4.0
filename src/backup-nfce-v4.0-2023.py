from datetime import date, timedelta, datetime
import shutil
import yaml
import os
from py7zr import pack_7zarchive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
 
class arius_backup:
    def __init__(self, company_name):            
        self.last_day = str(date.today() - timedelta(days=1))
        self.company_name = company_name
            
    def copy_nfce(self, server, hd):
        for root, subFolder, filename in os.walk(server):
            for folder in subFolder:                
                if self.last_day in folder:
                    self.server_file = os.path.join(root, folder)
                    self.hd_file = os.path.join(hd, self.checkMonth,folder)                
                    try:                       
                        log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')                         
                        file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                        file.write(f'{log_data ,self.company_name} Copiando arquivos.\n')
                              
                        print(f'{self.company_name} Copiando arquivos.')                        
                        shutil.copytree(self.server_file, self.hd_file)                                            
                        print(f'{self.company_name} Arquivos copiados para HD.')
                        file.write(f'{log_data, self.company_name} Arquivos copiados para HD.\n')
                        file.close()                                                                                          
                        pass                                       
                    except PermissionError as e:
                        print(f'{self.company_name} Sem permissao para acessar o arquivo!\n\n')
                    except FileExistsError as e:
                        print(f'{self.company_name} Você ja fez backup deste arquivo!\n\n')
                        log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')                         
                        file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                        file.write(f'{log_data ,self.company_name} Você ja fez backup deste arquivo!\n')
                        file.close()
                    except FileNotFoundError as e:
                        print(f'{self.company_name} Arquivo não encontrado. \n\n')                        
                        log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')                         
                        file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                        file.write(f'{log_data ,self.company_name} Arquivo não encontrado.!\n')
                        file.close()
                    except shutil.SameFileError as e:
                        pass                      

    def compress(self, path_name):
        for root, subFolder, filename in os.walk(path_name):
            for folder in subFolder:
                if self.last_day in folder:
                    name_archive = os.path.join(root, folder)                                     
                    shutil.register_archive_format ( '7zip' ,  pack_7zarchive ,  description = '7zip archive' )
                    extension = '7zip'        
                    local = name_archive                    
                    try:                                    
                        log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')           
                        file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                        file.write(f'{log_data, self.company_name} Compactando arquivos.\n') 
                        print(f'{self.company_name} Compactando arquivos.')
                        shutil.make_archive(name_archive, extension, local)   
                        print(f'{self.company_name} Arquivos compactados!')
                        file.write(f'{log_data, self.company_name} Arquivos compactados em 7zip!\n') 
                        file.close()
                    except FileExistsError as e:
                        print(f'{self.company_name} ESTE ARQUIVO JÁ FOI COMPACTADO!\n\n')
                    except FileNotFoundError as e:
                        pass
                                  
    def remove_folders(self, path_name):
            for root, subFolder, filename in os.walk(path_name):
                for folder in subFolder:                
                    if self.last_day in folder:
                        try:
                            log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')           
                            file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                            file.write(f'{log_data, self.company_name} Removendo pastas sem compactação.\n')

                            print(f'{self.company_name} Removendo pasta sem compactação.')
                            shutil.rmtree(self.hd_file)
                            print(f'{self.company_name} Pastas removidas.')
                            file.write(f'{log_data, self.company_name} Pastas removidas.\n')
                            file.close()
                        except:
                            pass
                        
    def copy_kw_erp(self, path_f, path_dst):
        date_today = date.today().strftime("%d-%m-%y")

        for root, dirs, files in os.walk(path_f):
            for file in files:                
                if date_today in file:        
                    server = os.path.join(root, file)
                    hd = os.path.join(path_dst, self.checkMonth, file)                                                                                                                           
                    try:      
                        log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')                                                                                                                
                        file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
                        file.write(f'{log_data, self.company_name} Copiando arquivos.\n')                        
                                                
                        print(f'{self.company_name} Copiando arquivos.\n')
                        shutil.copyfile(server, hd)
                        print(f'{self.company_name} Copiado com sucesso !\n\n')
                        file.write(f'{log_data, self.company_name} Copiado Com sucesso !.\n')
                        file.close()
                    except FileExistsError as e:
                        print(f'{self.company_name} O arquivo ja foi copiado\n\n')
                    except FileNotFoundError as e:
                        pass
                else:
                    pass
                                                        
    def months(self):
        months = { 1:'JANEIRO', 2:'FEVEREIRO', 3:'MARCO', 4:'ABRIL', 
                    5:'MAIO', 6:'JUNHO', 7:'JULHO', 8:'AGOSTO', 
                    9:'SETEMBRO', 10:'OUTUBRO', 11:'NOVEMBRO', 12:'DEZEMBRO'}
        
        self.currentMonth = date.today().strftime("%m")
        self.currentMonth = int(self.currentMonth)
        self.currentDate = date.today().strftime('%d')                  
        
        if self.currentDate == '1' and self.currentMonth == 1:
            self.currentMonth = 12
            self.checkMonth = months.get(self.currentMonth)
        
        elif self.currentDate == '1' and self.currentMonth != 12:
            self.currentMonth = self.currentMonth - 1
            self.checkMonth = months.get(self.currentMonth)
        else:            
            self.checkMonth = months.get(self.currentMonth)
        

    def google_auth(self):
        dir_credentials = 'credentials.json'
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = dir_credentials
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(dir_credentials)

        if gauth.credentials is None:
            gauth.LocalWebserverAuth(port_numbers=[8080])
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        
        gauth.SaveCredentialsFile(dir_credentials)
        credentials = GoogleDrive(gauth)
        return credentials

    def path_google_drive(self, file_path, google_path):
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if self.last_day in file:                    
                    try:
                        obsolete = os.path.join(root, file)
                        self.path_drive = os.path.join(google_path, self.checkMonth, file)                                  
                    except FileNotFoundError as e:
                        pass
                    except PermissionError as e:
                        pass
                        
    def file_upload(self, id_folder):       
        credentials = arius_backup.google_auth(self)
        archivo = credentials.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                        "id": id_folder}]})
        try:
            archivo['title'] = self.path_drive.split("\\")[-1]
            archivo.SetContentFile(self.path_drive)

            log_data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            file = open('C:\\backup_nfce\\config\\log_backup.txt', 'a')
            file.write(f'{log_data, self.company_name} Enviando para google drive.\n')

            print(f'\n\n{self.company_name} Enviando para google drive')
            archivo.Upload()
            print(f'\n\n{self.company_name} Enviado com sucesso!\n\n')
            file.write(f'{log_data, self.company_name} Enviado com sucesso!.\n\n\n')
            file.close()
        except AttributeError as e:
            pass
        except FileNotFoundError as e:
            pass    

with open('C:\\backup_nfce\\config\\arius_path.yml','r') as config:
    cfg = yaml.safe_load(config)
    
#Loja
    #NFCERESP
nfce_matriz_resp = arius_backup(company_name=cfg["matriz_nome_nfceresp"])
nfce_matriz_resp.months()
nfce_matriz_resp.copy_nfce(server=cfg["matriz_servidor_nfceresp"],hd=cfg["matriz_hd_nfceresp"])
nfce_matriz_resp.compress(path_name=cfg["matriz_hd_nfceresp"])
nfce_matriz_resp.remove_folders(path_name=cfg["matriz_hd_nfceresp"])
nfce_matriz_resp.path_google_drive(file_path=cfg["matriz_filePath_nfceresp"], google_path=cfg["matriz_fileUpload_nfceresp"])
nfce_matriz_resp.file_upload(id_folder=cfg["matriz_link_drive_nfceresp"])
    #NFCEPROC
nfce_matriz_proc = arius_backup(company_name=cfg["matriz_nome_nfceproc"])
nfce_matriz_proc.months()
nfce_matriz_proc.copy_nfce(server=cfg["matriz_servidor_nfceproc"],hd=cfg["matriz_hd_nfceproc"])
nfce_matriz_proc.compress(path_name=cfg["matriz_hd_nfceproc"])
nfce_matriz_proc.remove_folders(path_name=cfg["matriz_hd_nfceproc"])
nfce_matriz_proc.path_google_drive(file_path=cfg["matriz_filePath_nfceproc"], google_path=cfg["matriz_fileUpload_nfceproc"])
nfce_matriz_proc.file_upload(id_folder=cfg["matriz_link_drive_nfceproc"])

#KW
retaguarda = arius_backup(company_name=cfg["retaguarda_nome"])
retaguarda.months()
retaguarda.copy_kw_erp(path_f=cfg["retaguarda_server_local"], path_dst=cfg["retaguarda_hd_local"])

#RETAGUARDA
kw = arius_backup(company_name=cfg["kw_nome"])
kw.months()
kw.copy_kw_erp(path_f=cfg["kw_server_local"], path_dst=cfg["kw_hd_local"])

#
#build
#pyinstaller --icon=C:\backup_nfce\icon\arius-logo-grande.ico C:\backup_nfce\src\backup-nfce-v4.0-2023.py
#gerar requirements >> pip freeze > requirements.txt