import shutil

class compress:
    file = file
    data = file
    extension = 'zip'
    file2 = '/home/leandro/Downloads'

    def compress_folder(self):
        #shutil.make_archive(file, extension, file2,)
        shutil.make_archive(self.file, self.extension, self.file, './')