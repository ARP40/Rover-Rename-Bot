from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("28022279"))
API_HASH = os.environ.get("d3169e7c44e9de1061305b07375c1f73")
BOT_TOKEN = os.environ.get("7981941197:AAHmAHF_Ej6_7mv8rSLNERsPx_TMXFBg0n8")

app = Client(
    "rename_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

THUMBNAIL_PATH = "thumb.jpg"  # optional thumbnail

@app.on_message(filters.document)
async def rename_file(client, message):
    file = message.document
    new_filename = file.file_name.replace("_", " ")

    # Download file
    download_path = await message.download()

    # Re-upload with spaces, thumbnail, caption
    await message.reply_document(
        document=download_path,
        file_name=new_filename,
        thumb=THUMBNAIL_PATH if os.path.exists(THUMBNAIL_PATH) else None,
        caption=f"📂 {new_filename}\n✅ Renamed by @{(await app.get_me()).Rover_Rename_Bot}"
    )

    os.remove(download_path)

app.run()
