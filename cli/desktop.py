# | [ Dia 6 ]
# | ~/cli/desktop.py
# | Gestiona la interfaz CLI de la herramienta

from manager.desktop import DesktopManager


class CliDesktop():
    def __init__(self):
        self.manager = None

    # Metodo que solicita los datos necesarios al usuario
    def ask_data(self):
        path_file = input(
            "[hiro] Ruta del archivo: "
        ).strip()

        desktop_name = input(
            "[hiro] Nombre del desktop (opcional): "
        ).strip()

        comment = input(
            "[hiro] Comentario del desktop (opcional): "
        ).strip()

        category = input(
            "[hiro] Categoria (Utility/Game/Development/etc): "
        ).strip()

        terminal_choice = input(
            "[hiro] Ejecutar en terminal? (s/n): "
        ).strip().lower()

        # Si el usuario no escribe nada se usa None
        if not desktop_name:
            desktop_name = None

        # Comentario predeterminado
        if not comment:
            comment = "Sin comentario"

        # Categoria predeterminada
        if not category:
            category = "Utility"

        # Configuracion de terminal
        if terminal_choice == "s":
            terminal = True
        else:
            terminal = False

        # Crear manager con los datos del usuario
        self.manager = DesktopManager(
            path_file=path_file,
            new_name_desktop=desktop_name,
            comment=comment,
            terminal=terminal,
            category=category
        )

    # Metodo que reacciona a lo que exists_desktop devuelve
    def notify_existence(self, existed_before: bool):
        if existed_before:
            print(
                f"[hiro] El desktop ya existia en: "
                f"'{self.manager.desktop_path}' sera modificado..."
            )

            print("[hiro] El desktop fue modificado.")

        else:
            print(
                f"[hiro] El desktop fue creado en: "
                f"'{self.manager.desktop_dir}'."
            )

    # Metodo que verifica si el archivo existe
    def check_file(self):
        if not self.manager.exists_file():
            print("[hiro] Error: el archivo no existe.")
            return False

        return True

    # Metodo que verifica permisos del archivo seleccionado
    def check_executable(self):
        if not self.manager.is_executable():
            print("[hiro] El archivo no es ejecutable...")

            choice = input(
                "[hiro] Dar permisos para que sea ejecutable? (s/n): "
            ).strip().lower()

            if choice == "s":
                try:
                    self.manager.grant_file_permissions()

                    print("[hiro] Permisos otorgados.")
                    return True

                except PermissionError:
                    print(
                        "[hiro] Error: no tienes permisos suficientes."
                    )

                    return False

                except FileNotFoundError:
                    print(
                        "[hiro] Error: el archivo ya no existe."
                    )

                    return False

            else:
                print("[hiro] Cancelando creación del desktop.")
                return False

        print("[hiro] Archivo seleccionado...")
        return True

    # Metodo principal de creacion
    def create(self):
        # Solicitar datos al usuario
        self.ask_data()

        # Verificar existencia del archivo
        if not self.check_file():
            return

        # Verificar permisos del archivo
        if not self.check_executable():
            return

        # Guardar estado de existencia antes de crear
        existed_before = self.manager.exists_desktop()

        try:
            # Crear desktop
            self.manager.create_desktop()

        except PermissionError:
            print(
                "[hiro] Error: no tienes permisos para crear el desktop."
            )

            return

        # Informar resultado al usuario
        self.notify_existence(existed_before)