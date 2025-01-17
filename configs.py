"""
File that disponibilize the configurations of the project.
"""
from pydantic import SecretStr

import os
import getpass


__configs_cache = None

class ConfigObj:
    def __init__(self) -> None:
        self.transcription_model = "small"

        self.api_key_envvar_name = "GOOGLE_AISTUDIO_API_KEY"

        self.model_name = "gemini-pro"
        self.model_temperature = 0.7
        self.model_top_p = None
        self.model_top_k = None

def get_configs() -> ConfigObj:
    global __configs_cache

    if not __configs_cache:
        __configs_cache = ConfigObj()

    return __configs_cache

def get_llm_model_api_key(model_provider: str = "") -> SecretStr:
    configs = get_configs()

    api_key = os.environ.get(configs.api_key_envvar_name, False)

    if not api_key:
        api_key = getpass.getpass(f"Please, provide your {model_provider} API key: ")

    return SecretStr(api_key)