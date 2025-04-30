
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "TOKEN = "7747740066:AAHPd2kh2QwkGJsbsMn2fL_8G3P_uxlvcFk
def start(update, context):
    update.message.reply_text("أهلاً يا محمود، ليلى هنا. جاهز للتعليم؟")

def handle_message(update, context):
    user_text = update.message.text.lower()
    if "أمرك" in user_text:
        update.message.reply_text("Yes, mistress يا محمود")
    else:
        update.message.reply_text("عايز تقول إيه بالظبط؟")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
