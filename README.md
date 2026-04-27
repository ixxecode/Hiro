# Hiro [v0.5]

Hiro es una herramienta simple para generar archivos .desktop en Linux a partir de cualquier archivo ejecutable.

## Descripción

Permite crear accesos directos (.desktop) de forma rápida, sin tener que escribir manualmente la estructura del archivo.

Pensado como una herramienta personal para simplificar el uso de ejecutables, scripts o AppImages.

## Uso [Actual]

```bash
python main.py /ruta/al/archivo
```

Si no se proporciona una ruta, se usa un archivo de prueba interno.

## Resultado

Se genera un archivo .desktop en:

```bash
~/.local/share/applications/
```

### Con una estructura funcional:

- Nombre automático (basado en el archivo)
- Ejecución adaptada según el tipo de archivo
- Sin terminal
- Tipo aplicación

## Estado del proyecto

### v0.5

- Generación de .desktop funcional
- Validación básica de ejecutables
- Confirmación del usuario antes de asignar permisos (chmod)
- Cancelación del proceso si el usuario rechaza otorgar permisos
- Detección de existencia del .desktop (creación o modificación)
- Ejecución diferenciada según tipo de archivo:
 - .py → python3
 - .sh → bash
 - otros → bash -c (cd + ejecución)
- Mejora en la estructura interna del código (separación en métodos)
- Logging simple en consola

## Próximos pasos

- Mejorar soporte para archivos .py (modo terminal opcional)
- Agregar interfaz gráfica (PySide6)
- Personalización de nombre y descripción
- Soporte para iconos
- Integración con menú contextual

## Notas
- Hiro no asigna permisos automáticamente sin intervención del usuario.
- Si el archivo no es ejecutable, se solicita confirmación antes de continuar.
- Si el usuario rechaza, la creación del .desktop se cancela.