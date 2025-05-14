from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("20621590")
APP_HASH = os.environ.get("a7e91275d681fefd4b2453b158b254ec")
BOT_USERNAME = os.environ.get("Bsgsg7s8wbot")
session = os.environ.get("1BJWap1sAUF8B-YYYtte-w_gCT7Ucb4SsqWC--N4wzwERLhYqByU1LPArKt54Mng2IFc-l7Gy1stQonO9RgAns9ZV4-pfjfWkNRA94iQi8dilnRhSz-_18vXFdbkGOx0SkFp6Uvexv6Cm4d2fcu3_UpzRynPLfQZJuCXz1GhbbydEWse8BFXWuL56OGCdNVoR78gG8TiJ1vYgekfRtP-MdjllylT2LDkGu_pYoYnS0qXeAogFzhlkdl-OQtBenR2yYnQ4zX8CVD_5QPh_bD4Q7iReOcyx0xIbbM_HaK-0Pd_C385e-rcLfjj_wlS4ZWLrfAnO5kwEm5fiZsg9ViC-zm9W_1gf36k=")
SESSION = os.environ.get("1BJWap1sAUF8B-YYYtte-w_gCT7Ucb4SsqWC--N4wzwERLhYqByU1LPArKt54Mng2IFc-l7Gy1stQonO9RgAns9ZV4-pfjfWkNRA94iQi8dilnRhSz-_18vXFdbkGOx0SkFp6Uvexv6Cm4d2fcu3_UpzRynPLfQZJuCXz1GhbbydEWse8BFXWuL56OGCdNVoR78gG8TiJ1vYgekfRtP-MdjllylT2LDkGu_pYoYnS0qXeAogFzhlkdl-OQtBenR2yYnQ4zX8CVD_5QPh_bD4Q7iReOcyx0xIbbM_HaK-0Pd_C385e-rcLfjj_wlS4ZWLrfAnO5kwEm5fiZsg9ViC-zm9W_1gf36k=")
token = os.environ.get("7657246738:AAEY-NO6KaCWkxod6N33ENvI-bvucpwLXGs")
Tepthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

