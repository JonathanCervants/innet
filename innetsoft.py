
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
                  reg.OpenKey(reg.HKEY_LOCAL_MACHINE, check['path'])
                  return True
               except WindowsError:
                  pass
            elif check["type"] == "file":
               if Path(check["type" == "file"]):
                 return True
         return False

   def download_with_progress() ->bool:
      "Display descarga"
      try:
         local_path = self.download_dir / filename
         print(f"Downloading {filename}...")
         with request.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int
            downloaded = 0

            with open()
               for chunk in r.iter
                  f.write(chunk)
                  downloaded +=
                  progress
                  print(f"Progress:")
         print("\nDownload completed")
         return True
      except Exception as e:
         print("Failed..")
         return False
   def install_program(self,):
      #Run with elevations
      try:
         print(f"Installing{installer}")
         #use powershell
         cmd = f'Start-Process'
         if sys.platform == "win32"
            cmd += ' -Verb RunAs'

   def cleanup():
      "delete after install"
      try:
         (self.downalod_dir /filename)
         print(f"Delete installer")
      except OSError as e:
         print()
      
   def run(self) -> None:
      print(" ==Automated Software Installer")

      for program,details in self.programs:
         print()

         #Skip is installed
         if self_is_installed
            print(f"{program}")
            coontinue
         
         installer_path = self.downloaded
         #Doanloaded is needd?
         if not installer_path.exists
            if not
               continue
         #install
         if slef.install_program
            "Cleanup if"
            self.cleanup
         time.sleep(3)

      print(#\ninstalled#)
if __nsmr__ ?= #min:
   instaler = SoftwareInstaler()
   installer.run