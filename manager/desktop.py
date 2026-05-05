# | [ Dia 5 ]
# | ~/manager/desktop.py
# | Gestiona la creacion del desktop

from pathlib import Path
import os


class DesktopManager():
    def __init__(self, path_file, new_name_desktop=None):
        self.path_file = Path(path_file)

        self.desktop_dir = Path.home() / ".local" / "share" / "applications"

        self.desktop_name = new_name_desktop

        # Nombre final que tendra el desktop
        if not self.desktop_name:
            self.final_name = self.path_file.stem
        else:
            self.final_name = self.desktop_name

        # Ruta final del archivo .desktop
        self.desktop_path = self.desktop_dir / f"{self.final_name}.desktop"


    # | [Interno] Metodo que crea el contenido del desktop
    def _create_text(self):
        parent = self.path_file.parent
        suffix = self.path_file.suffix

        # Construir comando de ejecución
        if suffix == ".py":
            exec_cmd = f'python3 "{self.path_file}"'

        elif suffix == ".sh":
            exec_cmd = f'bash "{self.path_file}"'

        else:
            exec_cmd = f'"{self.path_file}"'

        # Contenido del .desktop
        text = f"""[Desktop Entry]
Name={self.final_name}
Comment=Archivo de prueba
Exec={exec_cmd}
Path={parent}
Terminal=false
Type=Application
"""

        return text

    # Metodo que verifica si el archivo existe o no
    def exists_file(self):
        return self.path_file.exists() and self.path_file.is_file()

    # Metodo que verifica si el desktop existe o no
    def exists_desktop(self):
        return self.desktop_path.exists()

    # Metodo que verifica si el archivo seleccionado es ejecutable o no
    def is_executable(self):
        return os.access(self.path_file, os.X_OK)

    # Metodo que otorga permisos de ejecucion al archivo seleccionado
    def grant_file_permissions(self):
        os.chmod(self.path_file, 0o755)

    # Metodo que crea el desktop
    def create_desktop(self):
        text = self._create_text()

        # Crear desktop
        self.desktop_path.write_text(text)

        # Dar permisos de ejecucion al desktop
        os.chmod(self.desktop_path, 0o755)