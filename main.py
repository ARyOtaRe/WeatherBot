import discord
from discord.ext import commands
from datetime import datetime
import requests



client=commands.Bot(command_prefix=commands.when_mentioned_or('WeatherBot:'))

@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return 

@client.command(description='Shows the weather information of the city of your choice!',aliases=["crt","now"])
async def current(ctx,*,args):
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+ args +"&appid="
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    print(complete_api_link)

    if api_data['cod']=='404':
        embed=discord.Embed(title='The city you\'re trying to get the weather from does not exist!', description='Please check if you\'ve made any typo, or get the weather from the closest city :)', color=0xce2029)
    else:
        temperature=((api_data['main']['temp'])-273.15)
        windspeed=((api_data['wind']['speed'])*3.6)
        city = f'{args}\'' if args[-1]=='s' else f'{args}\'s'
        fahr=9.0/5.0 * temperature + 32
        embed=discord.Embed(title=f'{city.capitalize()} right now', description='It\'s not always the case, keep that in mind', color=0xce2029)\
            .add_field(name='Description :',value=f"{api_data['weather'][0]['description']}".capitalize(), inline=False)\
            .add_field(name='Average temperature :', value=f"{float(temperature):,.2f} °C/{fahr:,.0f} °F ",inline=False)\
            .add_field(name='Average humidity',value=f"{api_data['main']['humidity']}%", inline=False)\
            .add_field(name='Wind speed', value=f"{windspeed:,.2f} m/s", inline=False)

    embed.set_footer(text="WeatherBot | Developed by your fav dev")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed)
    #print(city)

@client.command(description='Gives you the invite links',aliases=['inv','invitation'])
async def invite(ctx):
    embed=discord.Embed(title="Invites", description="", color=0xE20088) \
    .add_field(name="Admin invite:", value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=&scope=bot", inline=False) \
    .add_field(name="Normal invite:",value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=4294967287&scope=bot", inline=False) \
    .set_footer(text="MétéoBot | Developped by your fav dev") \
    .set_author(name="Thanks for inviting me!")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 


client.run('bot_token')

