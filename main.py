import discord
from discord.ext import commands
from datetime import datetime
import requests



client=commands.Bot(command_prefix=commands.when_mentioned_or('Weather:'))
client.remove_command('help')


@client.command()
async def current(ctx,*,args):
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+ args +"&appid=6e2d2db27e5a42fa384a698d859fc686"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()

    if api_data['cod']=='404':
        embed=discord.Embed(title='The city you\'re trying to get the weather from does not exist!', description='Please check if you made any typos, and then ask about weather in a bigger city around yours', color=0xce2029)\

    else:
        temperature=((api_data['main']['temp'])-273.15)
        windspeed=((api_data['wind']['speed'])*3.6)
        embed=discord.Embed(title=f'Here is {args}\'s weather right now', description='Reminder that it\'s not always accurate, pls no bully me', color=0xce2029)\
            .add_field(name='Weather description:',value=f"{api_data['weather'][0]['description']}", inline=False)\
            .add_field(name='Average temperature', value=f"{float(temperature):,.2f} °C",inline=False)\
            .add_field(name='Humidity',value=f"{api_data['main']['humidity']}%", inline=False)\
            .add_field(name='Wind speed', value=f"{windspeed:,.2f} m/s", inline=False)

    embed.set_footer(text="Weather Bot | Developed by me")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 

client.run('NzgzMzQ0NTg2NDA3OTM2MDQw.X8ZYfw.8y5o1mqKTZOynKdLrLMHQc6PoCk') 