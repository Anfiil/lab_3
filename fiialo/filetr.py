import os
import re
from translation.google_trans import TransLate, LangDetect

#def file_translate(config_file: str):
#    try:
#        with open(config_file, "r") as conf:
#            lines = conf.readlines()
#            text_file = lines[0].strip()
#            lang = lines[1].strip()
#            #lang.replace("\n", "")
#            output = lines[2].strip()
#            #print(lang)
#
#        with open(text_file, "r", encoding="utf-8") as file:
#            text = file.read()
#
#        translated_text = TransLate(text, 'auto', lang)
#
#        if output == "screen":
#            print(f"Переклад:\n{translated_text}")
#        elif output == "file":
#            output_file = f"{os.path.splitext(text_file)[0]}_{lang}.txt"
#            with open(output_file, "w", encoding="utf-8") as out_file:
#                out_file.write(translated_text)
#            print("Ok")
#    except Exception as e:
#        print(f"Помилка: {str(e)}")


def file_translate(config_file: str):
    try:
        # Читання конфігураційного файлу
        with open(config_file, "r") as conf:
            lines = conf.readlines()
            text_file = lines[0].strip()  # Назва файлу з текстом
            lang = lines[1].strip()       # Мова для перекладу
            output = lines[2].strip()     # Де вивести результат: 'screen' або 'file'
            max_chars = int(lines[3].strip())  # Максимальна кількість символів
            max_words = int(lines[4].strip())  # Максимальна кількість слів
            max_sentences = int(lines[5].strip())  # Максимальна кількість речень

        # Перевірка існування текстового файлу
        if not os.path.exists(text_file):
            print(f"Помилка: файл {text_file} не існує")
            return

        # Читання текстового файлу поступово, доки не буде досягнута одна з умов
        current_text = []
        num_chars = 0
        num_words = 0
        num_sentences = 0

        with open(text_file, "r", encoding="utf-8") as file:
            for line in file:
                current_text.append(line.strip())  # Додаємо рядок до результату
                num_chars += len(line)  # Підраховуємо символи
                num_words += len(line.split())  # Підраховуємо слова
                num_sentences += len(re.findall(r'[.!?]', line))  # Підраховуємо речення

                # Перевірка, чи досягнуто хоча б однієї з умов
                if num_chars > max_chars or num_words > max_words or num_sentences > max_sentences:
                    break

        # Переклад тексту
        text_to_translate = " ".join(current_text)
        translated_text = TransLate(text_to_translate, 'auto', lang)

        # Виведення результату
        if output == "screen":
            print(f"Переклад:\n{translated_text}")
        elif output == "file":
            output_file = f"{os.path.splitext(text_file)[0]}_{lang}.txt"
            with open(output_file, "w", encoding="utf-8") as out_file:
                out_file.write(translated_text)
            print("Ok")

    except Exception as e:
        print(f"Помилка: {str(e)}")




def file_info(config_file: str):
    try:
        # Читання конфігураційного файлу
        with open(config_file, "r") as conf:
            lines = conf.readlines()
            text_file = lines[0].strip()  # Отримання назви текстового файлу

        # Перевірка наявності файлу
        if not os.path.exists(text_file):
            print(f"Помилка: файл {text_file} не існує")
            return

        # Читання вмісту файлу
        with open(text_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Розмір файлу в байтах
        file_size = os.path.getsize(text_file)

        # Кількість символів
        num_chars = len(text)

        # Кількість слів
        num_words = len(text.split())

        # Кількість речень (рахуємо по знаках кінця речення (регулярка))
        num_sentences = len(re.split(r'[.!?]', text)) - 1

        # Визначення мови тексту
        try:
            lang = LangDetect(text, 'lang')
        except Exception:
            lang = "Невідомо"

        # Виведення результатів
        print(f"Назва файлу: {text_file}")
        print(f"Розмір файлу: {file_size} байтів")
        print(f"Кількість символів: {num_chars}")
        print(f"Кількість слів: {num_words}")
        print(f"Кількість речень: {num_sentences}")
        print(f"Мова тексту: {lang}")

    except Exception as e:
        print(f"Помилка: {str(e)}")


# Виклик функції
file_info("config.ini")

file_translate("config.ini")

#file_translate("fiialo/config.ini")
