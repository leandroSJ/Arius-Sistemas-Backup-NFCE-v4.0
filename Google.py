from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import FileNotUploadedError

dir_credentials = 'credentials.json'

# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = dir_credentials
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(dir_credentials)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(dir_credentials)
    credentials = GoogleDrive(gauth)
    return credentials

def create_file_txt(nombre_archivo,contenido,id_folder):
    credentials = login()
    archivo = credentials.CreateFile({'title': nombre_archivo,\
                                       'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo.SetContentString('O trabalho é macho!')
    archivo.Upload()

# SUBIR UN ARCHIVO A DRIVE
def subir_archivo(ruta_archivo,id_folder):
    credentials = login()
    archivo = credentials.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo['title'] = ruta_archivo.split("/")[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()

if __name__ == "__main__":
    #create_file_txt('teste.txt','O trabalho é macho','1h7TExwTm4j8zXhfQlTvSlcJIdJW95Sa9')
    subir_archivo('/home/leandro/Documentos/dev/python/CDF/NFCERESP/14800340000101/2021-05-01.zip', '1h7TExwTm4j8zXhfQlTvSlcJIdJW95Sa9')