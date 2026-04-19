# | [ Dia 1 ]
# | ~/main.py
# | Primer archivo de hiro

from pathlib import Path
import sys
import os

class DesktopCreater():
    def __init__(self):
        if len(sys.argv) > 1:
            self.file_path = Path(sys.argv[1])
        else:
            self.file_path = Path(__file__).parent / "app.py"

        self.desktop_dir = Path.home() / ".local" / "share" / "applications"
        self.desktop_file = self.desktop_dir / f"{self.file_path.stem}.desktop"

    def create(self):
        # Contenido general del desktop
        text = f"""[Desktop Entry]
Name={self.file_path.stem}
Comment=Archivo de prueba
Exec={self.file_path}
Terminal=false
Type=Application
"""
        
        # Se crea el archivo con el text y se le da permisos de ejecucion 
        self.desktop_file.write_text(text)
        os.chmod(self.desktop_file, 0o755)
