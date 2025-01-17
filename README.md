# Resume Audio
Simple project with cli command that resume audio with AI.

## Installation
Install requirements with `pip install -r requirements.txt` into your virtual environment or globally and 
you're set. The command/entry point is `resume_audio.py`.

## Usage
### resume_audio command
Just run `python resume_audio.py audio_file_path` and the audio will be resumed and key words extracted to your
terminal. This command use whisper AI locally to transcript the audio, so be careful if you don't think you 
have a computer powerful enough. In the other hand, it use Google AI remote models to resume and extract the kw.
If you wanna know more about the command, just run `python resume_audio.py --help`.


### `configs.json`
In `configs.json` you have the configs for the command. The configs are listed below:
- llm_model: configs form the llm model.
    - name: the name of the google model.
    - temperature: The temperature param for the model.
    - top_p: The top_p param for the model.
    - top_k: The top_k param for the model.
- transcription_model: The whisper transcription model type/size.
- api_key_envvar_name: The name of the env var that contains the google api key.

## About and more
### Cronstructed with
As said above, this project was constructed with whisper AI running locally and Google AI running remote.
But futhermore, it was constructed with Python 3.12.1 and the following libraries:
- langchain==0.3.14
- langchain-google-genai==2.0.8
- openai-whisper==20240930

### Tips
This project already provide some audios files to test the command. They are in the `audios` folder and also 
fake audios files to be used when using the command like `python resume_audio.py -f "txt_file_path"`. This 
will not run whisper, will use the text in the file as the audio transcript.

Use "" to pass params with spaces ' '.

### Examples
Some examples of responses.
- `python resume_audio.py -f "./fake_audios/I Spent 30 Days Learning Pixel Art.txt"`:
    Response:
    ```bash
    **Resume:**

    The speaker embarked on a 30-day challenge to learn and thrive in pixel art, despite having no prior experience. Despite initial setbacks, they persisted, experimenting with different techniques and seeking feedback from social media. By the end of the challenge, they had developed their own unique style and received positive feedback on their work.

    **Key Words:**

    * Pixel art
    * Art challenge
    * Learning curve
    * Social media feedback
    * Experimentation
    * Style development
    * Perseverance
    ```
- `python resume_audio.py -f "./fake_audios/Bryan_-_The_Ideal_Republic.ogg.txt"`:
    response:
    ```bash
    **resume:**

    The text envisions a republic that upholds equality, liberty, and self-governance. It emphasizes the importance of civil and religious freedom, the rule of law, and the sovereignty of citizens. The republic is depicted as a beacon of hope and inspiration, influencing global progress and resolving societal issues.

    **key words:**

    * Republic
    * Equality
    * Liberty
    * Self-governance
    * Civil and religious freedom
    * Rule of law
    * Sovereignty
    * Progress
    * Inspiration
    * Influence
    * Universal brotherhood
    ```

The above examples are made with the fake audios files in the `fake_audios` folder. The results are the same of 
running with the real audios, because the these fake audios files are the transcript of the real audios files 
extracted with `-t` flag.

### Hardware needed to run whisper
I runned whisper with an I5 3470 without GPU and it took 6:30 minutes to transcript a 9:30 minutes audio.