# Traductor al Alfabeto Militar

Este proyecto es una aplicación web sencilla que convierte palabras o frases al alfabeto militar (también conocido como alfabeto fonético). Es útil tanto para aprender las palabras clave del alfabeto militar como para traducir fácilmente texto a este sistema.

## Características

- Convierte caracteres alfabéticos (a-z) a su equivalente en alfabeto militar.
- Traduce palabras con caracteres acentuados (á, é, í, ó, ú, ñ) usando su versión sin acento.
- Mantiene caracteres no alfabéticos (como números y signos de puntuación) sin alteraciones.
- Interfaz web limpia y sencilla para interactuar con la app.

## Tecnologías utilizadas

- **Flask**: Framework web de Python para crear la aplicación web.
- **HTML/CSS**: Para crear la interfaz de usuario.
- **Python**: Lenguaje de programación utilizado para la lógica de traducción y servidor web.

## ¿Cómo funciona?

1. El usuario ingresa una palabra o frase en la barra de búsqueda de la web.
2. La aplicación traduce cada letra al alfabeto militar correspondiente (como "A" a "Alfa", "B" a "Bravo", etc.).
3. La traducción se muestra en la misma página, listando el alfabeto militar para cada letra.

## Instalar y Ejecutar Localmente

Si quieres probar la aplicación de manera local en tu máquina, sigue estos pasos:

### 1. Clona este repositorio

```bash
git clone https://github.com/tu-usuario/alfabeto-militar.git
cd alfabeto-militar
```

### 2. Ejecuta esta aplicación

```bash
python app.py
```

Por defecto, la aplicación estará corriendo en http://localhost:5000. Solo abre esta URL en tu navegador y podrás empezar a traducir palabras al alfabeto militar.
