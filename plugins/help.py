from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"{message.from_user.first_name},เดเดฐเต ๐ฌ๐ผ๐๐ง๐๐ฏ๐ฒ ๐จ๐ฟ๐น เดเดเตเดเตเดเตเดเต เดคเดจเตเดจเต๐..\n\n๐ข๐๐๐๐พ๐๐๐๐ ๐ฎ๐๐๐ ๐ฒ๐๐๐๐๐๐๐ ๐ธ๐๐๐ณ๐๐ป๐พ ๐ฒ๐๐๐๐๐พ  (No playlist) ๐ฉ๐๐๐ ๐ฒ๐พ๐๐ ๐ธ๐๐๐ณ๐๐ป๐พ ๐ด๐๐"
    await message.reply_text(helptxt)
