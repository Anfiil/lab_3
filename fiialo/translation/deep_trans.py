#from deep_translator import GoogleTranslator
#from langdetect import detect
#
#def TransLate(text: str, src: str = 'auto', dest: str = 'en') -> str:
#    #Перекладає текст на вказану мову.
#    try:
#        translator = GoogleTranslator(source=src, target=dest)
#        return translator.translate(text)
#    except Exception as e:
#        return f"Помилка: {str(e)}"
#
#def LangDetect(text: str, set: str = "all") -> str:
#    #Визначає мову тексту.
#    try:
#        lang = detect(text)
#        if set == "lang":
#            return lang
#        elif set == "confidence":
#            return "Недоступно в langdetect"
#        else:
#            return f"Мова: {lang}"
#    except Exception as e:
#        return f"Помилка: {str(e)}"


from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory, LangDetectException

# Для отримання стабільних результатів при визначенні мови
DetectorFactory.seed = 0

def TransLate(text: str, src: str = 'auto', dest: str = 'en') -> str:
    # Перекладає текст на вказану мову або повідомляє про помилку.
    try:
        if src == 'auto':
            src = detect(text)
        translation = GoogleTranslator(source=src, target=dest).translate(text)
        return translation
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    # Визначає мову тексту та коефіцієнт довіри.
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        else:
            return f"Мова: {detected_lang}"  # Бібліотека langdetect не дає прямої довіри, тільки мову
    except LangDetectException as e:
        return f"Помилка: {str(e)}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    # Виводить таблицю підтримуваних мов та перекладений текст.
    try:
        supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)
        result = "N  Language         ISO-639 code   Text\n"
        result += "-" * 50 + "\n"
        for i, (code, lang) in enumerate(supported_languages.items(), 1):
            translation = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
            result += f"{i:<3} {lang:<15} {code:<14} {translation}\n"
        result += "\n" + 50 * "-" + "\nOk"

        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages_list.txt", "w", encoding="utf-8") as file:
                file.write(result)
        return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"
