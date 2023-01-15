import discord
from discord.ext import commands
import joguinho
from os import environ


tokenbot = environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents = intents)


bot = commands.Bot(command_prefix='!', help_command=None, intents = intents)

jogos = {}

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    if ctx.content.strip()[0] != '!':
      return

    command = ctx.content.split()

    if command[0] != '!joguinho':
      await ctx.channel.send('sai man bot é pra isso n 😥')
      return

    if command[1] == 'iniciar':
      jogos[ctx.guild.id] = joguinho.Joguinho()
      jogos[ctx.guild.id].iniciar()
      await ctx.channel.send('ii man prepara ai 😲')
      return

    if command[1] == "terminar":
      jogos[ctx.guild.id].resetar()
      await ctx.channel.send('terminou o jogo pq nubao 😡')
      return
    
    resultado = jogos[ctx.guild.id].tentativa(command[1].lower())

    if resultado == joguinho.ERRO:
      await ctx.channel.send('ei man joga direito ai 😤')
      return  

    proximidade = jogos[ctx.guild.id].proximidade.replace("X",":green_square:").replace("O",":yellow_square:").replace("-",":black_large_square:")
    palavra_em_emoji = ''.join(map(lambda x: f':regional_indicator_{x}:', command[1]))
    await ctx.channel.send(palavra_em_emoji)
    await ctx.channel.send(proximidade)
      
    if resultado == joguinho.VITORIA:
      await ctx.channel.send('vose é demais 🥶')
      return  

    if resultado == joguinho.DERROTA:
      await ctx.channel.send('tu é muito ruim !!!!! 🤣')
      return  
  

@bot.event
async def on_ready():
    print(f"Pronto para ligar {bot.user}")

bot.run(tokenbot)