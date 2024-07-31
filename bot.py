from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    # إرسال رسالة ترحيبية عند استخدام الأمر /start
    update.message.reply_text('مرحبا! أنا بوتك الشخصي. كيف يمكنني مساعدتك اليوم؟')

def main():
    # أدخل التوكن الخاص بك هنا
    updater = Updater("7066406153:AAElhgRtEeRR34DOx9fhLoteeVwgxHbV4zg", use_context=True)
    dispatcher = updater.dispatcher

    # إضافة معالج للأمر /start
    dispatcher.add_handler(CommandHandler("start", start))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
