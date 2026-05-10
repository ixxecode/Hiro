# | [ Dia 7 ]
# | ~/manager/desktop.py
# | Gestiona la creacion del desktop

from pathlib import Path
import os


class DesktopManager:
    """
    Encargado de toda la lógica relacionada con el archivo .desktop.

    No interactúa con el usuario.
    Solo trabaja con archivos y datos.
    """

    def __init__(
        self,
        path_file,
        desktop_name=None,
        comment="Sin comentario",
        terminal=False,
        category="Utility",
    ):
        """
        Inicializa el manager con la información del archivo y configuración del desktop.
        """

        self.path_file = Path(path_file)

        # Directorio estándar de aplicaciones en Linux
        self.desktop_dir = Path.home() / ".local" / "share" / "applications"
        self.desktop_dir.mkdir(parents=True, exist_ok=True)

        # Nombre final del .desktop
        self.final_name = desktop_name or self.path_file.stem

        self.comment = comment
        self.terminal = terminal
        self.category = category

        # Ruta final del archivo .desktop
        self.desktop_path = self.desktop_dir / f"{self.final_name}.desktop"

    def exists_file(self):
        """
        Verifica si el archivo original existe.
        """
        return self.path_file.exists() and self.path_file.is_file()

    def exists_desktop(self):
        """
        Verifica si ya existe un .desktop previamente creado.
        """
        return self.desktop_path.exists()

    def is_executable(self):
        """
        Verifica si el archivo tiene permisos de ejecución.
        """
        return os.access(self.path_file, os.X_OK)

    def grant_file_permissions(self):
        """
        Otorga permisos de ejecución al archivo original.
        """
        os.chmod(self.path_file, 0o755)

    def _create_exec(self):
        """
        Genera el comando de ejecución según el tipo de archivo.
        """

        suffix = self.path_file.suffix

        if suffix == ".py":
            return f'python3 "{self.path_file}"'
        elif suffix == ".sh":
            return f'bash "{self.path_file}"'
        else:
            return f'"{self.path_file}"'

    def preview(self):
        """
        Devuelve el contenido del .desktop sin guardarlo,
        útil para mostrar al usuario antes de crear el archivo.
        """

        return f"""[Desktop Entry]
Name={self.final_name}
Comment={self.comment}
Exec={self._create_exec()}
Path={self.path_file.parent}
Terminal={str(self.terminal).lower()}
Type=Application
Categories={self.category};
"""

    def create_desktop(self):
        """
        Crea el archivo .desktop en el sistema.
        """

        self.desktop_path.write_text(self.preview())
        os.chmod(self.desktop_path, 0o755)