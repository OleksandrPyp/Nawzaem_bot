import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, filters, MessageHandler, ConversationHandler, \
    ContextTypes, Application, CallbackContext
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("tg_token")
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    bot_menu_msg = '''Привіт, я бот Навзаєм та ось що я можу:
/start - інформація про спільноту 
/help - список команд
/mentorship - менторство
/partnership - партнерство
/post_vacancy - розміщення вакансій
/post_ad - розміщення реклами
/support_project - підтримати проект
/website - веб сайт
/app - мобільний застосунок
'''
    await context.bot.send_message(chat_id=chat_id, text=bot_menu_msg)


async def start_command(update: Update, context):
    user_id = update.message.from_user.id
    user = update.message.from_user
    chat_id = update.message.chat_id

    intro_message = """
*Вітаємо у спільноті Навзаєм!*
"""

    info_button = InlineKeyboardButton("Про спільноту Навзаєм", url="#")
    rules_button = InlineKeyboardButton("Правила спільноти", url="#")

    welcome_keyboard = [
        [info_button],
        [rules_button]
    ]

    reply_markup = InlineKeyboardMarkup(welcome_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=intro_message, reply_markup=reply_markup,
                                   parse_mode="Markdown")


async def mentorship_command(update: Update, context):
    chat_id = update.message.chat_id
    mentor_message = """#"""
    mentor_keyboard = [
        [
            InlineKeyboardButton("Обрати ментор_ку", url="#")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(mentor_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=mentor_message, reply_markup=reply_markup,
                                   parse_mode="Markdown")


async def partnership_command(update: Update, context):
    chat_id = update.message.chat_id
    partner_message = """
#
    """

    conditions_button = InlineKeyboardButton("Умови співпраці", url="#")
    form_button = InlineKeyboardButton("Заповнити форму", url="#")
    manager_button = InlineKeyboardButton("Написати менеджерці", url="#")

    custom_keyboard = [
        [conditions_button],
        [form_button],
        [manager_button]
    ]

    reply_markup = InlineKeyboardMarkup(custom_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=partner_message, reply_markup=reply_markup,
                                   parse_mode="Markdown")


async def post_vacancy_command(update: Update, context):
    chat_id = update.message.chat_id
    vacancy_message = """#"""

    conditions_button = InlineKeyboardButton("Умови розміщення", url="#")
    order_button = InlineKeyboardButton("Замовити розміщення вакансії", url="#")
    manager_button = InlineKeyboardButton("Написати менеджерці", url="#")

    vacancy_keyboard = [
        [conditions_button],
        [order_button],
        [manager_button]
    ]

    reply_markup = InlineKeyboardMarkup(vacancy_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=vacancy_message, reply_markup=reply_markup,
                                   parse_mode="Markdown")


async def post_ad_command(update: Update, context):
    chat_id = update.message.chat_id
    ad_message = """#"""

    conditions_button = InlineKeyboardButton("Умови розміщення", url="#")
    order_button = InlineKeyboardButton("Замовити розміщення нативної реклами", url="#")
    manager_button = InlineKeyboardButton("Написати менеджерці", url="#")

    ad_keyboard = [
        [conditions_button],
        [order_button],
        [manager_button]
    ]

    reply_markup = InlineKeyboardMarkup(ad_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=ad_message, reply_markup=reply_markup, parse_mode="Markdown")


async def support_project_command(update: Update, context):
    chat_id = update.message.chat_id
    support_message = """#"""
    send_button = InlineKeyboardButton("Зробити внесок", url="#")

    support_keyboard = [
        [send_button]
    ]

    reply_markup = InlineKeyboardMarkup(support_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=support_message, reply_markup=reply_markup,
                                   parse_mode="Markdown")


async def website_command(update: Update, context):
    chat_id = update.message.chat_id
    web_message = """
    #
    """

    web_keyboard = [
        [
            InlineKeyboardButton("На сайт", url="https://navzaem.com/")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(web_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=web_message, reply_markup=reply_markup, parse_mode="Markdown")


async def app_command(update: Update, context):
    chat_id = update.message.chat_id
    app_message = """#"""
    app_button = InlineKeyboardButton("Перейти до застосунку", url="#")
    manager_button = InlineKeyboardButton("Написати менеджерці", url="#")

    app_keyboard = [
        [app_button],
        [manager_button]
    ]

    reply_markup = InlineKeyboardMarkup(app_keyboard)

    await context.bot.send_message(chat_id=chat_id, text=app_message, reply_markup=reply_markup, parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is not None and update.message.text:
        pass


async def handle_mention(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        bot_username = "nawzaem_bot"
        if update.message.entities:
            for entity in update.message.entities:
                if entity.type == 'mention':
                    mentioned_username = entity.user.username
                    if mentioned_username:
                        if mentioned_username == bot_username:
                            chat_id = update.message.chat_id
                            await context.bot.send_message(chat_id=chat_id,
                                                           text="I was mentioned! How can I assist you?")
                    else:
                        chat_id = update.message.chat_id
                        await context.bot.send_message(chat_id=chat_id,
                                                       text="The mentioned user does not have a username.")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting the bot...")
    app = Application.builder().token(tg_token).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("mentorship", mentorship_command))
    app.add_handler(CommandHandler("partnership", partnership_command))
    app.add_handler(CommandHandler("post_vacancy", post_vacancy_command))
    app.add_handler(CommandHandler("post_ad", post_ad_command))
    app.add_handler(CommandHandler("support_project", support_project_command))
    app.add_handler(CommandHandler("website", website_command))
    app.add_handler(CommandHandler("app", app_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & filters.Entity(filters.MessageEntity.MENTION), handle_mention))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Looking for new messages...")
    app.run_polling(poll_interval=5)
