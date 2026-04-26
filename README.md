# Hiro [v0.4]

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

```
~/.local/share/applications/
```

Con una estructura funcional:

- Nombre automático (basado en el archivo)
- Ejecución mediante bash para asegurar rutas correctas
- Sin terminal
- Tipo aplicación

## Estado del proyecto
### v0.4
- Generación de .desktop funcional
- Validación básica de ejecutables
- Confirmación del usuario antes de asignar permisos (chmod)
- Cancelación del proceso si el usuario rechaza otorgar permisos
- Detección de existencia del .desktop (creación o modificación)
- Ejecución robusta usando bash -c (cd + ejecución del archivo)
- Mejora en la estructura interna del código (separación en métodos)
- Logging simple en consola

## Próximos pasos
- Soporte más completo para distintos tipos de archivo (.py, etc.)
- Agregar interfaz gráfica (PySide6)
- Personalización de nombre y descripción
- Soporte para iconos
- Integración con menú contextual

## Notas

- Hiro ya no asigna permisos automáticamente sin intervención del usuario.
- Si el archivo no es ejecutable, se solicita confirmación antes de continuar.
- Si el usuario rechaza, la creación del .desktop se cancela.