# | [ Dia 2 ]
# | ~/main.py
# | Primer archivo de hiro

from pathlib import Path
import sys
import os

class DesktopCreater():
    def __init__(self):
        # if que verifica si se tiene un archivo seleccionado o en caso de no tenerlo usa una ruta predeterminada
        if len(sys.argv) > 1:
            self.file_path = Path(sys.argv[1])
        else:
            self.file_path = Path(__file__).parent / "app.py"

        # Ruta directa al directorio applications donde se guardan los desktop
        self.desktop_dir = Path.home() / ".local" / "share" / "applications"

        # Ruta donde se dejara el archivo con el nombre del archivo
        self.desktop_file = self.desktop_dir / f"{self.file_path.stem}.desktop"
    
    # [Interno] Metodo que crea el contenido del desktop
    def _create_text(self):
        # Obtener partes del path
        parent = self.file_path.parent
        name = self.file_path.name

        # Construir comando de ejecución
        exec_cmd = f'bash -c "cd {parent} && ./{name}"'

        # Contenido del .desktop
        text = f"""[Desktop Entry]
Name={self.file_path.stem}
Comment=Archivo de prueba
Exec={exec_cmd}
Terminal=false
Type=Application
"""
        return text
    
    # [Interno] Metodo que verifica si el desktop existe o no (devuelve True o False)
    def _exists_desktop(self):
        return self.desktop_file.exists()
    
    # [Interno] Metodo que verifica si el archivo seleccionado es ejecutable o no (devuelve True o False)
    def _is_executable(self):
        file = self.file_path
        if file.exists() and file.is_file() and os.access(file, os.X_OK):
            return True
        return False
    
    # Metodo que reacciona a lo que _exists devuelva y actua en consecuencia informando al usuario
    def notify_existence(self, existed_before: bool):
        if existed_before:
            print(f"[hiro] El desktop ya existia en: '{self.desktop_file}' sera modificado...")
            print("[hiro] El desktop fue modificado.")
        else:
            print(f"[hiro] El desktop fue creado en: '{self.desktop_dir}'.")

    # Metodo que reacciona a lo que _is_executable devuelva y actua en consecuencia informando al usuario
    def check_executable(self):
        file = self._is_executable()

        if not file:
            print(f"[hiro] El archivo seleccionado no tenia permisos de ejecucion...")
            os.chmod(self.file_path, 0o755)
            print("[hiro] Se le dio permisos de ejecucion al archivo seleccionado.")
        else:
            print("[hiro] Archivo seleccionado...")

    # Metodo que crea el desktop
    def create(self):
        # Contenido general del desktop
        text = self._create_text()

        # Verificar si el archivo tiene permisos de ejecucion
        self.check_executable()

        # Verifica y notifica si el desktop existe o no y guarda el estado
        existed_before = self._exists_desktop()

        # Se crea el desktop con el text y se le da permisos de ejecucion 
        self.desktop_file.write_text(text)
        os.chmod(self.desktop_file, 0o755)

        # Verifica y notifica que el desktop fue creado o modificado segun el estado guardado
        self.notify_existence(existed_before)