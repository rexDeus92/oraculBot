# bot/gemini_integration.py

import os
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)

def setup_gemini():
    """
    Конфигурирует Gemini API с ключом из переменных окружения.
    Должна быть вызвана один раз при старте бота.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        # Если ключ не найден, выбрасываем исключение, чтобы бот не запустился с ошибкой
        raise ValueError("GEMINI_API_KEY не найден. Проверьте ваш .env файл и его расположение.")
    
    genai.configure(api_key=api_key)
    logger.info("Gemini API успешно сконфигурирован.")

def generate_horoscope(zodiac_sign: str) -> str:
    """
    Генерирует уникальный гороскоп для знака зодиака с помощью Gemini.
    """
    try:
        model = genai.GenerativeModel('gemini-pro')

        prompt = (
            f"Представь, что ты мудрый и загадочный астролог. "
            f"Напиши уникальный и интересный гороскоп на сегодня для знака зодиака: {zodiac_sign}. "
            f"Гороскоп должен быть позитивным, вдохновляющим и содержать одно небольшое, "
            f"но конкретное предсказание или совет. Избегай общих фраз. "
            f"Отвечай только текстом гороскопа, без лишних вступлений."
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        logger.error(f"Ошибка при генерации гороскопа через Gemini: {e}")
        return "К сожалению, звезды сегодня молчат... Произошла ошибка при связи с космосом. Попробуйте позже."