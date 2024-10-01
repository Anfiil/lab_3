from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, src: str = 'auto', dest: str = 'en') -> str:
    #Перекладає текст на вказану мову або повідомляє про помилку.
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    #Визначає мову тексту та коефіцієнт довіри.
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Мова: {detection.lang}, Довіра: {detection.confidence}"
    except Exception as e:
        return f"Помилка: {str(e)}"

def CodeLang(lang: str) -> str:
    #Повертає код мови або назву мови.
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Помилка: не знайдено відповідного коду або назви мови."

def LanguageList(out: str = "screen", text: str = "") -> str:
    #Виводить таблицю підтримуваних мов та перекладений текст.
    try:
        languages = list(LANGUAGES.items())
        result = "N  Language         ISO-639 code   Text\n"
        result += "-" * 50 + "\n"
        for i, (code, lang) in enumerate(languages, 1):
            translation = translator.translate(text, dest=code).text if text else ""
            result += f"{i:<3} {lang:<15} {code:<14} {translation}\n"
        result += "\n"+ 50*"-"+"\nOk"

        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages_list.txt", "w", encoding="utf-8") as file:
                file.write(result)
        return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"


