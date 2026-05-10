# Hiro

Hiro es una herramienta CLI para Linux que permite generar archivos .desktop de forma automática a partir de ejecutables, scripts o binarios.

## Descripción

Hiro automatiza la creación de archivos .desktop válidos en sistemas Linux, evitando la escritura manual de su estructura.

## Características

### Hiro en su versión 1.0 soporta:

- `Scripts Python (.py)`
- `Scripts Bash (.sh)`
- `Ejecutables Linux (binarios y similares)`

### Incluye:

- Detección automática del tipo de ejecución
- Generación consistente de archivos .desktop
- Vista previa antes de crear el archivo
- Confirmación del usuario antes de escribir en disco
- Manejo controlado de permisos de ejecución
- Validación de existencia del archivo original
- Detección de .desktop existente (actualización o creación)
- Organización modular CLI / lógica
- Generación estándar compatible con Linux

## Instalación

Hiro incluye un instalador local mediante `install.sh`.

### Ejecutar instalación

```bash
chmod +x install.sh
./install.sh
```

La instalación crea el comando global:

```bash
hiro
```

usando:

```bash
~/.local/bin/
```

## Uso

```bash
hiro
```

El flujo es interactivo y guiado.

### Hiro solicitará:

```bash
[hiro] Ruta del archivo:
[hiro] Nombre del desktop (opcional):
[hiro] Comentario (opcional):
[hiro] Categoria:
[hiro] Ejecutar en terminal? (s/n):
```

Luego mostrará una vista previa del `.desktop` generado antes de continuar.

Finalmente pedirá confirmación antes de crear o actualizar el archivo.

## Resultado

Se genera un archivo .desktop en:

```bash
~/.local/share/applications/
```

### Estructura generada:
- Nombre automático o personalizado
- Comentario configurable
- Categorías compatibles con el estándar Linux (Categories=)
- Soporte para ejecución en terminal (Terminal=true/false)
- Detección automática del tipo de ejecución (Exec=)
- Working directory correcto (Path=)
- Tipo de aplicación (Type=Application)
- Validación previa de entrada
- Confirmación explícita antes de escritura

Además incluye firma interna:

```bash
[X-Hiro-Version=1.0]
```

Estructura del proyecto

```bash
Hiro/
├── main.py
├── install.sh
├── cli/
│ └── desktop.py
├── manager/
│ └── desktop.py
├── README.md
└── .gitignore
```

## Organización interna

### cli/

Encargado de la interacción con el usuario:

- Entrada de datos
- Confirmaciones
- Flujo de ejecución
- Presentación de información

### manager/

Encargado de la lógica del sistema:

- Generación del .desktop
- Validación de archivos
- Manejo de permisos
- Construcción del contenido final

## Estado del proyecto

### v1.0

Esta versión representa un estado estable del proyecto:

- Flujo de ejecución completo y controlado
- Separación clara entre interfaz y lógica
- Vista previa del resultado antes de escritura
- Confirmación explícita del usuario antes de cambios en el sistema
- Manejo consistente de errores comunes
- Generación estándar de archivos .desktop
- Compatibilidad con scripts y binarios Linux
- Instalación local sin requerir permisos root
- Arquitectura modular estable (CLI / Manager)
- Diferencias con versiones anteriores