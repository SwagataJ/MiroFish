"""
LLM Prompt i18n module.
Provides get_prompt() to retrieve prompts in the current language.
"""

from flask import g
from .en import PROMPTS as EN_PROMPTS
from .zh import PROMPTS as ZH_PROMPTS

_PROMPTS = {
    'en': EN_PROMPTS,
    'zh': ZH_PROMPTS,
}

DEFAULT_LANG = 'en'


def get_prompt(key):
    """
    Get a prompt string in the current request language.
    Falls back to English if key is missing.
    """
    lang = getattr(g, 'lang', DEFAULT_LANG)
    prompts = _PROMPTS.get(lang, _PROMPTS[DEFAULT_LANG])
    return prompts.get(key, _PROMPTS[DEFAULT_LANG].get(key, key))
