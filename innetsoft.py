import time
import subprocess
import requests
import winreg as reg
from typing import Dict, Any
import sys
from pathlib import Path

class SoftwareInstaller:
    def __init__(self):
     self.download_dir = Path("C:/temp")
     self.create_directory = Path("C:/temp")
     #Conf to install
     self.programs = {
          "7-Zip": {
                "url": "https://www.7-zip.org/a/7z2400-x64.exe",
                "install_cmd": ["/S"],
                "filename": "7zip_installer.exe",
                "checks": [
                    {"type": "file", "path": r"C:\Program Files\7-Zip\7z.exe"}
                ]
            },
         "Google Chrome": {
                "url": "https://dl.google.com/chrome/install/standalonesetup.exe",
                "install_cmd": ["/silent", "/install"],
                "filename": "standalonesetup.exe",
                "checks": [
                    {"type": "registry", "path": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Google Chrome"}
                ]
            },
     }

    def create_directory(self, path: Path):
       #create if not exists
        try:
          path.mkdir(parents=True, exist_ok = True)
        except OSError as e:
           print("error")
           sys.exit(1)
    
    def create_directory(self, path: Path):
       #create if not exists
        try:
          path.mkdir(parents=True, exist_ok = True)
        except OSError as e:
           print("error")
           sys.exit(1)

    def is_installed(self, checks):
        for check in checks:
            if check["type"] == "registry":
               try:
                  reg.OpenKey(reg.HKEY_LOCAL_MACHINE, check['path'])
                  return True
               except WindowsError:
                  pass
            elif check["type"] == "file":
               if Path(check['path']).exists():
                 return True
            return False

    def download_with_progress(self, filename,url) ->bool:
      #"Display descarga"
      try:
         local_path = self.download_dir / filename
         print(f"Downloading {filename}...")
         with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int
            downloaded = 0

            with open(local_path, 'wb') as f:
               for chunk in r.iter_content(chunk_size=8125):
                  f.write(chunk)
                  downloaded += len(chunk)
                  progress = (downloaded / total_size) * 100 if total_size > 0 else 0
                  print(f"Progress of download: {progress}")

         print("\nDownload completed")
         return True
      except Exception as e:
         print(f"Failed...: {e}")
         return False
      
    def install_program(self, installer_path: Path, install_cmd: list)-> bool:
      #Run with elevations
        try:
         print(f"Installing {installer_path.name}")
         #use powershell
         cmd = f'Start-Process -FilePath "{installer_path}" -ArgumentList "{ " ".join(install_cmd)}" -Wait'
         if sys.platform == "win32":
            cmd += ' -Verb RunAs'
        except subprocess.calledProcessError as e:
            print(f"Instalation failled: {e}")
            return False

   # def cleanup():
   #    "delete after install"
   #    try:
   #       (self.downalod_dir /filename)
   #       print(f"Delete installer")
   #    except OSError as e:
   #       print()
      
    def run(self) -> None:
      print(" ==Automated Software Installer")

      for program,details in self.programs.items():
         print(f"\nProcesing {program}")

         #Skip is installed
         if self.is_installed(details["checks"]):
            print(f"{program} is already installed. Skip..")
            continue
         
         installer_path = self.download_dir / details["filename"]
         #Doanloaded is needd?
         if not installer_path.exists():
            if not self.download_with_progress(details["url"],details["filename"]):
               continue
         #install
         if self.install_program(installer_path, details["install_cmd"]):
            #"Cleanup if"
            # self.cleanup
            time.sleep(3)

      print("\ninstalled proccess completed script")

if __name__ == "__main__":
   installer = SoftwareInstaller()
   installer.run()