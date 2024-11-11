import asyncio
import os
from bs4 import BeautifulSoup
from markdown import markdown
import json
import requests
from config import * 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}


async def p_paste(message, extension=None):
    """
    To Paste the given message/text/code to paste.pelkum.dev
    """
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Unable to reach pasty.lus.pm"}


async def s_paste(message, extension="txt"):
    """
    To Paste the given message/text/code to spaceb.in
    """
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        response = requests.post(
            siteurl, data={"content": message, "extension": extension}
        )
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        if response["error"] != "" and response["status"] < 400:
            return {"error": response["error"]}
        return {
            "url": f"https://spaceb.in/{response['payload']['id']}",
            "raw": f"{siteurl}{response['payload']['id']}/raw",
            "bin": "Spacebin",
        }
    return {"error": "Unable to reach spacebin."}


def spaste(message, extension="txt"):
    """
    To Paste the given message/text/code to spaceb.in
    """
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        response = requests.post(
            siteurl, data={"content": message, "extension": extension}
        )
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        if response["error"] != "" and response["status"] < 400:
            return {"error": response["error"]}
        return {
            "url": f"https://spaceb.in/{response['payload']['id']}",
            "raw": f"{siteurl}{response['payload']['id']}/raw",
            "bin": "Spacebin",
        }
    return {"error": "Unable to reach spacebin."}


async def n_paste(message, extension=None):
    """
    To Paste the given message/text/code to nekobin
    """
    siteurl = "https://nekobin.com/api/documents"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"nekobin.com/{response['result']['key']}.{extension}"
            if extension
            else f"nekobin.com/{response['result']['key']}"
        )
        return {
            "url": purl,
            "raw": f"nekobin.com/raw/{response['result']['key']}",
            "bin": "Neko",
        }
    return {"error": "Unable to reach nekobin."}


async def d_paste(message, extension=None):
    """
    To Paste the given message/text/code to dogbin
    """
    siteurl = "http://catbin.up.railway.app/documents"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"http://catbin.up.railway.app/{response['key']}.{extension}"
            if extension
            else f"http://catbin.up.railway.app/{response['key']}"
        )
        return {
            "url": purl,
            "raw": f"http://catbin.up.railway.app/raw/{response['key']}",
            "bin": "Dog",
        }
    return {"error": "Unable to reach dogbin."}


async def pastetext(text_to_print, pastetype=None, extension=None):
    response = {"error": "something went wrong"}
    if pastetype is not None:
        if pastetype == "p":
            response = await p_paste(text_to_print, extension)
        elif pastetype == "s" and extension:
            response = await s_paste(text_to_print, extension)
        elif pastetype == "s":
            response = await s_paste(text_to_print)
        elif pastetype == "d":
            response = await d_paste(text_to_print, extension)
        elif pastetype == "n":
            response = await n_paste(text_to_print, extension)
    if "error" in response:
        response = await p_paste(text_to_print, extension)
    if "error" in response:
        response = await n_paste(text_to_print, extension)
    if "error" in response:
        if extension:
            response = await s_paste(text_to_print, extension)
        else:
            response = await s_paste(text_to_print)
    if "error" in response:
        response = await d_paste(text_to_print, extension)
    return response















async def paste_message(text, pastetype="p", extension=None, markdown=True):
    if markdown:
        text = md_to_text(text)
    response = await pastetext(text, pastetype, extension)
    if "url" in response:
        return response["url"]
    return "Error while pasting text to site"

def md_to_text(md):
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()

#======================================================================================
async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    deflink=False,
    noformat=False,
    linktext=None,
    caption=None,
):
    sudo_users = {}
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096 and not deflink:
        parse_mode = parse_mode or "md"
        if event.sender_id in sudo_users:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    if not noformat:
        text = md_to_text(text)
    if aslink or deflink:
        linktext = linktext or "الرسالة كبيرة تم لصقها بصفحه ويب خاصه بك"
        response = await paste_message(text, pastetype="s")
        text = f"{linktext} [اضغط هنا]({response})"
        if event.sender_id:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        await event.edit(text, link_preview=link_preview)
        return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)


async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    sudo_users = {}
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in sudo_users:
        reply_to = await event.get_reply_message()
        zedevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        zedevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await zedevent.delete()
