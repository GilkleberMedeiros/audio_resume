"""
File that disponibilize the configurations of the project.
"""
from pydantic import SecretStr, BaseModel

import os
import getpass
import json
from typing import Any


__configs_cache = None

class LlmModelConfig(BaseModel):
    name: str
    temperature: float
    top_p: float | None
    top_k: int | None


class ConfigObj(BaseModel):
    api_key_envvar_name: str

    llm_model: LlmModelConfig

    transcription_model: str

def get_configs() -> ConfigObj:
    global __configs_cache

    with open("./configs.json", "r") as f:
        json_configs = json.load(f)

    if not __configs_cache:
        __configs_cache = ConfigObj(**json_configs)

    return __configs_cache

def get_llm_model_api_key(model_provider: str = "") -> SecretStr:
    configs = get_configs()

    api_key = os.environ.get(configs.api_key_envvar_name, False)

    if not api_key:
        api_key = getpass.getpass(f"Please, provide your {model_provider} API key: ")

    return SecretStr(api_key)