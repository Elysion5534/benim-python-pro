import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/help'):
        await message.channel.send("çevre kirliliği nedir,çevremizi kimler kirletmektedir,neden çevremizi korumalıyız,Çevre kirliliğinin sonuçları nelerdir")
    elif message.content.startswith('$çevre kirliliği nedir'):
        await message.channel.send("Çevrenin canlı ögelerinin hayat aktivitelerini olumsuz yönde etkileyen, cansız ögelerin üzerinde ise yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına çevre kirliliği denir.")
    elif message.content.startswith('$çevremizi kimler kirletmektedir'):
        await message.channel.send("İnsanlar kirletmektedir.")
    elif message.content.startswith('$neden çevremizi korumalıyız'):
        await message.channel.send("daha güzel bir dünyada yaşayabilmek için.")
    elif message.content.startswith('$Çevre kirliliğinin sonuçları nelerdir'):
        await message.channel.send("ölümler artar,hastalıklara yol açar,yaşanılmaz bir yer olur,göçler başlayabilir,insanlar ve diğer canlılar kötü kokulardan etkilenebilir,hayvanlar , bitkiler ve diğer canlılar ölebilir")
    else:
        await message.channel.send(message.content)

client.run("token giriniz")
