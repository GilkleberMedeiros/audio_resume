"""
Dependencies for resume_audio.py
"""

from langchain.prompts import PromptTemplate
from langchain_google_genai.llms import GoogleGenerativeAI
from whisper import load_model

from configs import get_configs, get_llm_model_api_key


configs = get_configs()
api_key = get_llm_model_api_key("Google")

llm_model = GoogleGenerativeAI(
    model=configs.model_name, 
    api_key=api_key, 
    temperature=configs.model_temperature, 
    top_p=configs.model_top_p, 
    top_k=configs.model_top_k
)

template = """
    Resume a text from a audio transcription and extract it key words.
    Resume what was said, and what the audio text transcript is about. 
    Structure these in the below form with "resume:" and "key words:" sections and 
    don't put the original text in the output.
    If you see any "[FAKE AUDIO]" in the start of the text, just ignore it, but do the tasks with the text.

    TEXT: {text}

    resume:

    key words:

"""

prompt_template = PromptTemplate(
    input_variables=["text"],
    template=template
)

def resume_text(text: str) -> str:
    """
    Resume text and extract key words using an AI model.
    """
    chain = prompt_template | llm_model
    response = chain.invoke({"text": text})

    print(response)

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe audio, given an audio file path.
    """
    w_model = load_model(configs.transcription_model)

    return w_model.transcribe(audio_path, fp16=False)["text"]