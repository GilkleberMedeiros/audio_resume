"""
Entry point file. Usage: python resume_audio.py <audio_path>
"""

from argparse import ArgumentParser

from configs import ConfigObj
from dependencies import transcribe_audio, resume_text


configs = ConfigObj()

def main():
    parser = ArgumentParser(prog="resume_audio.py", description="Resume audios with AI.")
    parser.add_argument(
        "audio_path", 
        help="Path to the audio file to be resumed."
    )
    parser.add_argument(
        "-f", "--fake-transcription",
        dest="fake_transcription",
        help="If present espects <audio_path> to be a .txt file to use as transcription.",
        action="store_true",
    )
    parser.add_argument(
        "-t", "--just-transcription",
        dest="just_transcription",
        help="If present, return only the transcription.",
        action="store_true",
    )

    print("starting parsing args...")
    args = parser.parse_args()
    print("args parsed...")

    if args.fake_transcription:
        if not args.audio_path.endswith(".txt"):
            raise ValueError("When using -f, --fake-transcription, <audio_path> must be a .txt file.")
        
        with open(args.audio_path, "r") as f:
            audio_transcript = f.read()
    else:
        audio_transcript = transcribe_audio(args.audio_path)

    if args.just_transcription:
        print(audio_transcript)
    else:  
        resume_text(audio_transcript)


if __name__ == "__main__":
    main()