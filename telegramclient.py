from telethon import TelegramClient, sync
import sys
import socks
from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.errors import FloodWaitError, RPCError
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
import datetime
import csv

api_id = ******
api_hash = '************************'
client = TelegramClient('season',  api_id, api_hash,  proxy=(socks.SOCKS5, 'localhost', ****)).start()

# me = client.get_me()
# print(me.stringify())
# client.send_message('me', 'Hello World from Telethon!')
# Sending a file
#client.send_file('me', '/home/myself/Pictures/holidays.jpg')

 
channel_entity=client.get_entity('your channel')#


with open('outputtelegram.csv',mode='w', newline='', encoding='utf-16') as outputfile:
    filewriter =csv.writer(outputfile,delimiter=',',quotechar=' ',quoting=csv.QUOTE_ALL)
    result=client(GetHistoryRequest(
        peer=channel_entity,
        offset_id=0,
        offset_date=datetime.datetime(2019,7,5),
        add_offset=0,
        limit=3000,
        max_id=0,
        min_id=0,
        hash=0
    ))
    for res in result.messages:
        if res.message is not None:
            filewriter.writerow([  str(res.date.year), str(res.date.month), str(res.date.day), res.message])
