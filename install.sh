#!/bin/bash

# | [ Hiro Installer ]
# | Instala Hiro como comando global local

echo "[hiro] Iniciando instalacion..."

# Obtener ruta absoluta del proyecto
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Crear carpeta local bin si no existe
mkdir -p "$HOME/.local/bin"

# Ruta final del launcher
HIRO_LAUNCHER="$HOME/.local/bin/hiro"

# Crear launcher
cat > "$HIRO_LAUNCHER" << EOF
#!/bin/bash
python3 "$PROJECT_DIR/main.py" "\$@"
EOF

# Dar permisos de ejecucion
chmod +x "$HIRO_LAUNCHER"

echo "[hiro] Launcher instalado en:"
echo "[hiro] $HIRO_LAUNCHER"

# Verificar si ~/.local/bin existe en PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo
    echo "[hiro] ~/.local/bin no esta en tu PATH."
    echo "[hiro] Agrega esta linea a tu ~/.bashrc o ~/.zshrc:"
    echo
    echo 'export PATH="$HOME/.local/bin:$PATH"'
    echo
    echo "[hiro] Luego reinicia la terminal."
else
    echo
    echo "[hiro] Instalacion completada correctamente."
    echo "[hiro] Ya puedes usar el comando: hiro"
fi