# Rocks Verification Bot Property Of Rocks
# Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


async def MakeCaptchaMarkup(markup, __emoji, indicator):
    __markup = markup
    for i in markup:
        for k in i:
            if k["text"] == __emoji:
                k["text"] = f"{indicator}"
                k["callback_data"] = "HeHe"
                return __markup
