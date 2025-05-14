from telethon.sessions import StringSession
from telethon import TelegramClient

# ضع القيم هنا مباشرة
API_ID = 20621590  # ضع الـ API ID هنا (رقم فقط)
API_HASH = "a7e91275d681fefd4b2453b158b254ec"  # ضع الـ API HASH هنا (بين علامتي اقتباس)
BOT_USERNAME = "Bsgsg7s8wbot"  # ضع اسم البوت هنا بدون @
session = "1BJWap1sAUHl2c0e-HMqG0ro9sWUwKxaVE25hgWIFos3_aopztUyGRoR6wQlNZ98YSBTm4Tg8TU0p9BBlJysCFYe5Jt8aYTX1T_aR-V9sUsJFsq0c5HzWb63YtDYgJMKkOA0W-yqkflyGSFZ_fYpljkFt2gK-Id5Nhuzbl5Zt8flVWqsY3S2gKlsYxsnS3gT6A57i3vaD7X8TfGOge9QI49xbo0136dRQ5C5UlSDQjkvD3CA7kiTS1MP-Bt6_CxhaMPh9b6avxN7YWcPNG6FuqX4qQMwPhqG2Wrm4pj1rdI9BSRgAi-UQtFWaaWtTayVHq14vcvm24cbPxim9noBDKxg6eyqSqlw="  # ضع StringSession هنا (بين علامات اقتباس)
SESSION = "1BJWap1sAUHl2c0e-HMqG0ro9sWUwKxaVE25hgWIFos3_aopztUyGRoR6wQlNZ98YSBTm4Tg8TU0p9BBlJysCFYe5Jt8aYTX1T_aR-V9sUsJFsq0c5HzWb63YtDYgJMKkOA0W-yqkflyGSFZ_fYpljkFt2gK-Id5Nhuzbl5Zt8flVWqsY3S2gKlsYxsnS3gT6A57i3vaD7X8TfGOge9QI49xbo0136dRQ5C5UlSDQjkvD3CA7kiTS1MP-Bt6_CxhaMPh9b6avxN7YWcPNG6FuqX4qQMwPhqG2Wrm4pj1rdI9BSRgAi-UQtFWaaWtTayVHq14vcvm24cbPxim9noBDKxg6eyqSqlw="  # إذا كان يستخدم في مكان آخر
token = "7657246738:AAEY-NO6KaCWkxod6N33ENvI-bvucpwLXGs"  # ضع توكن البوت من BotFather هنا (بين علامات اقتباس)

Tepthon = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
