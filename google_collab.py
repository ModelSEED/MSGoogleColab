import os
from os.path import exists
import shutil
import tarfile

class MSColabUtils:
    def __init__(self):
      self.DownloadSetupEnv()
      self.SetupColabHome()
      self.LinkColabHome()

    def DownloadSetupEnv(self,overwrite=False):
      if exists('/Environment') and overwrite:
        shutil.rmtree('/Environment')
      if not exists('/Environment'):
        with tarfile.open("/content/drive/MyDrive/ModelSEEDpy-Collab/Env.tgz", 'r:gz') as tar:
          tar.extractall(path="/")
    
    def SetToken(self,token):
      self.SetupColabHome()
      self.LinkColabHome()
      with open("/root/.kbase/token", 'w') as file:
        file.write(token)

    def SetupColabHome(self,overwrite=False):
      if exists('/content/drive/MyDrive/MyMSCollab') and overwrite:
        shutil.rmtree('/content/drive/MyDrive/MyMSCollab')
      if not exists('/content/drive/MyDrive/MyMSCollab'):
        os.makedirs('/content/drive/MyDrive/MyMSCollab')
      if not exists('/content/drive/MyDrive/MyMSCollab/config'):
        shutil.copyfile('/content/drive/MyDrive/ModelSEEDpy-Collab/defaultconfig','/content/drive/MyDrive/MyMSCollab/config')
    
    def LinkColabHome(self,overwrite=False):
      if exists("/root/.kbase") and overwrite:
        shutil.rmtree("/root/.kbase")
      if not exists("/root/.kbase"):
        os.symlink("/content/drive/MyDrive/MyMSCollab","/root/.kbase")

    def LinkNotebookDirectory(self,notebook_dir,name):
      if not exists("/content/"+name):
        os.symlink(notebook_dir,"/content/"+name)

    def UpdateSourceEnvironment(self):
      if exists('/Environment'):
         with tarfile.open("/content/drive/MyDrive/ModelSEEDpy-Collab/NewEnv.tgz", "w:gz") as tar:
            tar.add('/Environment', arcname=os.path.basename('/Environment'))

gc_util = MSColabUtils()