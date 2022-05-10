# Author: Leandro de Jesus
# Candeias-BA Brasil - 2022                               
#</First Project...>

#Load modules
from datetime import date, timedelta
import shutil
import time
import pyautogui
import pymsgbox
import yaml
from tkinter import *
import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import FileNotUploadedError
 

class backup:
    def __init__(self, company_name):            
        self.company_name = company_name          #set name for company                
            
    def copy_nfe(self, server, hd): #check file kw and erp if exist move to Hard disk                
        self.last_day = str(input('Digite a data no formato >> AAA-MM-DD <<: '))        
        for root, subFolder, filename in os.walk(server):
            for folder in subFolder:                
                if self.last_day in folder:
                    self.server_file = os.path.join(root, folder)
                    self.hd_file = os.path.join(hd, self.month,folder)                
                    try:                                                                                                 
                        print(f'{self.company_name}Copiando arquivos.')
                        shutil.copytree(self.server_file, self.hd_file)                    
                        print(f'{self.company_name}Arquivos copiados para HD.')                                               
                        pass                                       
                    except PermissionError as e:
                        print(f'{self.company_name}Sem permissao para acessar o arquivo!\n\n')
                    except FileExistsError as e:
                        print(f'{self.company_name}Você ja fez backup deste arquivo!\n\n')
                    except FileNotFoundError as e:
                        print(f'{self.company_name}Arquivo não encontrado. \n\n')
                    except shutil.SameFileError as e:
                        pass                      

    def compress(self, path_name):#compress folders in format .zip to upload Google Drive
        for root, subFolder, filename in os.walk(path_name): #walking on files
            for folder in subFolder:
                if self.last_day in folder: #last_day is file backup with date yerterday YY-MM-DD
                    name_archive = os.path.join(root, folder)                                     
                    extension = 'zip' #I'll compress in zip        
                    local = name_archive                    
                    try:                                                
                        print(f'{self.company_name}Compactando arquivos.')
                        shutil.make_archive(name_archive, extension, local)   
                        print(f'{self.company_name}Arquivos compactados!')
                    except FileExistsError as e:
                        print(f'{self.company_name}ESTE ARQUIVO JÁ FOI COMPACTADO!\n\n')
                    except FileNotFoundError as e:
                        pass      
                                  
    def remove_folders(self, path_name):
            for root, subFolder, filename in os.walk(path_name):
                for folder in subFolder:                
                    if self.last_day in folder:
                        try:
                            print(f'{self.company_name}Removendo pasta sem compactação.')
                            shutil.rmtree(self.hd_file)
                            print(f'{self.company_name}Pastas removidas.')
                        except:
                            pass
                        
    def copy_kw_erp(self, path_f, path_dst): #checkfile kw and erp if exist move to Hard disk
        date_today = str(input('Digite a data no formato >> DD-MM-DD <<: '))

        for root, dirs, files in os.walk(path_f):
            for file in files:                
                if date_today in file:        
                    server = os.path.join(root, file)
                    hd = os.path.join(path_dst, self.month, file)                                                                                                                           
                    try:                                                                                                                      
                        print(f'{self.company_name}Copiando arquivos.\n')
                        shutil.copyfile(server, hd)
                        print(f'{self.company_name}Copiado com sucesso !\n\n')
                    except FileExistsError as e:
                        print(f'{self.company_name}O arquivo ja foi copiado\n\n')
                    except FileNotFoundError as e:
                        pass
                    except SameFileError as e:
                        print(f'{self.company_name}O arquivo ja foi copiado\n\n')
                else:
                    pass
                                                        
    def months(self): #Create a folder with current month
        months = { 1:'JANEIRO', 2:'FEVEREIRO', 3:'MARCO', 4:'ABRIL', 
                    5:'MAIO', 6:'JUNHO', 7:'JULHO', 8:'AGOSTO', 
                    9:'SETEMBRO', 10:'OUTUBRO', 11:'NOVEMBRO', 12:'DEZEMBRO'}
        
        self.month_today = date.today().strftime("%m")
        self.month_today = int(self.month_today)
        self.date_now = date.today().strftime('%d')                
        if self.date_now == '1':
            self.month_today = self.month_today - 1            
        else:
            pass
        self.month = months.get(self.month_today)            

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
                        self.path_drive = os.path.join(google_path, self.month, file)                                  
                    except FileNotFoundError as e:
                        pass
                    except PermissionError as e:
                        pass
                        
    def file_upload(self, id_folder):        
        credentials = backup.google_auth(self)
        archivo = credentials.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                        "id": id_folder}]})
        try:
            archivo['title'] = self.path_drive.split("\\")[-1]
            archivo.SetContentFile(self.path_drive)
            print(f'{self.company_name}Enviando para google drive')
            archivo.Upload()
            print(f'{self.company_name}Enviado com sucesso!\n\n')
        except AttributeError as e:
            pass
        except FileNotFoundError as e:
            pass

    def stop(self): #stop if execution is manual        
        player_input = str(input('BACKUP CONCLUIDO | >> Presione <enter> << para encerrar...'))
        if player_input != 0:
            sys.exit()
                                                  
#Atacado
with open('C:\\Users\\Administrador\\Documents\\backup_nfce\\src\\configurar_backup.yml','r') as yFile:
    cfg = yaml.safe_load(yFile)        
  
nfe_filial = backup(company_name=cfg["filial_nome"])
nfe_filial.months()
nfe_filial.copy_nfe(server=cfg["filial_server_local"],hd=cfg["filial_hd_local"])
nfe_filial.compress(path_name=cfg["filial_compact"])
nfe_filial.remove_folders(path_name=cfg["filial_compact"])
nfe_filial.path_google_drive(file_path=cfg["filial_filePath"], google_path=cfg["filial_googlePath"])
nfe_filial.file_upload(id_folder=cfg["filial_link_drive"])

#Varejao
nfe_varejao = backup(company_name=cfg["varejao_nome"])
nfe_varejao.months()
nfe_varejao.copy_nfe(server=cfg["varejao_server_local"],hd=cfg["varejao_hd_local"])
nfe_varejao.compress(path_name=cfg["varejao_compact"])
nfe_varejao.remove_folders(path_name=cfg["varejao_compact"])
nfe_varejao.path_google_drive(file_path=cfg["varejao_filePath"], google_path=cfg["varejao_googlePath"])
nfe_varejao.file_upload(id_folder=cfg["varejao_link_drive"])

#Loja
nfe_matriz = backup(company_name=cfg["matriz_nome"])
nfe_matriz.months()
nfe_matriz.copy_nfe(server=cfg["matriz_server_local"],hd=cfg["matriz_hd_local"])
nfe_matriz.compress(path_name=cfg["matriz_compact"])
nfe_matriz.remove_folders(path_name=cfg["matriz_compact"])
nfe_matriz.path_google_drive(file_path=cfg["matriz_filePath"], google_path=cfg["matriz_googlePath"])
nfe_matriz.file_upload(id_folder=cfg["matriz_link_drive"]) #JANEIRO Empresa 1

#KW
retaguarda = backup(company_name=cfg["retaguarda_nome"])
retaguarda.months()
retaguarda.copy_kw_erp(path_f=cfg["retaguarda_server_local"], path_dst=cfg["retaguarda_hd_local"])

#RETAGUARDA

kw = backup(company_name=cfg["kw_nome"])
kw.months()
kw.copy_kw_erp(path_f=cfg["kw_server_local"], path_dst=cfg["kw_hd_local"])

#PARAR EXECUÇAO
stop = backup('STOP: ')
stop.stop()

#pyinstaller --icon=C:\Users\FABIO-ESCRITORIO\AppData\Local\backup-nfe\icon\img-256x256.ico src\bkp_predefinido.py