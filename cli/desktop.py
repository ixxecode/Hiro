# | [ Dia 7 ]
# | ~/cli/desktop.py
# | Gestiona la interfaz CLI de la herramienta

from manager.desktop import DesktopManager


class CliDesktop:
    """
    Maneja toda la interacción con el usuario en terminal.

    Su responsabilidad es:
    - Pedir datos
    - Validar flujo básico
    - Delegar lógica al DesktopManager
    """

    def ask_data(self):
        """
        Solicita al usuario los datos necesarios para crear el .desktop.
        """

        path_file = input("[hiro] Ruta del archivo: ").strip()
        desktop_name = input("[hiro] Nombre del desktop (opcional): ").strip()
        comment = input("[hiro] Comentario (opcional): ").strip()
        category = input("[hiro] Categoria: ").strip()
        terminal_choice = input("[hiro] Ejecutar en terminal? (s/n): ").strip().lower()

        return {
            "path_file": path_file,
            "desktop_name": desktop_name or None,
            "comment": comment or "Sin comentario",
            "category": category or "Utility",
            "terminal": terminal_choice == "s",
        }

    def show_preview(self, manager):
        """
        Muestra al usuario cómo quedará el archivo .desktop antes de crearlo.
        """
        print("\n[hiro] Preview del desktop:")
        print(manager.preview())

    def confirm(self):
        """
        Pide confirmación final antes de crear el archivo.
        """
        return input("\n[hiro] Confirmar creacion? (s/n): ").strip().lower() == "s"

    def run(self):
        """
        Flujo principal de la CLI:
        1. Obtener datos del usuario
        2. Validar archivo
        3. Manejar permisos si es necesario
        4. Mostrar preview
        5. Confirmar creación
        6. Crear .desktop
        """

        data = self.ask_data()
        manager = DesktopManager(**data)

        # Verificar que el archivo exista
        if not manager.exists_file():
            print("[hiro] Error: el archivo no existe.")
            return

        # Verificar permisos de ejecución
        if not manager.is_executable():
            choice = input("[hiro] No es ejecutable. Dar permisos? (s/n): ").strip().lower()

            if choice != "s":
                print("[hiro] Cancelado.")
                return

            manager.grant_file_permissions()

        # Mostrar cómo quedará el archivo
        self.show_preview(manager)

        # Confirmación final
        if not self.confirm():
            print("[hiro] Cancelado por el usuario.")
            return

        existed_before = manager.exists_desktop()

        # Crear el .desktop
        manager.create_desktop()

        # Feedback final
        if existed_before:
            print("[hiro] Desktop actualizado.")
        else:
            print("[hiro] Desktop creado.")