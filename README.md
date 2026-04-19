# Hiro [V0.1]

Hiro es una herramienta simple para generar archivos `.desktop` en Linux a partir de cualquier archivo ejecutable.

## Descripción

Permite crear accesos directos (`.desktop`) de forma rápida, sin tener que escribir manualmente la estructura del archivo.

Pensado como una herramienta personal para simplificar el uso de ejecutables, scripts o AppImages.

## Uso [Actual]

```bash
python main.py /ruta/al/archivo
```

Si no se proporciona una ruta, se usa un archivo de prueba interno.

## Resultado

Se genera un archivo `.desktop` en:

```
~/.local/share/applications/
```

Con una estructura básica:

* Nombre automático (basado en el archivo)
* Ruta de ejecución (`Exec`)
* Sin terminal
* Tipo aplicación

## Estado del proyecto

v0.1

* Generación básica de `.desktop`
* Sin interfaz gráfica
* Sin validaciones avanzadas

## Próximos pasos

* Agregar interfaz gráfica (PySide6)
* Personalización de nombre y descripción
* Soporte para iconos
* Integración con menú contextual