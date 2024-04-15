# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta pic: https://te.legra.ph/file/7772a7dae6290f0a612a6.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Bull.jpg

import random
from .. import loader, utils
from ..inline.types import InlineCall
from ..inline.types import InlineQuery



bull1r = (
                "Пися",
                "Байден",
                "Томат",
                
            )

def bull1me():
    iwfy = random.choice(bull1r)
    return iwfy
     
@loader.tds
class Bull1Mod(loader.Module):
    """Bull1 пиз#а собеседнику"""

    strings = {"name": "BullMod"}
    
    @loader.inline_everyone
    async def bull1_inline_handler(self, query: InlineQuery):
        """Забулить кого-то жесткими матами про мать"""
        aoa = bull1me()
        
        btn_a = [{"text": "🌀 Random", "callback": self.bull1s}]

        return {
            "title": "Пошутить про маму",
            "thumb": "https://te.legra.ph/file/b2a6c8d20e0034a534ac4.jpg",
            "description": "Отправить...",
            "message": f"<i>{aoa}</i>",
            "reply_markup": btn_a,
        }
    
    async def bull1cmd(self, message):
        """Забулить кого-то жесткими матами про мать"""  
        aoa = bull1me()
        await utils.answer(message, aoa)
    
    async def bull1icmd(self, message):
        """Забулить кого-то жесткими матами про мать (inline)""" 
        aoa = bull1me()
        await self.inline.form(
            message=message,
            text=aoa,
            reply_markup=[
                [{"text": "🌀 Random", "callback": self.bull1s}],
            ]
        )
