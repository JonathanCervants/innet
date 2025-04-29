
from pathlib import Path
class SoftwareInst:
    def __init__(self):
     self.download_dir = Path("")
     self.create_directory = Path("")
     #Conf to install
     self.programs = {
        "Google Chrome": {
                "url": "https://dl.google.com/chrome/install/standalonesetup.exe",
                "install_cmd": ["/silent", "/install"],
                "filename": "chrome_installer.exe",
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

    def is_installed(self, checks:):
        for check in checks:
            if checks["type"] == "registry":
               try:
                  reg.OpenKey()
                  return True
               except WindowsError:
                  pass
            elif check["type"] == "file":
               if 