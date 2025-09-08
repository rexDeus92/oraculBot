# Gemini API integration 
import os
import google.generativeai as genai

# Конфигурируем API-ключ при загрузке модуля
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    print(f"Ошибка конфигурации Gemini API: {e}. Убедитесь, что GEMINI_API_KEY задан в .env")

def generate_horoscope(zodiac_sign: str) -> str:
    """
    Генерирует уникальный гороскоп для знака зодиака с помощью Gemini.
    """
    try:
        # Инициализация модели
        model = genai.GenerativeModel('gemini-pro')

        # Создаем креативный промпт для модели
        prompt = (
            f"Представь, что ты мудрый и загадочный астролог. "
            f"Напиши уникальный и интересный гороскоп на сегодня для знака зодиака: {zodiac_sign}. "
            f"Гороскоп должен быть позитивным, вдохновляющим и содержать одно небольшое, "
            f"но конкретное предсказание или совет. Избегай общих фраз. "
            f"Отвечай только текстом гороскопа, без лишних вступлений."
        )

        # Отправляем промпт модели
        response = model.generate_content(prompt)

        # Возвращаем сгенерированный текст
        return response.text

    except Exception as e:
        print(f"Ошибка при генерации гороскопа через Gemini: {e}")
        return "К сожалению, звезды сегодня молчат... Произошла ошибка при связи с космосом. Попробуйте позже."