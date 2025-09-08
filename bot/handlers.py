# Bot command handlers 
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from .gemini_integration import generate_horoscope # Импортируем новую функцию

# Знаки зодиака для клавиатуры (остаются без изменений)
ZODIAC_SIGNS = [
    ["Овен", "Телец", "Близнецы"],
    ["Рак", "Лев", "Дева"],
    ["Весы", "Скорпион", "Стрелец"],
    ["Козерог", "Водолей", "Рыбы"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Отправляет приветственное сообщение и клавиатуру с выбором знака зодиака.
    """
    keyboard = [[KeyboardButton(sign) for sign in row] for row in ZODIAC_SIGNS]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    await update.message.reply_text(
        "Привет! Я твой персональный астролог на базе искусственного интеллекта. "
        "Выбери свой знак зодиака, и я составлю для тебя уникальное предсказание на сегодня.",
        reply_markup=reply_markup
    )

async def zodiac_sign_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обрабатывает выбор знака зодиака и отправляет гороскоп от Gemini.
    """
    zodiac_sign = update.message.text
    
    # Проверка, что выбранный текст есть в нашем списке знаков
    if any(zodiac_sign in row for row in ZODIAC_SIGNS):
        await update.message.reply_text(f"✨ Соединяюсь с космосом, чтобы составить предсказание для знака {zodiac_sign}...")
        
        # Получаем гороскоп от Gemini
        horoscope_text = generate_horoscope(zodiac_sign)
        
        await update.message.reply_text(horoscope_text)
    else:
        await update.message.reply_text("Пожалуйста, выбери знак зодиака с помощью клавиатуры.")