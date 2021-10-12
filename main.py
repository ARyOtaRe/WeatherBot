import discord
from discord.ext import commands
from datetime import datetime
import requests



client=commands.Bot(command_prefix=commands.when_mentioned_or('MétéoBot:'))
#client.remove_command('help')


@client.command(description='Displays the current weather in a city of your choice',aliases=["crt","now"])
#@commands.is_owner()
async def current(ctx,*,args):
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+ args +"&appid=6e2d2db27e5a42fa384a698d859fc686"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    print(complete_api_link)

    if api_data['cod']=='404':
        embed=discord.Embed(title='The city you\'re trying to get the weather for does not exist!', description='Please check if you made any typos, and then ask about weather in a bigger city around yours', color=0xce2029)
    else:
        temperature=((api_data['main']['temp'])-273.15)
        windspeed=((api_data['wind']['speed'])*3.6)
        city = f'{args}\'' if args[-1]=='s' else f'{args}\'s'
        embed=discord.Embed(title=f'Here is {city.capitalize()} weather right now', description='Reminder that it\'s not always accurate.', color=0xce2029)\
            .add_field(name='Weather description:',value=f"{api_data['weather'][0]['description']}".capitalize(), inline=False)\
            .add_field(name='Average temperature', value=f"{float(temperature):,.2f} °C",inline=False)\
            .add_field(name='Humidity',value=f"{api_data['main']['humidity']}%", inline=False)\
            .add_field(name='Wind speed', value=f"{windspeed:,.2f} m/s", inline=False)

    embed.set_footer(text="Weather Bot | Developed by me")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed)
    #print(city)

<<<<<<< Updated upstream
client.run('ODk3NTI1MDg3MzA0MDQ4Njcx.YWW7YA.T1Uzrpvpb5L6hCKj-vSyb6vObsY')
=======
<<<<<<< HEAD


@client.command(description='Gives you invitation links to add it to your server',aliases=['inv','invitation'])
async def invite(ctx):
    embed=discord.Embed(title="Invitations", description="", color=0xE20088) \
    .add_field(name="Admin invite:", value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=&scope=bot", inline=False) \
    .add_field(name="Normal invite:",value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=4294967287&scope=bot", inline=False) \
    .set_footer(text="Star Wars Archives | Developed by me") \
    .set_author(name="merci pour l'invitation bg!")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 
client.run('NzgzMzQ0NTg2NDA3OTM2MDQw.X8ZYfw.8y5o1mqKTZOynKdLrLMHQc6PoCk')
=======
client.run('ODk3NTI1MDg3MzA0MDQ4Njcx.YWW7YA.T1Uzrpvpb5L6hCKj-vSyb6vObsY')
>>>>>>> f75e5770f79d6c64210a4fc006c93f72ef109bd8
>>>>>>> Stashed changes
