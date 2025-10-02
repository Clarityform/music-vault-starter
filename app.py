from flask import Flask, render_template, request
from generate import generate_music

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    music_path = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        music_path = generate_music(prompt)
    return render_template('index.html', music_path=music_path)

if __name__ == '__main__':
    app.run()
