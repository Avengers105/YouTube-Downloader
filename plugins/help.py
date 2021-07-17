from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>ഓ വല്ലിയ formalities ഒന്നും എനിക്ക് ഇല്ല,ഒരു YouTube URL ഇങ്ങോട്ട് ഒന്ന് തന്നാൽ മാത്രം മതി🤪..\n\nCurrently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_text(helptxt)
