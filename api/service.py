from translate import Translator

class TranslationSrevice:
    _cache = {}

    @staticmethod
    def translate_text(text:str, target_lang:str) -> dict:
        if (text, target_lang) in TranslationSrevice._cache:
            return TranslationSrevice._cache[(text, target_lang)]
        else:
            translator = Translator(to_lang=target_lang)
            translated_text = translator.translate(text)

            TranslationSrevice._cache[(text, target_lang)] = {
                "original_text": text,
                "translated_text": translated_text,
                "target_lanuange": target_lang,
            }

            return TranslationSrevice._cache[(text, target_lang)]