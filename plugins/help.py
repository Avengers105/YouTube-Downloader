from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>ഓ വല്ലിയ formalities ഒന്നും എനിക്ക് ഇല്ല,നിനക്ക് വേണ്ടുന്ന ആ YouTube URL ഇങ്ങോട്ട് ഒന്ന് തന്നാൽ മാത്രം മതി🤪..<\b>\n\n<i>Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url<\i>"
    await message.reply_text(helptxt)
