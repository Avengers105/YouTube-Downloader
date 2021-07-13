from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/movielover2021")],
        [InlineKeyboardButton("Group", url="https://t.me/songdownloading")],
        [InlineKeyboardButton("Developer 😊", url="https://t.me/Avengerkannan")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}</b>\nI am a Simple YouTube videos Download bot/n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton
    raise StopPropagation
