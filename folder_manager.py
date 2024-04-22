# bazi dosya uzantilari bilinmiyor olabilir ? 
# OK --- bu klasor organize mi ? 
# bu klasorde bilinmeyen dosya uzantilari va mi ?
# dosyalari organize et
# hangi klasordeyiz ? 


class FolderOrganize:
    """
    FolderOrganize Class Yapisi Bir Folderda Asagidaki islemleri yapar..
    """
    import os
    
    IGNORED_FILE_TYPES = ['py', 'exe', 'app', 'sqlite3']

    FILE_TYPES = {
        "xls": "Sheets",
        "xlsx": "Sheets",
        "doc": "Documents",
        "docx": "Documents",
        "txt": "Documents",
        "pdf": "Documents",
        "jpg": "Pictures",
        "mp3": "Musics",
    }

    # initial??
    def __init__(self, folder_path):
        # bulundugumuz klasor??
        self.folder_path = folder_path
        
        if not self.is_folder_path_correct():
            raise ValueError("Klasor Bilgisi Dogru Degildir..")

    def is_folder_path_correct(self):
        return self.os.path.isdir(self.folder_path)
    
    def is_folder_organize(self):
        """
        is_folder_organize check islemi folder bilgisinin organize olup olmadigini kontrol eder
        """
        file_types = self.get_file_types()
        
        for item in file_types:
            if not item in self.IGNORED_FILE_TYPES:
                return False
        return True
    
    def get_files(self):
        return [
            item for item in self.os.listdir(self.folder_path) 
            if not item.startswith('.') and 
                self.os.path.isfile(item) and 
                len(item.split('.')) == 2
        ]
    
    def get_organizable_files(self):
        files = self.get_files()
        return [
            file for file in files
            if not file.split('.')[1] in self.IGNORED_FILE_TYPES
        ]
    
    def get_file_types(self):
        files = self.get_files()
        file_types = set() 
        for file in files:
            try:
                file_types.add(file.split('.')[1])
            except:
                pass
        return list(file_types)
    
    def has_folder_unknown_file_types(self):
        file_types = self.get_file_types()
        for file_type in file_types:
            if not file_types in list(self.FILE_TYPES.keys()):
                return True
        return False
    
    def create_folder(self):
        file_types = self.get_file_types()
        for file_type in file_types:
            folder_name = self.FILE_TYPES.get(file_type, 'Unknown')
            if not self.os.path.isdir(folder_name):
                self.os.mkdir(folder_name)

    def organize(self):
        import shutil
        files = self.get_organizable_files()
        self.create_folder()
        
        for file in files:
            file_type = file.split('.')[1]
            folder_name = self.FILE_TYPES.get(file_type, 'Unknown')
            shutil.move(file, f"{folder_name}/{file}")
        