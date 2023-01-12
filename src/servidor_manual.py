from datetime import date, timedelta, datetime
import shutil
import yaml
import os
from py7zr import pack_7zarchive

# Load google modules for Authentication
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
 
date_today = str(input("DD-MM-AA: "))

class arius_backup: #arius_backup
    def __init__(self, company_name):                    
        self.company_name = company_name          #set name for company        
                                    
    def copy_kw_erp(self, path_f, path_dst): #checkfile kw and erp if exist move to Hard disk        

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
                                                        
    def months(self): #Create a folder with current month
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

    

with open('C:\\arius_backup_nfce\\windows\\config\\arius_path.yml','r') as config:
    cfg = yaml.safe_load(config)

#KW
retaguarda = arius_backup(company_name=cfg["retaguarda_nome"])
retaguarda.months()
retaguarda.copy_kw_erp(path_f=cfg["retaguarda_server_local"], path_dst=cfg["retaguarda_hd_local"])

#RETAGUARDA
kw = arius_backup(company_name=cfg["kw_nome"])
kw.months()
kw.copy_kw_erp(path_f=cfg["kw_server_local"], path_dst=cfg["kw_hd_local"])

#pyinstaller --icon=C:\backup_nfce\icon\arius-logo-grande.ico C:\backup_nfce\src\servidor_manual.py
# gerar requirements >> pip freeze > requirements.txt
