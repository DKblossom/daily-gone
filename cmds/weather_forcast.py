import discord
from discord.ext import commands
from cmds.core.classes import Cog__Extension
import urllib
import json
import datetime
import asyncio

link = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-7CA3A3ED-9E94-46C3-8083-F9CCD164D4C7"
f = urllib.request.urlopen(link)
myfile = f.read()
embed = discord.Embed


class forcast(Cog__Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def time_task():        
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1007284624969441421)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M%S')
                print(now_time)
                if now_time == "230000":
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                elif now_time == "225500":
                    f = urllib.request.urlopen(link)
                    myfile = f.read()
                    tmp = json.loads(myfile)["records"]["location"][5]["weatherElement"][0]["time"][1]["parameter"]["parameterName"]
                    Url = "0"
                    if "雨" in tmp:
                        Url = "https://upload.cc/i1/2022/08/11/6cq7La.png"
                    elif "晴" in tmp:
                        Url = "https://upload.cc/i1/2022/08/11/J9tj6R.png"
                    else :
                        Url = "https://upload.cc/i1/2022/08/11/jLV5Zs.png"
                    embed=discord.Embed(title="明日天氣預報", description="資料來源：中央氣象局", color=0x9190ea, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                    embed.set_thumbnail(url=Url)
                    embed.add_field(name="最低溫", value=json.loads(myfile)["records"]["location"][5]["weatherElement"][2]["time"][1]["parameter"]["parameterName"]+"°C", inline=True)
                    embed.add_field(name="最高溫", value=json.loads(myfile)["records"]["location"][5]["weatherElement"][4]["time"][1]["parameter"]["parameterName"]+"°C", inline=True)
                    embed.add_field(name="降雨機率", value=json.loads(myfile)["records"]["location"][5]["weatherElement"][1]["time"][1]["parameter"]["parameterName"]+"%", inline=True)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

def setup(bot):
    bot.add_cog(forcast(bot))