from datetime import datetime, date, timedelta, time
import shutil
import os

class essentials:
    def __init__(self):
        self.date_today = date.today().strftime("%d-%m-%y")
        self.last_day = str(date.today() - timedelta(days=1))

        #self.server = server
        #self.hd = hd

    def find_copy_nfe(self, server, hd): #this module check files nfe in internal network
        for root, subFolder, filename in os.walk(server):
            for folder in subFolder:
                if self.last_day in folder: #last_day is file with date yerterday
                    server = os.path.join(root, folder)
                    hd = os.path.join(hd, self.month, folder)               
                    try:
                        print('Load Files...')
                      #  shutil.copytree(server, hd)                        
                    except FileNotFoundError as e:
                        print('File Not Found!\n')
                    except PermissionError as e:
                        print('Permission Error!\n')
                    except FileExistsError as e:
                        print('Nao existe')
    
    def compress(self, name, extension, file, local, msg_compress):#compress folders to upload to Google Drive
        name = name
        extension = extension #I'll compress in zip
        file = file
        local = local
        #shutil.make_archive(file, extension, file2,)
        msg_compress = msg_compress
        print(f'{msg_compress}\n')
        shutil.make_archive(name, extension, file, local)

    def months(self):
        months = { 1:'JANEIRO', 2:'FEVEREIRO', 3:'MARCO', 4:'ABRIL', 
                    5:'MAIO', 6:'JUNHO', 7:'JULHO', 8:'AGOSTO', 
                    9:'SETEMBRO', 10:'OUTUBRO', 11:'NOVEMBRO', 12:'DEZEMBRO'}
        
        self.month_today = date.today().strftime("%-m")
        self.month_today = int(self.month_today)
        self.date_now = date.today().strftime('%d')        
        
        if self.date_now == '01':
            self.month_today = self.month_today - 1            
        else:          
            pass               

        self.month = months.get(self.month_today)
                        
loja = essentials()
loja.months()
loja.find_copy_nfe('/home/leandro/Documentos/dev/python/CDF/NFCERESP/14800340000101', '/home/leandro/Documentos/dev/python/CDF/BACKUP NFCE GESTAO LOJA01/NFCE2021/')