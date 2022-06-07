from telethon import events, Button

HELP_PIC = "https://te.legra.ph/file/f07857daaad3426175943.jpg"
Riz_Help = " • Help menu Of XTron • \n\n __Basic Cmds__ \n `/ping` \n `/alive` \n\n __Click On Below Buttons for help__"

@Tron.on(events.NewMessage(pattern="[!/]help"))
async def bot_help(event):
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
       await Tron.send_file(event.chat_id, 
                                HELP_PIC, 
                                caption=Riz_Help, 
                                buttons=[
           [
           Button.url("• SUPPORT •", "https://t.me/cute_chatters"),
           Button.url("• OWNER •", "https://t.me/spa4ky")
           ],
           [
           Button.inline("• Cmds Available •", data="available")
           ],
           ],
           ) 
                   
dm_msg = f"""
** Raid Cmds**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Send Dm Message:** `/dm`

**Start Dm Spam:** `/dmspam`

**Start Dm Raid:** `/dmraid`
"""

joinleave_msg = f"""
**Join Leave Cmds**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Join Group/Channel:** `/join`

**Join Private Group/Channel:** `/pjoin`

**Leave Group/Channels:** `/leave`
"""
           
userbot_msg = f"""
**Userbot Cmds**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Check Ping/uptime**: `/ping`

**Check Alive Version**: `/alive`

**Restart Bots:** `/restart`

**Members adding:** `/scrape`

**Add Sudo**: `/addsudo` 

**Add Full Sudo**: `/fullsudo`
"""

profile_msg = """
**Profile Cmds**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Change Name:** `/setname`

**Change Bio:** `/setbio`
"""

@Tron.on(events.CallbackQuery(pattern=r"help_back"))
async def help_back(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            Riz_Help,
            buttons=[
               [
               Button.inline("• userbot •", data="userbot"),
               Button.inline("• Profile •", data="profile")
               ],
               [
               Button.inline("• Join/Leave •", data="joinleave"),
               Button.inline("• Dm •", data="dm")
               ],
               ],
               )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

           
@Tron.on(events.CallbackQuery(pattern=r"available"))
async def raid_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit("__Click Below Button To Know cmds__",
           buttons=[
               [
               Button.inline("• userbot •", data="userbot"),
               Button.inline("• Profile •", data="profile")
               ],
               [
               Button.inline("• Join/Leave •", data="joinleave"),
               Button.inline("• Dm •", data="dm")
               ],
               ],
               )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)


@Tron.on(events.CallbackQuery(pattern=r"profile"))
async def spam_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            profile_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
 
                  
@Tron.on(events.CallbackQuery(pattern=r"dm"))
async def spam_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            dm_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
                                                        
                                                                
@Tron.on(events.CallbackQuery(pattern=r"joinleave"))
async def raid_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            joinleave_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
            

@Tron.on(events.CallbackQuery(pattern=r"userbot"))
async def userbot_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            userbot_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
                ],
                ],
                )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
