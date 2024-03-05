import asyncio
from telethon import TelegramClient 
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InputMediaPhoto

# python3 main.py to start the bot

TOKEN : Final = ""
BOT_USERNAME : Final = ""

async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("Bonjour, je suis moins nul !")

async def start_command_test (update : Update, Context : ContextTypes.DEFAULT_TYPE):
    await update.message.edit_media (
        media =InputMediaPhoto(
            media=open(
                'https://lemagduchat.ouest-france.fr/images/dossiers/2023-06/mini/chat-cinema-061232-650-400.jpg','rb'
                ),
            caption='Title'))
    
async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("Désolé ! J'peux rien faire pour toi !")
    
async def custom_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("C'est tout?")
async def coffee_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text ("Et un café bien chaud !")
    
def handle_response (text: str) -> str:
    processed : str = text.lower()
    
    if "Bonjour" in processed:
            return "Salut toi !"
    if "Comment vas-tu?" in processed:
            return "tranquille!"
    if "Tu t'en sors?" in processed:
            return "Nan c'est la merde!"
    return "JE COMPRENDS RIEEEEEEEEEN"
    
async def handle_message(update: Update, context : ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text
    
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == "group":
        if BOT_USERNAME in text : 
            new_text: str = text.replace(BOT_USERNAME, "").strip ()
            response : str= handle_response (new_text)
        else: 
            return 
    else: 
        response : str = handle_response(text)
    print ('Bot:', response)
    await update.message.reply_text(response)
    
async def error (update: Update, context : ContextTypes.DEFAULT_TYPE):
    print (f"Update {update} caused error {context.error}")
    

if __name__ == "__main__":
    print ("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    
    #Commands
    
    app.add_handler (CommandHandler("start",start_command))
    app.add_handler (CommandHandler("help",help_command))
    app.add_handler(CommandHandler("custom",custom_command))
    app.add_handler(CommandHandler("photo",start_command_test))
    app.add_handler (CommandHandler("coffee",coffee_command))
    # Messages
    
    app.add_handler (MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    print ('Polling...')
    app.run_polling(poll_interval=3)
