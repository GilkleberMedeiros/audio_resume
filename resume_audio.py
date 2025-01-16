"""
Entry point file. Usage: python resume_audio.py <audio_path>
"""

from argparse import ArgumentParser
from whisper import load_model

from configs import ConfigObj


configs = ConfigObj()

def main():
    parser = ArgumentParser(prog="resume_audio.py", description="Resume audios with AI.")
    parser.add_argument(
        "audio_path", 
        help="Path to the audio file to be resumed."
    )

    args = parser.parse_args()

    audio_transcript = transcribe_audio(args.audio_path)

    print(audio_transcript)


def transcribe_audio(audio_path: str) -> str:
    w_model = load_model(configs.transcription_model)

    return w_model.transcribe(audio_path, fp16=False)["text"]


if __name__ == "__main__":
    main()