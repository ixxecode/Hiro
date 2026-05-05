# Hiro [v0.6]

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
```

---

## Resultado

Se genera un archivo `.desktop` en:

```bash
~/.local/share/applications/
```

### Con una estructura funcional:

* Nombre automático o personalizado
* Detección automática del tipo de ejecución
* Compatibilidad con ejecutables Linux
* Working directory correcto mediante `Path=`
* Sin terminal por defecto
* Tipo aplicación

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
  * Mensajes en consola
  * Confirmaciones

* `manager/`

  * Gestiona la lógica principal
  * Creación del `.desktop`
  * Permisos
  * Validaciones
  * Generación del contenido

---

## Estado del proyecto

### v0.6

* Reestructuración completa del proyecto
* Separación entre CLI y lógica interna
* Arquitectura modular preparada para futuras herramientas
* Generación funcional de archivos `.desktop`
* Compatibilidad con:

  * `.py`
  * `.sh`
  * binarios Linux
* Personalización del nombre del launcher
* Validación de existencia del archivo
* Validación de permisos de ejecución
* Confirmación antes de aplicar `chmod`
* Manejo básico de errores controlados
* Detección de creación o modificación del `.desktop`
* Uso correcto de `Exec=` y `Path=` para compatibilidad Linux
* Logging simple en consola

---

## Próximos pasos

* Personalización de descripción
* Soporte para iconos
* Modo terminal opcional
* Soporte para categorías (`Categories=`)
* Integración con menú contextual
* Nuevas herramientas internas dentro de Hiro

---

## Notas

* Hiro no asigna permisos automáticamente sin intervención del usuario.
* Si el archivo no existe, el proceso se cancela de forma segura.
* Si el archivo no es ejecutable, Hiro solicita confirmación antes de otorgar permisos.
* El proyecto está pensado exclusivamente para Linux y entornos compatibles con `.desktop`.
