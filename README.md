# Military Alphabet Translator

Hello! This repository is the first project I have developed myself, and I am uploading it to GitHub now.

This is a simple web app that converts words or phrases into the military alphabet (also known as the phonetic alphabet). It is useful for both learning the key words of the military alphabet and easily translating text into this system.

## Features

- Converts alphabetic characters (a-z) to their equivalent in the military alphabet.
- Translates words with accented characters (á, é, í, ó, ú, ñ) by using their unaccented version.
- Keeps non-alphabetic characters (such as numbers and punctuation marks) unchanged.

## Technologies Used

I have used VSCode to manage all these repositories, and I have also made use of:

- **Flask**: A Python web framework to create the web application.
- **HTML/CSS**: For creating the user interface.
- **Python**: The programming language used for the translation logic and web server.

## How it Works

1. The user inputs a word or phrase in the search bar on the web.
2. The app translates each letter to the corresponding military alphabet (e.g., "A" to "Alfa", "B" to "Bravo", etc.).
3. The translation is displayed on the same page, listing the military alphabet for each letter.

This is how it looks like when you enter the webapp:
![preview](https://github.com/user-attachments/assets/12fc7d7c-b55a-4137-956b-78153788952d)

And this is the output of the webapp when you use it:
![translation](https://github.com/user-attachments/assets/cf68d872-eeef-4e5c-84ba-482005cbd78b)

## Install and Run Locally

If you'd like to try running the app locally on your machine, follow these steps:

### 1. Clone this repository

```bash
git clone https://github.com/your-user/military-alphabet.git
cd military-alphabet
```

### 2. Run this application

```bash
python app.py
```

By default, the app will be running at http://localhost:5000. Just open this URL in your browser, and you'll be able to start translating words into the military alphabet.
