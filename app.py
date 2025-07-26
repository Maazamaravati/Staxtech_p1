from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Pass your data to the HTML template
    return render_template('index.html',
                           name="Maaz Amaravati",
                           bio="Computer science student passion in AI/ML and Python Programming.",
                           projects=[
                               {"name": "Quiz Game", "description": "A Python terminal quiz game.",
                                   "link": "https://github.com/Maazamaravati/quiz-game"},
                               {"name": "Caesar Cipher Tool", "description": "Encrypt and decrypt messages using Caesar cipher.",
                                   "link": "https://github.com/Maazamaravati/caesar-cipher"}
                           ],
                           contact={"email": "maazamaravati@gmail.com", "github": "Maazamaravai", "linkedin": "Maaz amaravati"})


if __name__ == '__main__':
    app.run(debug=True)
