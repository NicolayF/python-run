# Reto 1 - Python Run, Debug the Future

## Autor

**Franco Nicolay**

---

## Descripción

Este proyecto corresponde a la resolución del **Reto 1 - Python Run, Debug the Future** de EPAM.

El objetivo fue limpiar un conjunto de reseñas de usuarios de una aplicación ficticia (FlowApp), calcular las palabras más frecuentes para cada nivel de rating y generar un resumen estadístico del dataset.

La solución fue desarrollada utilizando únicamente Pandas y herramientas de la biblioteca estándar de Python.

---

## Objetivos

- Limpiar el dataset.
- Normalizar el texto de las reseñas.
- Calcular las palabras más frecuentes por nivel de rating.
- Generar un resumen estadístico del dataset.

---

## Tecnologías utilizadas

- Python 3
- Pandas
- Biblioteca estándar de Python (`re` y `collections.Counter`)

---

## Estructura del proyecto

```
.
├── datos/
│   └── resenas_flowapp.csv
├── main.py
└── README.md
```

---

## Limpieza de datos

Durante el procesamiento se realizaron las siguientes tareas:

- Eliminación de registros duplicados.
- Eliminación de filas con valores nulos en las columnas **texto** y **rating**.
- Conservación únicamente de ratings válidos (1 a 5).
- Conversión de la columna **fecha** al tipo `datetime`.
- Conversión de la columna **rating** al tipo `int`.
- Normalización del texto:
  - Conversión a minúsculas.
  - Eliminación de emojis.
  - Eliminación de caracteres especiales y números.
  - Normalización de espacios en blanco.
- Eliminación de textos que quedaron vacíos luego de la limpieza.

**Nota**: La limpieza de texto se realizó mediante expresiones regulares (re), conservando caracteres propios del idioma español como tildes y la letra ñ.

---

## Requisitos

- Python 3
- Pandas

## Instalación

Instalar la dependencia:

```bash
pip install pandas
```

## Ejecución

Antes de ejecutar el programa, el archivo `resenas_flowapp.csv` debe ubicarse dentro de la carpeta `datos/`.

Ejecutar el programa:

```bash
python main.py
```

---

## Salida del programa

El script muestra por consola:

- Validación básica del dataset.
- Palabras más frecuentes para cada nivel de rating.
- Resumen estadístico:
  - Promedio.
  - Mediana.
  - Distribución de ratings.
  - Porcentaje de reseñas positivas, neutras y negativas.

---

## Decisiones tomadas

- Se conservaron las tildes y la letra **ñ** para mantener el significado de las palabras.
- No se eliminaron *stopwords*, ya que la consigna solicita calcular las palabras más frecuentes y no especifica un filtrado adicional.
- Se utilizó una solución basada en Pandas y la biblioteca estándar de Python, priorizando un código simple, legible y fácil de reproducir.
