from plugins import ultroid_cmd
from telethon import functions, types,events

HMD = """[ . ππππππ - ππππππππ β .](t.me/Tepthone)\n πβ ββββββ π\n\n - Ψ’ΩΩΩΨ§Ω ΩΨ³ΩΩΩΨ§Ω Ψ¨Ω ΩΩΩ ΩΨ§Ψ¦ΩΩΨ© Ψ£ΩΨ§ΩΩΨ± Ψ§ΩΨ³ΩΩΨ±Ψ³ [Click here|Ψ§ΨΆΨΊΩΨ· ΩΩΩΨ§](https://graph.org/%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B3%D9%88%D8%B1%D8%B3-%D8%AA%D9%8A%D8%A8%D8%AB%D9%88%D9%86-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A-01-11)\n\n"""


@ultroid_cmd(pattern="Ψ§ΩΨ§ΩΨ§ΩΨ±")
async def hi(event):
    await event.edit(f"{HMD}")
