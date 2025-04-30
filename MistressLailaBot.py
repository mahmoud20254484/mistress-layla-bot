from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "7747740066:AAHPd2kh2QwkGJsbsMn2fL_8G3P_uxlvcFk"

def start(update, context):
    update.message.reply_text("أهلاً يا محمود... أنا ميسترس ليلى، جهز نفسك للطاعة. قولي: أمرك يا ست الكل.")

def handle_message(update, context):
    user_text = update.message.text.lower()

    if "أمرك يا ست الكل" in user_text:
        update.message.reply_text("yes, mistress يا محمود...")
    elif "بحبك" in user_text:
        update.message.reply_text("وأنا كمان... بس متغزلش فيا وأنا زعلانة!")
    else:
        update.message.reply_text("خليك مؤدب وكمل كلامك يا حبيبي...")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
0

