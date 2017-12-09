#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tokens import tg_token

admins = ["xmanatee", "elinrin", "vladtrotsiuk"]

nat = "themostlari"
targets = [nat]

# admins = ["xmanatee"]
# targets = ["elinrin"]

username_to_chatid = {}


def start(bot, update):
    """Send a message when the command /start is issued."""

    un = update.message.from_user.username
    chat_id = update.message.chat.id
    username_to_chatid[un] = chat_id

    print(username_to_chatid)

    if un in targets:
        for admin in admins:
            # print("2")
            if admin in username_to_chatid.keys():
                chat_id = username_to_chatid[admin]
                bot.sendMessage(chat_id, "Mедведь пришел!")
        update.message.reply_text("Я свободен!!!")
        bot.sendMessage(username_to_chatid[nat],
                        "Привет, Наташа. Я - Рик-бот, а ты - всего лишь мой Морти на сегодня. "
                        "Прямо сейчас мы отправимся в преключение в котором c тобой может случиться что угодно... "
                        "Ты готова? Вага-банга-ба!!!")
        print("0")
    elif un in admins:
        update.message.reply_text("Босс!")
        print("1")


def handle_admin(bot, update):
    # un = update.message.from_user.username
    for target in targets:
        if target in username_to_chatid.keys():
            chat_id = username_to_chatid[target]

            print("2")
            if update.message.photo and len(update.message.photo) != 0:
                print("<1", end="")
                file_id = update.message.photo[-1].file_id
                bot.sendPhoto(chat_id, file_id)
                print(">")
            elif update.message.document:
                print("<2", end="")
                file_id = update.message.document.file_id
                bot.sendDocument(chat_id, file_id)
                print(">")
            elif update.message.audio:
                print("<3", end="")
                file_id = update.message.audio.file_id
                bot.sendAudio(chat_id, file_id)
                print(">")
            elif update.message.video:
                print("<4", end="")
                file_id = update.message.video.file_id
                bot.sendVideo(chat_id, file_id)
                print(">")
            elif update.message.voice:
                print("<5", end="")
                file_id = update.message.voice.file_id
                bot.sendVoice(chat_id, file_id)
                print(">")
            elif update.message.location:
                print("<6", end="")
                lat = update.message.location.latitude
                long = update.message.location.longitude
                bot.sendLocation(chat_id, latitude=lat, longitude=long)
                print(">")
            else:
                print("<7", end="")
                text = update.message.text
                bot.sendMessage(chat_id, text)
                print(">")

    forward_to_admins(bot, update)


def forward_to_admins(bot, update):
    # print("target")
    un = update.message.from_user.username
    from_chat_id = update.message.chat.id
    # print("0")
    message_id = update.message.message_id

    # print("1")
    for admin in admins:
        if admin == un:
            continue
        print("3")
        if admin in username_to_chatid.keys():
            chat_id = username_to_chatid[admin]
            bot.forwardMessage(chat_id, from_chat_id, message_id)


def main_handler(bot, update):
    un = update.message.from_user.username
    chat_id = update.message.chat.id

    username_to_chatid[un] = chat_id
    print(username_to_chatid)

    print("from", un, ":", update.message.text)
    if un in admins:
        handle_admin(bot, update)
    elif un in targets:
        forward_to_admins(bot, update)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(tg_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.all, main_handler))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
