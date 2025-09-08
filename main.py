# Main bot file 
import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import start, zodiac_sign_handler

# Загружаем переменные окружения в самом начале
load_dotenv()

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Запуск бота.
    """
    token = os.getenv("TELEGRAM_TOKEN")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if not token:
        logger.error("Не найден TELEGRAM_TOKEN в .env файле!")
        return
    if not gemini_key:
        logger.error("Не найден GEMINI_API_KEY в .env файле!")
        return

    # Создаем приложение
    application = Application.builder().token(token).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    
    # Обработчик для текстовых сообщений (знаков зодиака)
    zodiacs = [sign for row in [
        ["Овен", "Телец", "Близнецы"], ["Рак", "Лев", "Дева"], 
        ["Весы", "Скорпион", "Стрелец"], ["Козерог", "Водолей", "Рыбы"]
    ] for sign in row]
    zodiac_filter = filters.TEXT & (~filters.COMMAND) & filters.Regex(f'^({"|".join(zodiacs)})$')
    application.add_handler(MessageHandler(zodiac_filter, zodiac_sign_handler))
    
    # Запускаем бота
    logger.info("Бот запускается...")
    application.run_polling()

if __name__ == '__main__':
    main()