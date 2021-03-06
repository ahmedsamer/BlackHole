# -*- coding: utf-8 -*-
import os.path
from blackhole.black_hole import settings
import gettext

TRANSLATION_DOMAIN = "BlackHole"
DEFAULT_LANGUAGE = 'en-us'
AVAILABLE_LANGUAGES = ['es', 'es-AR', 'en-us']
LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")
if settings.LANGUAGE_CODE not in AVAILABLE_LANGUAGES:
    LANGUAGE = DEFAULT_LANGUAGE
else:
    LANGUAGE = settings.LANGUAGE_CODE
LANGUAGES = [LANGUAGE]
lang = gettext.translation(TRANSLATION_DOMAIN, LOCALE_DIR, LANGUAGES)
lang.install()
