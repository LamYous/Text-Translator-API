from translate import Translator

class TranslationSrevice:
    _cache = {}

    @staticmethod
    def translate_text(text:str, target_language:str) -> dict:
        if (text, target_language) in TranslationSrevice._cache:
            return TranslationSrevice._cache[(text, target_language)]
        else:
            translator = Translator(to_lang=target_language)
            translated_text = translator.translate(text)

            TranslationSrevice._cache[(text, target_language)] = {
                "original_text": text,
                "translated_text": translated_text,
                "target_language": target_language,
            }

            return TranslationSrevice._cache[(text, target_language)]