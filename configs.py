"""
File that disponibilize the configurations of the project.
"""

class ConfigObj:
    def __init__(self) -> None:
        self.transcription_model = "small"

        self.api_key_envvar_name = "GOOGLE_AISTUDIO_API_KEY"

        self.model_name = "gemini-pro"
        self.model_temperature = 0.7
        self.model_top_p = None
        self.model_top_k = None