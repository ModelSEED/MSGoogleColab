import os
from os.path import exists
from google.colab import drive
import shutil
import tarfile

class MSColabUtils:
    def __init__(self):
      drive.mount('/content/drive')
      self.SetupColabHome()
      self.SetupEnv()
      self.LinkColabHome(True)

    def SetupEnv(self,overwrite=False):
      if exists('/Environment') and overwrite:
        shutil.rmtree('/Environment')
      if not exists('/Environment'):
        with tarfile.open("/content/drive/MyDrive/MyMSColab/MSGoogleColab/Env.tgz", 'r:gz') as tar:
          tar.extractall(path="/")

    def SetupData(self,overwrite=False):
      if exists('/Data') and overwrite:
        shutil.rmtree('/Data')
      if not exists('/Data'):
        with tarfile.open("/content/drive/MyDrive/MyMSColab/MSGoogleColab/data.tgz", 'r:gz') as tar:
          tar.extractall(path="/")
    
    def SetToken(self,token):
      self.SetupColabHome()
      self.LinkColabHome()
      with open("/root/.kbase/token", 'w') as file:
        file.write(token)

    def SetupColabHome(self,overwrite=False):
      if exists('/content/drive/MyDrive/MyMSColab') and overwrite:
        shutil.rmtree('/content/drive/MyDrive/MyMSColab')
      if not exists('/content/drive/MyDrive/MyMSColab'):
        os.makedirs('/content/drive/MyDrive/MyMSColab')
      if not exists('/content/drive/MyDrive/MyMSColab/MSGoogleColab'):
        os.system("cd /content/drive/MyDrive/MyMSColab;git clone https://github.com/ModelSEED/MSGoogleColab.git")
      if not exists('/content/drive/MyDrive/MyMSColab/config'):
        shutil.copyfile('/content/drive/MyDrive/MyMSColab/MSGoogleColab/defaultconfig','/content/drive/MyDrive/MyMSColab/config')
    
    def LinkColabHome(self,overwrite=False):
      if exists("/root/.kbase") and overwrite:
        shutil.rmtree("/root/.kbase")
      if not exists("/root/.kbase"):
        os.symlink("/content/drive/MyDrive/MyMSColab","/root/.kbase")

    def LinkNotebookDirectory(self,notebook_dir,name):
      if not exists("/content/"+name):
        os.symlink(notebook_dir,"/content/"+name)

    def UpdateSourceEnvironment(self):
      if exists('/Environment'):
         with tarfile.open("/content/drive/MyDrive/MyMSColab/MSGoogleColab/Env.tgz", "w:gz") as tar:
            tar.add('/Environment', arcname=os.path.basename('/Environment'))

gc_util = MSColabUtils()