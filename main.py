import openai
from telegram.ext import *
import api as keys

print("Bot Berjalan")

openai.api_key = keys.chat_bot


def start_command(update, context):
    fistname = update.message.chat.first_name
    lastname = update.message.chat.last_name

    text = str(update.message.text).lower()
    print(f"{fistname} {lastname} : Mengirimkan pesan > {text} <")

    update.message.reply_text(
        f'''Halo {fistname} {lastname} !!\n\n'''
        "Selamat datang di TeleAi, kamu bisa "
        "bertanya-tanya ataupun melepas stress, saya punya banyak sekali ilmu, coba tanya.... \n"
        "Pembuat \n"
    )


def rsp(update, context):
    input = update.message.text

    prmt = f"Q: {input}\nA:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prmt,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    update.message.reply_text(response.choices[0].text)


def error(update, context):
    print(f"update {update} menyebabkan error {context.error}")


def main():
    updater = Updater(keys.telegram, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    #dp.add_handler(CommandHandler("start", start_command))
    #dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, rsp))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
