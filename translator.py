# translator.py
import argostranslate.translate

def translate_text(text: str, from_lang: str, to_lang: str) -> str:
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang_obj = next((lang for lang in installed_languages if lang.code == from_lang), None)
    to_lang_obj = next((lang for lang in installed_languages if lang.code == to_lang), None)

    if not from_lang_obj or not to_lang_obj:
        return "❌ Language not supported."

    translation = from_lang_obj.get_translation(to_lang_obj)
    return translation.translate(text)
