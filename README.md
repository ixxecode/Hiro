# Hiro [v0.7]

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

## Uso [Actual]

```bash
python main.py
```

La herramienta solicitará:

```bash
[hiro] Ruta del archivo:
[hiro] Nombre del desktop (opcional):
[hiro] Comentario del desktop (opcional):
[hiro] Categoria (Utility/Game/Development/etc):
[hiro] Ejecutar en terminal? (s/n):
```

---

## Resultado

Se genera un archivo `.desktop` en:

```bash
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

```ini
X-Hiro-Version=0.7
```

---

## Estructura del proyecto

```bash
Hiro/
├── main.py
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

### v0.7

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
* El proyecto está pensado exclusivamente para Linux y entornos compatibles con `.desktop`.