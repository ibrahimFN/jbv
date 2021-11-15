# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/JMTHON >
# Please read the GNU Affero General Public License in;
# < https://www.github.com/JMTHON-AR/LICENSE/blob/LICENSE/LICENSE/ 
# ================================================================

import sys

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import jmthon
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("جمثون")

print(userbot.__copyright__)
print("جميع الحقوق والملفات محفوظة " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info(f"⚒️ يتم تشغيل جمثون")
    jmthon.loop.run_until_complete(setup_bot())
    LOGS.info(f"✅ انتهاء التشغيل ")
 
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


class JmtCheck:
    def __init__(self):
        self.sucess = True


JmtCheck = JmtCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        JmtCheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("--------------------------------------------------------")
    print("تم بنجاح اكتمال تنصيب سورس جمثون المجاني ✓")
    print(" - ارسل  فحص  للتأكد من البوت\n-  ولعرض اوامر السورس ارشل  .الاوامر\n-  للمزيد من المعلومات ادخل الى مجموعتك في التليجرام")
    print("-------------------------------------------------------")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    JmtCheck.sucess = True
    return

jmthon.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
    jmthon.disconnect()
elif not JmtCheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        jmthon.run_until_disconnected()
    except ConnectionError:
        pass
