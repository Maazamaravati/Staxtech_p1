from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Pass your data to the HTML template
    return render_template('index.html',
                           name="Afnaan",
                           bio="Cybersecurity student with a passion for Python and ethical hacking.",
                           projects=[
                               {"name": "Quiz Game", "description": "A Python terminal quiz game.",
                                   "link": "https://github.com/Afnaan037/quiz-game"},
                               {"name": "Caesar Cipher Tool", "description": "Encrypt and decrypt messages using Caesar cipher.",
                                   "link": "https://github.com/Afnaan037/caesar-cipher"}
                           ],
                           contact={"email": "afnaanalji123@gmail.com", "github": "Afnaan037", "linkedin": "Mohammed Afnaan Alji"})


if __name__ == '__main__':
    app.run(debug=True)
