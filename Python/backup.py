import shutil
import os

def backup_files(source,destination):
    today = datetime.data.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)

source="/Users/Prabuddha/Documents/devops/python/backup.py"
destination="/Users/Prabuddha/Documents/devops/python"

backup_files(source,destination)