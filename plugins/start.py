from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("ℂ𝕙𝕒𝕟𝕟𝕖𝕝", url="https://t.me/movielover2021")],
        [InlineKeyboardButton(
            "𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 😊", url="https://t.me/Avengerkannan")]
    ])
    welcomed = f"𝗛𝗲𝗹𝗹𝗼 <b>@{message.from_user.username}</b>\n\n@ytdownloadv2bot 𝐢𝐬 𝐭𝐡𝐞 𝐌𝐨𝐬𝐭 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐁𝐨𝐭😂[📥](https://telegra.ph/file/28f37560abd3099a65971.jpg)\n\n/help 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨\n© @songdownloading"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
