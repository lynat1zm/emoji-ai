import ollama

def define_emoji(img_path: str):
    response = ollama.chat(
        model="qwen3.5:cloud",
        messages=[{
            "role": "user",
            "content": "Рассмотри изображение, и определи эмоцию изображенную на нем. В ответ ты должен прислать json со смайликом, подходящим этой эмоции. Пример JSON {'emoji': '😀'}. Возвращай только фигурные скобки и их содержимое!",
            "images": [img_path]
        }]
    )

    return response["message"]["content"]