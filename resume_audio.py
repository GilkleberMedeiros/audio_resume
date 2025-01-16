"""
Entry point file. Usage: python resume_audio.py <audio_path>
"""

from sys import argv, exit
from whisper import load_model

from .configs import ConfigObj


configs = ConfigObj()

def main():
    if len(argv) < 2:
        print("Usage: python resume_audio.py <audio_path>")
        exit(1)
    elif len(argv) > 2:
        print("WARNNING: You passed more than one argument, only the first one will be used.")

    audio_path = argv[1]

    audio_transcript = transcribe_audio(audio_path)

    print(audio_transcript)


def transcribe_audio(audio_path: str) -> str:
    w_model = load_model(configs.transcription_model)

    return w_model.transcribe(audio_path, fp16=False)["text"]


if __name__ == "__main__":
    main()