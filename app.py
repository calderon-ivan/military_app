from flask import Flask, render_template, request

app = Flask(__name__)

# Military alphabet dictionary
military_alphabet = {
    'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
    'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
    'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
    'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee',
    'z': 'Zulu'
}

# Additional dictionary for accented characters
accented_characters = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'ü': 'u', 'ñ': 'n'
}

# Function to translate to military alphabet
def to_military_alphabet(word):
    word = word.lower()
    translation = []
    for letter in word:
        if letter in accented_characters:
            letter = accented_characters[letter]
        if letter in military_alphabet:
            translation.append(military_alphabet[letter])
        else:
            translation.append(letter)  # Keep non-alphabetic characters
    return ' '.join(translation)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word = request.form.get("word", "").strip()
        if word:
            result = to_military_alphabet(word)
            return render_template("index.html", result=result, word=word)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)