import os
import ast
from pathlib import Path
from func.emoji import define_emoji

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE_DIR / "images"

def start_cli(width=50):
    while True:
        os.system("cls")
        print(
f"""{"="*width}

{"Приветствуем вас в Emoji AI".center(width)}

{"="*width}

1. Руководство
2. Распознать эмоцию
3. Выйти"""
            )
        
        choice = int(input("Введите цифру: "))

        if choice == 1:
            os.system("cls")
            print("\n\n1. В папке с программой находиться папка images, загрузите туда нужные фотографии.\n2. Запустите программу, и выберите пункт 2.\n3. Вы увидете список фотографий, выберите нужную.\n\n")
            input("Нажмите ENTER чтобы продолжить!")

        if choice == 2:
            os.system("cls")
            images_list = os.listdir(IMAGES_DIR)
            print("Список изображений: ")

            for num, pic in enumerate(images_list, start=1):
                print(f"{num}. {pic}")
            print("\n")

            img_choice = int(input("Введите номер изображения: "))
            os.system("cls")
            print("Пытаемся распознать эмоцию...")
            answer = define_emoji(IMAGES_DIR / images_list[img_choice - 1])

            if answer:
                parsed = ast.literal_eval(answer)
                print(f"\nЭмоция распознана: {parsed["emoji"]}")
                input("Нажмите ENTER чтобы продолжить!")
            else:
                print("\nНе удалось распознать эмоцию")
                input("Нажмите ENTER чтобы продолжить!")

        if choice == 3:
            os.system("cls")
            exit()