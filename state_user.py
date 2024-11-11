import time

from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from telethon import events

from telethon.tl.types import Channel, Chat, User
from config import *
from payment import *
from Formater import *


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"\n[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)

STAT_INDICATION = f"**⎉╎جـارِ جـلب الاحصـائيـات إنتظـر ⅏ . . .**"
CHANNELS_STR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع القنـوات** 𓆪\n\n"
CHANNELS_ADMINSTR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع القنـوات اشـراف** 𓆪\n\n"
CHANNELS_OWNERSTR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع القنـوات ملكيـة** 𓆪\n\n"
GROUPS_STR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع المجمـوعـات** 𓆪\n\n"
GROUPS_ADMINSTR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع المجمـوعـات اشـراف** 𓆪\n\n"
GROUPS_OWNERSTR = f"𓆩 **[IEX Multi HUNTER](t.me/ghxxx)** **- 🝢 - احصـائيـات جميـع المجمـوعـات ملكيـة** 𓆪\n\n"

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.احصائياتي"))
async def count(event):
    start_time = time.time()
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("**⪼ جاري المعـالجه ༗.**")
    dialogs = await IEX.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)

    result += f"𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 IEX **- 🝢 - احصـائيـات الحسـاب** 𓆪\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    result += f"**⎉╎المستخدمون :**\t**{u}**\n"
    result += f"**⎉╎المجموعات :**\t**{g}**\n"
    result += f"**⎉╎المجموعات الخارقه :**\t**{c}**\n"
    result += f"**⎉╎القنوات :**\t**{bc}**\n"
    result += f"**⎉╎البوتات :**\t**{b}**\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
    stop_time = time.time() - start_time
    result += f"\n**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"

    await event.edit(result)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.معلوماتي"))
async def stats(event):
    "To get statistics of your telegram account."
    cat = await event.edit(STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 IEX **- 🝢 - معلومات {full_name}** 𓆪\n"
    response += f"**𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻**\n"
    response += f"**- الخـاص :** {private_chats} \n"
    response += f"   ★ **اشخـاص :** `{private_chats - bots}` \n"
    response += f"   ★ **بـوتـات :** `{bots}` \n"
    response += f"**- المجمـوعـات :** {groups} \n"
    response += f"**- القنـوات :** {broadcast_channels} \n"
    response += f"**- ادمـن في مجموعات :** {admin_in_groups} \n"
    response += f"   ★ **مـالك :** `{creator_in_groups}` \n"
    response += f"   ★ **ادمـن : ** `{admin_in_groups - creator_in_groups}` \n"
    response += f"**- ادمـن في قنـوات :** {admin_in_broadcast_channels} \n"
    response += f"   ★ **مـالك :** `{creator_in_channels}` \n"
    response += (
        f"   ★ **ادمـن :** `{admin_in_broadcast_channels - creator_in_channels}` \n"
    )
    response += f"**Unread:** {unread} \n"
    response += f"**Unread Mentions:** {unread_mentions} \n\n"
    response += f"📌**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    await cat.edit(response)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.قنواتي (الكل|ادمن|مالك)"))
async def stats(event):
    catcmd = event.pattern_match.group(1)
    catevent = await event.edit(STAT_INDICATION)
    start_time = time.time()
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.username, entity.id])  # Added username here
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.username, entity.id])  # Added username here
            if entity.creator:
                hico.append([entity.title, entity.username, entity.id])  # Added username here
    if catcmd == "الكل":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Added username here
        caption = CHANNELS_STR
    elif catcmd == "ادمن":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Added username here
        caption = CHANNELS_ADMINSTR
    elif catcmd == "مالك":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Added username here
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    output += f"\n**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption,
        )

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.كروباتي (الكل|ادمن|مالك)"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await event.edit(STAT_INDICATION)
    start_time = time.time()
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            hi.append([entity.title, entity.username, entity.id])  # Added username here
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.username, entity.id])  # Added username here
            if entity.creator:
                higo.append([entity.title, entity.username, entity.id])  # Added username here
    if catcmd == "الكل":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Using username here
        caption = GROUPS_STR
    elif catcmd == "ادمن":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Using username here
        caption = GROUPS_ADMINSTR
    elif catcmd == "مالك":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"I✥┊ {k} ┊ [{i[0]}](https://t.me/c/{i[2]}/1) - @{i[1]}\n"  # Using username here
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    output += f"\n**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption,
        )

