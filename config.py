from telethon.sessions import StringSession
from telethon import TelegramClient

# ضع القيم هنا مباشرة
API_ID = 20621590  # ضع الـ API ID هنا (رقم فقط)
API_HASH = "a7e91275d681fefd4b2453b158b254ec"  # ضع الـ API HASH هنا (بين علامتي اقتباس)
BOT_USERNAME = "Bsgsg7s8wbot"  # ضع اسم البوت هنا بدون @
session = "1BJWap1sAUF8B-YYYtte-w_gCT7Ucb4SsqWC--N4wzwERLhYqByU1LPArKt54Mng2IFc-l7Gy1stQonO9RgAns9ZV4-pfjfWkNRA94iQi8dilnRhSz-_18vXFdbkGOx0SkFp6Uvexv6Cm4d2fcu3_UpzRynPLfQZJuCXz1GhbbydEWse8BFXWuL56OGCdNVoR78gG8TiJ1vYgekfRtP-MdjllylT2LDkGu_pYoYnS0qXeAogFzhlkdl-OQtBenR2yYnQ4zX8CVD_5QPh_bD4Q7iReOcyx0xIbbM_HaK-0Pd_C385e-rcLfjj_wlS4ZWLrfAnO5kwEm5fiZsg9ViC-zm9W_1gf36k="  # ضع StringSession هنا (بين علامات اقتباس)
SESSION = "1BJWap1sAUF8B-YYYtte-w_gCT7Ucb4SsqWC--N4wzwERLhYqByU1LPArKt54Mng2IFc-l7Gy1stQonO9RgAns9ZV4-pfjfWkNRA94iQi8dilnRhSz-_18vXFdbkGOx0SkFp6Uvexv6Cm4d2fcu3_UpzRynPLfQZJuCXz1GhbbydEWse8BFXWuL56OGCdNVoR78gG8TiJ1vYgekfRtP-MdjllylT2LDkGu_pYoYnS0qXeAogFzhlkdl-OQtBenR2yYnQ4zX8CVD_5QPh_bD4Q7iReOcyx0xIbbM_HaK-0Pd_C385e-rcLfjj_wlS4ZWLrfAnO5kwEm5fiZsg9ViC-zm9W_1gf36k="  # إذا كان يستخدم في مكان آخر
token = "7657246738:AAEY-NO6KaCWkxod6N33ENvI-bvucpwLXGs"  # ضع توكن البوت من BotFather هنا (بين علامات اقتباس)

Tepthon = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
