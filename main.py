import discord
from discord.ext import commands
from datetime import datetime
import requests



client=commands.Bot(command_prefix=commands.when_mentioned_or('MétéoBot:'))
#client.remove_command('help')


@client.command(description='Montre la météo dans la ville de ton choix',aliases=["crt","now"])
async def current(ctx,*,args):
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+ args +"&appid=6e2d2db27e5a42fa384a698d859fc686"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    print(complete_api_link)

    if api_data['cod']=='404':
        embed=discord.Embed(title='La ville pour laquelle tu recherche la météo n\'existe pas!', description='STP vérifie que tu n\'aies pas fait de fautes d\'orthographe... Et au pire prends la grande ville la plus proche', color=0xce2029)
    else:
        temperature=((api_data['main']['temp'])-273.15)
        windspeed=((api_data['wind']['speed'])*3.6)
        #city = f'{args}\'' if args[-1]=='s' else f'{args}\'s'
        embed=discord.Embed(title=f'La météo de {args.capitalize()} en ce moment', description='C\'est pas toujours vraiment le cas, la météo c\'est pas tjrs ça', color=0xce2029)\
            .add_field(name='Description :',value=f"{api_data['weather'][0]['description']}".capitalize(), inline=False)\
            .add_field(name='Température moyenne :', value=f"{float(temperature):,.2f} °C",inline=False)\
            .add_field(name='Humidité',value=f"{api_data['main']['humidity']}%", inline=False)\
            .add_field(name='Vitesse du vent', value=f"{windspeed:,.2f} m/s", inline=False)

    embed.set_footer(text="MétéoBot | Developed by your")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed)
    #print(city)

@client.command(description='Te donne les liens d\'invitation pour m\'ajouter à ton serveur',aliases=['inv','invitation'])
async def inviter(ctx):
    embed=discord.Embed(title="Invitations", description="", color=0xE20088) \
    .add_field(name="invitation admin:", value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=&scope=bot", inline=False) \
    .add_field(name="invitation normale:",value="https://discord.com/api/oauth2/authorize?client_id=897525087304048671&permissions=4294967287&scope=bot", inline=False) \
    .set_footer(text="MétéoBot | Développé par moi") \
    .set_author(name="merci pour l'invitation bg!")
    embed.timestamp=datetime.now()
    await ctx.send(embed=embed) 

@client.command()
@commands.is_owner()
async def squarfiuz(ctx):
    await ctx.send('Sah quel BG')

client.run('ODk3NTI1MDg3MzA0MDQ4Njcx.YWW7YA.T1Uzrpvpb5L6hCKj-vSyb6vObsY')

