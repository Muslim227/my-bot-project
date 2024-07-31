from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# تعريف دالة التعامل مع أمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوتك الجديد.')

# الدالة الرئيسية لتشغيل البوت
def main():
    # استبدل YOUR_TOKEN_HERE بالتوكن الذي حصلت عليه من BotFather
    updater = Updater("7066406153:AAElhgRtEeRR34DOx9fhLoteeVwgxHbV4zg")
    dispatcher = updater.dispatcher

    # إضافة معالج الأمر /start
    dispatcher.add_handler(CommandHandler("start", start))

    # بدء استقبال التحديثات من تليجرام
    updater.start_polling()

    # إبقاء البوت قيد التشغيل حتى يتم إيقافه يدويًا
    updater.idle()

if __name__ == '__main__':
    main()
