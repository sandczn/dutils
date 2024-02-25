


# developed by formik#0001
import json
import discord, datetime, asyncio
import re
import time, os
import random



dutils_version_num = "12.71.2"
dutils_version = "v" + dutils_version_num
configf = open('./config.json', 'r+', encoding='utf-8')
config = json.load(configf)
token = open(config["token_file_path"], 'r', encoding='utf-8').read()
amount = config["amount"]
msg = open(config["message_file_path"], 'r', encoding='utf-8').read()
log_messages = config["log_messages"]
log_channels = config["log_channels"]
announce = config["announce"]
clear = config["clear"]
prefix = config["prefix"]
post_clear_msg = open(config["post_clear_message_file_path"], 'r', encoding='utf-8').read()
wall = open(config["wall_file_path"], 'r').read()
patch_notes = open(f"./dutils-{dutils_version_num}-patch.txt", 'r', encoding='utf-8').read()

blackcheat = False
bleed_id = 593921296224747521
blackcheat_config = config["blackcheat"]
blackcheat_words = open(blackcheat_config['words_list_file_path'], 'r', encoding='utf-8') # Make sure the word list in in the same directory as the py file
blackcheat_lines = blackcheat_words.readlines()
blackcheat_version = 2.26
used = []
active_guilds = []

def blackcheat_title():
	print(f"\n\n\t\tBLACKCHEAT BY FORMIK, DEADLY, & BENITAS\n\t\t\tVERSION\t{blackcheat_version}\n\n")


class rpc:
	active = config["rpc"]["active"]
	name = config["rpc"]["name"]
	url = config["rpc"]["url"]






help_msg = f"""```
					Available Commands:
					``` ```
					{prefix}help -> Prints this menu

					{prefix}wall -> Spams walls to the text channel

					{prefix}spam -> Spams the provided message to the text channel

					{prefix}term -> Terminate the current process

					{prefix}cls -> Purges user messages (Only works in Regular Text Channels)

					{prefix}log.start -> Enable the message logger

					{prefix}log.stop -> Disable the message logger

					{prefix}log.add -> Add the current channel to the message logger target list 

					{prefix}log.remove -> Remove the current channel from the message logger target list

					{prefix}clear.true -> Enable Clear setting
					
					{prefix}clear.false -> Disable Clear setting

					{prefix}announce.true -> Enable Announce setting
					
					{prefix}announce.false -> Disable Announce setting

					{prefix}prefix.set -> Set new prefix

					{prefix}console.cls -> Clear the console

					{prefix}credit -> Display credit
					
					{prefix}verion -> Display version
					
					{prefix}info -> Display all information about dutils
					
					{prefix}patch -> Patch notes

					{prefix}blackcheat.true -> Enable BLACKCHEAT (BlackTea Cheat)

					{prefix}blackcheat.false -> Disable BLACKCHEAT (BlackTea Cheat)
					```"""



patch_msg = f"""```
{patch_notes}
```"""


info_msg = f"""```
					dutils Info:
					``` ```
					Current Version: {dutils_version}
					Developer: formik, deadly, benitas
```"""

credit_msg = f"""```
					dutils (Discord Utilities)
					developed by formik, deadly, benitas
```"""

version_msg = f"""```
					Current dutils Version: {dutils_version}
```"""

client = discord.Client()
	
def cls():
	cmd = "cls" if os.name == "nt" else "clear"
	os.system(cmd)

async def evaluate(message):
	global dutils_version, configf, config, token, amount, msg, log_messages, log_channels, announce, clear, prefix, post_clear_msg, wall, blackcheat, bleed_id, blackcheat_config, blackcheat_words, blackcheat_lines, blackcheat_version, used, active_guilds, help_msg, patch_notes, info_msg, credit_msg, version_msg 

	if message.author != client.user:
		return
	#cls()

	
	if f"{prefix}term" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		exit()
		return
	elif f"{prefix}wall" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		for i in range(amount):
			try:
				await message.channel.send(wall)
			except:
				exit()
		return
	elif f"{prefix}spam" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		for i in range(amount):
			try:
				await message.channel.send(msg)
			except:
				exit()
		return
	elif f"{prefix}cls" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.purge(limit=200, check=lambda message: message.author == message.author)
		if (len(post_clear_msg) > 0) and (post_clear_msg != None):
			await message.channel.send(post_clear_msg)
		return
	elif f"{prefix}help" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(help_msg)
		await message.channel.send(help_msg)
		return
	elif f"{prefix}info" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.send(info_msg)
		return
	elif f"{prefix}patch" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(patch_msg)
		await message.channel.send(patch_msg)
		return
	elif f"{prefix}version" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(version_msg)
		await message.channel.send(version_msg)
		return
	elif f"{prefix}credit" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(credit_msg)
		await message.channel.send(credit_msg)
		return
	elif f"{prefix}log.start" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		log_messages = True
		log_channels.append(message.channel.id)
		print("\nMessage Logger has been enabled for this session.\n")
		if announce:
			await message.channel.send("```Message Logger has been enabled for this session.```")
		return
	elif f"{prefix}log.stop" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print("\nMessage Logger has been disabled for this session.\n")
		if announce:
			await message.channel.send("```Message Logger has been disabled for this session.```")
		return
	elif f"{prefix}log.add" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		log_messages = True
		log_channels.append(message.channel.id)
		print(f"\nMessage Logger has been enabled for channel '{message.channel.name}' ({message.channel.id}) in guild '{message.guild.name}' ({message.guild.id}) for this session.\n")
		if announce:
			await message.channel.send("```Message Logger has been enabled for this channel for this session.```")
		return
	elif f"{prefix}log.remove" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print(f"\nMessage Logger has been disabled for channel '{message.channel.name}' ({message.channel.id}) in guild '{message.guild.name}' ({message.guild.id}) for this session.\n")
		if announce:
			await message.channel.send("```Message Logger has been disabled for this channel for this session.```")
		return
	elif f"{prefix}clear.true" in message.content.lower() and "available commands:" not in message.content.lower():
		clear = True
		if clear:
			await message.delete()
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print("\nClear has been enabled for this session.\n")
		if announce:
			await message.channel.send("```Clear has been enabled for this session.```")
		return
	elif f"{prefix}clear.false" in message.content.lower() and "available commands:" not in message.content.lower():
		clear = False
		if clear:
			await message.delete()
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print("\nClear has been disabled for this session.\n")
		if announce:
			await message.channel.send("```Clear has been disabled for this session.```")
		return
	elif f"{prefix}announce.true" in message.content.lower() and "available commands:" not in message.content.lower():
		announce = True
		if clear:
			await message.delete()
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print("\nAnnounce has been enabled for this session.\n")
		if announce:
			await message.channel.send("```Announce has been enabled for this session.```")
		return
	elif f"{prefix}announce.false" in message.content.lower() and "available commands:" not in message.content.lower():
		announce = False
		if clear:
			await message.delete()
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		print("\nAnnounce has been disabled for this session.\n")
		if announce:
			await message.channel.send("```Announce has been disabled for this session.```")
		return
	elif f"{prefix}prefix.set" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		argv = message.content.lower().split(" ")
		if len(argv) == 1:
			pass
		else:
			new = argv[1]
			prefix = new
			print(f"\nPrefix has been set to '{new}' for this session.\n")
			if announce:
				await message.channel.send(f"```Prefix has been set to '{prefix}' for this session.```")
	elif f"{prefix}console.cls" in message.content.lower() and "available commands:" not in message.content.lower():
		cls()
		if clear:
			await message.delete()
		print(f"\nConsole has been cleared.\n")
	elif f"{prefix}blackcheat.true" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		blackcheat = True
		print(f"\nBlackcheat has been enabled for this session.\n")
		if announce:
			await message.channel.send(f"```Blackcheat has been enabled for this session.```")
		
	elif f"{prefix}blackcheat.false" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		blackcheat = False		
		print(f"\nBlackcheat has been disabled for this session.\n")
		if announce:
			await message.channel.send(f"```Blackcheat has been disabled for this session.```")
	else:
		return

@client.event
async def on_ready():
	if rpc.active:
		# for dev: https://discordpy.readthedocs.io/en/stable/api.html#discord.Activity
		await client.change_presence(activity=discord.Streaming(name=rpc.name, url=rpc.url))
	print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	global dutils_version, configf, config, token, amount, msg, log_messages, log_channels, announce, clear, prefix, post_clear_msg, wall, blackcheat, bleed_id, blackcheat_config, blackcheat_words, blackcheat_lines, blackcheat_version, used, active_guilds, help_msg, patch_notes, info_msg, credit_msg, version_msg 

	# blackcheat (start)
	if blackcheat: # and (message.channel.guild.id in active_guilds):
		if client.user.mentioned_in(message) == False: # Only try to answer if bleed actually mentions you
			if message.author != client.user:
				return
			else:
				await evaluate(message)
		if blackcheat == False:
			return
		if message.author.id != bleed_id: # Check if the message is from bleed and in the current server
			return
		if len(message.embeds) == 0: # Check if the message is an embed message
			return

		cls()
		embedText = message.embeds[0].description
		regexSearch = re.search("Type a \*\*word\*\* containing the letters: \*\*(.{3})\*\*.", embedText) # Fetch the letters that need to be contained in the word
		if bool(regexSearch) == False or blackcheat == False:
			return
		startingLetters = regexSearch[1]
		blackcheat_title()
		print("\n\tStarting Letters Found\t:\t" + startingLetters)
		answerText = "null"
		for line in blackcheat_lines:
			if (startingLetters.lower() in line) and (line not in used) and (len(line) <= blackcheat_config["wlencap"]): # Find a word that contains the starting letters
				answerText = line
				used.append(line)
				break
		print("\tAnswer Found\t\t:\t" + answerText)
		pause = random.choice(blackcheat_config["pauses"])
		print(f"\tSleeping for realism\t:\t{pause}\tseconds")
		time.sleep(pause)
		await message.channel.send(answerText) # Send the answer in chat
	else:
		if message.author != client.user:
			return
		#cls()
		await evaluate(message)


@client.event
async def on_message_delete(message):
	if (log_messages == True) and (message.channel.id in log_channels):
		print(f"""

		===================================================================================================================
		
		Deleted message logged at {datetime.datetime.now()}:
		Author\t\t:\t{message.author.name}#{message.author.discriminator}\t\t\t(ID:{message.author.id})
		Server\t\t:\t{message.guild.name}\t\t\t(ID:{message.guild.id})
		Channel\t\t:\t{message.channel.name}\t\t\t(ID:{message.channel.id})
		Message\t\t:\t{message.content}

		===================================================================================================================
		
		""")


if config["looped_client"]:
	while True:
		cls()
		print("\nStarting client...\n")
		try:
			print(f"""

					dutils {dutils_version}
					developed by formik, deadly, benitas

			> Type {prefix}help in a text channel to get started.

			""")


			client.run(token)
		except Exception as e:
			continue
		else:
			continue
else:
	cls()
	print("\nStarting client...\n")
	print(f"""

			dutils {dutils_version}
			developed by formik, deadly, benitas

	> Type {prefix}help in a text channel to get started.

	""")

	client.run(token)













