# Hiro [v0.8]

Hiro es una herramienta CLI simple para generar archivos `.desktop` en Linux a partir de archivos ejecutables, scripts o binarios.

Pensado como una utilidad rápida y liviana para automatizar la creación de accesos directos sin depender de interfaces gráficas.

---

## Descripción

Hiro permite crear archivos `.desktop` funcionales de forma automática, evitando tener que escribir manualmente la estructura requerida por Linux.

Actualmente soporta:

* Scripts Python (`.py`)
* Scripts Bash (`.sh`)
* Ejecutables Linux (`.x86_64`, binarios y similares)

El proyecto está orientado a simplicidad, mantenimiento sencillo y crecimiento modular a futuro.

---

## Instalación

Hiro incluye un instalador local mediante `install.sh`.

### Ejecutar instalación

```bash id="o1vx6s"
chmod +x install.sh
./install.sh
```

La instalación crea el comando global:

```bash id="x8t4yn"
hiro
```

usando:

```bash id="w7n5qk"
~/.local/bin/
```

---

## Uso [Actual]

```bash id="n2m7fr"
hiro
```

La herramienta solicitará:

```bash id="y3v5dk"
[hiro] Ruta del archivo:
[hiro] Nombre del desktop (opcional):
[hiro] Comentario del desktop (opcional):
[hiro] Categoria (Utility/Game/Development/etc):
[hiro] Ejecutar en terminal? (s/n):
```

---

## Resultado

Se genera un archivo `.desktop` en:

```bash id="m5c8zw"
~/.local/share/applications/
```

### Con una estructura funcional:

* Nombre automático o personalizado
* Comentario personalizado
* Categorías compatibles con Linux (`Categories=`)
* Soporte para terminal (`Terminal=true/false`)
* Detección automática del tipo de ejecución
* Compatibilidad con ejecutables Linux
* Working directory correcto mediante `Path=`
* Tipo aplicación (`Type=Application`)
* Firma interna de Hiro mediante:

```ini id="d6u4rx"
X-Hiro-Version=0.8
```

---

## Estructura del proyecto

```bash id="j9k3tw"
Hiro/
├── main.py
├── install.sh
├── cli/
│   └── desktop.py
├── manager/
│   └── desktop.py
├── README.md
└── .gitignore
```

### Organización interna

* `cli/`

  * Gestiona interacción con el usuario
  * Inputs
  * Confirmaciones
  * Mensajes en consola

* `manager/`

  * Gestiona la lógica principal
  * Creación del `.desktop`
  * Validaciones
  * Permisos
  * Generación del contenido

---

## Estado del proyecto

### v0.8

* Instalador local mediante `install.sh`

* Comando global `hiro`

* Integración con `~/.local/bin`

* Soporte para categorías (`Categories=`)

* Soporte para ejecución en terminal (`Terminal=true/false`)

* Personalización de comentarios (`Comment=`)

* Firma interna mediante `X-Hiro-Version`

* Mejora de compatibilidad con launchers Linux

* Generación de `.desktop` más estándar y mantenible

* Uso correcto de:

  * `Exec=`
  * `Path=`
  * `Categories=`
  * `Terminal=`
  * `Type=Application`

* Compatibilidad con:

  * `.py`
  * `.sh`
  * binarios Linux

* Validación de existencia del archivo

* Validación de permisos de ejecución

* Confirmación antes de aplicar `chmod`

* Manejo básico de errores controlados

* Detección de creación o modificación del `.desktop`

* Arquitectura modular CLI/Manager

* Logging simple en consola

---

## Notas

* Hiro no asigna permisos automáticamente sin intervención del usuario.
* Si el archivo no existe, el proceso se cancela de forma segura.
* Si el archivo no es ejecutable, Hiro solicita confirmación antes de otorgar permisos.
* Hiro agrega una firma interna (`X-Hiro-Version`) para identificar launchers generados por la herramienta.
* El instalador utiliza `~/.local/bin` para evitar permisos root.
* El proyecto está pensado exclusivamente para Linux y entornos compatibles con `.desktop`.