from telethon import events, Button, types
from XTron.event import *


@Tron.on(events.NewMessage(pattern="^[?!/]pinned"))
async def get_pinned(event):
  if event.is_group:
     chat_id = (str(event.chat_id)).replace("-100", "")
     Ok = await Tron.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
     tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
     await event.reply(tem, parse_mode="html", link_preview=False)

@Tron.on(events.NewMessage(pattern="^[!?/]pin ?(.*)"))
@is_admin
async def pin(event, perm):
   if event.is_group:
       if not perm.pin_messages:
          await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
          return
       msg = await event.get_reply_message()
       if not msg:
          await event.reply("Reply to a msg to pin it!")
          return
       input_str = event.pattern_match.group(1)
       if "notify" in input_str:
          await Tron.pin_message(event.chat_id, msg, notify=True)
          return
       await Tron.pin_message(event.chat_id, msg)   

@Tron.on(events.NewMessage(pattern="^[!?/]unpin ?(.*)"))
@is_admin
async def unpin(event, perm):
   if event.is_group:
       if not perm.pin_messages:
          await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
          return
       chat_id = (str(event.chat_id)).replace("-100", "")
       ok = await Tron.get_messages(event.chat_id, ids=types.InputMessagePinned())
       await Tron.unpin_message(event.chat_id, ok)
       await event.reply(f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.", link_preview=False)

@Tron.on(events.NewMessage(pattern="^[!?/]permapin"))
@is_admin
async def permapin(event, perm):
   if event.is_group:
       if not perm.pin_messages:
          await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
          return
       msg = await event.get_reply_message()
       if not msg:
          await event.reply("Reply to a msg to permapin it.")
          return
       hn = await Tron.send_message(event.chat_id, msg.message)
       await Tron.pin_message(event.chat_id, hn, notify=True)


@Tron.on(events.NewMessage(pattern="^[!?/]unpinall"))
async def unpinall(event, perm):
   if event.is_group:
       if not perm.pin_messages:
          await event.reply("You are missing the following rights to use this command:CanPinMsgs!")
          return
       UNPINALL = """
Are you sure you want to 
unpin all msgs?
This action can't be undone!
"""

       await Tron.send_message(event.chat_id, UNPINALL, buttons=[
       [Button.inline("Confirm", data="unpin")], 
       [Button.inline("Cancel", data="cancel")]])


@Tron.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await Tron.unpin_message(event.chat_id)
        await event.edit("Unpinned All Msgs!")
        return 

    await event.answer("Group Creator Required!")

@Tron.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("Unpinning of all msgs has been cancelled!")
        return 

    await event.answer("Group Creator Required!")

