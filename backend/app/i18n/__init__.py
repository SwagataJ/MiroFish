"""
MiroFish Backend i18n Module
Simple dictionary-based internationalization.
"""

from flask import g, request

from .en import MESSAGES as EN_MESSAGES
from .zh import MESSAGES as ZH_MESSAGES

SUPPORTED_LANGS = {'en', 'zh'}
DEFAULT_LANG = 'en'

_MESSAGES = {
    'en': EN_MESSAGES,
    'zh': ZH_MESSAGES,
}


def init_i18n(app):
    """Register before_request hook to detect language from Accept-Language header."""
    @app.before_request
    def set_lang():
        accept = request.headers.get('Accept-Language', DEFAULT_LANG)
        lang = accept.split(',')[0].strip().split('-')[0].lower()
        if lang not in SUPPORTED_LANGS:
            lang = DEFAULT_LANG
        g.lang = lang


def get_text(key, **kwargs):
    """
    Get a translated message string.
    Falls back to English if key is missing in the current language.
    Supports str.format(**kwargs) interpolation.
    """
    try:
        lang = getattr(g, 'lang', DEFAULT_LANG)
    except RuntimeError:
        # Outside of Flask application context (e.g., background threads)
        lang = DEFAULT_LANG
    messages = _MESSAGES.get(lang, _MESSAGES[DEFAULT_LANG])
    text = messages.get(key)
    if text is None:
        text = _MESSAGES[DEFAULT_LANG].get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text
