from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)

# Set your Replicate API key securely
os.environ["REPLICATE_API_TOKEN"] = "your_replicate_api_token"

@app.route('/')
def home():
    return "🎵 Welcome to your Music Generator!"

@app.route('/generate', methods=['POST'])
def generate_music():
    data = request.get_json()
    prompt = data.get('prompt', '')

    try:
        # Connect to MusicGen model on Replicate
        output = replicate.run(
            "facebook/musicgen-small",
            input={"prompt": prompt}
        )

        audio_url = output  # Should return direct .mp3/.wav link
        return jsonify({
            "message": f"🎶 Music generated from: {prompt}",
            "url": audio_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
