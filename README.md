from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Music Generator!"

@app.route('/generate', methods=['POST'])
def generate_music():
    data = request.json
    prompt = data.get('prompt', '')
    # Placeholder logic
    return jsonify({"message": f"Music generated from: {prompt}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
