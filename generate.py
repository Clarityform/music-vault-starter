import os
import uuid
from riffusion_full.riffusion.cli import run_txt2im
from pydub import AudioSegment

def generate_music(prompt: str):
    # Run the Riffusion CLI tool to generate music from prompt
    # This assumes you have Riffusion set up locally.
    output_id = str(uuid.uuid4())
    output_path = f'static/music/{output_id}.wav'

    os.system(f'riffusion --prompt "{prompt}" --output {output_path}')

    # Convert to MP3 if needed
    # sound = AudioSegment.from_wav(output_path)
    # mp3_path = output_path.replace(".wav", ".mp3")
    # sound.export(mp3_path, format="mp3")

    return output_path
