from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"{message.from_user.first_name},ഒരു 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗨𝗿𝗹 ഇങ്ങോട്ട് തന്നെ😊..\n\n𝖢𝗎𝗋𝗋𝖾𝗇𝗍𝗅𝗒 𝖮𝗇𝗅𝗒 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖸𝗈𝗎𝖳𝗎𝖻𝖾 𝖲𝗂𝗇𝗀𝗅𝖾  (No playlist) 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝗍 𝖸𝗈𝗎𝖳𝗎𝖻𝖾 𝖴𝗋𝗅"
    await message.reply_text(helptxt)
