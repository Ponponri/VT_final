from chat_downloader import ChatDownloader
import google_LLM
import playsound
import edge_tts
import google_translate

import asyncio
import time
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--channel', type=str)
parser.add_argument('--token', type=str)
args = parser.parse_args()

# url = args.channel
url = 'https://www.youtube.com/watch?v=Dm5k0fx0YCg&ab_channel=Ponponri'
token = args.token

# VOICE = "zh-TW-HsiaoChenNeural"
VOICE = "en-US-JennyNeural"
OUTPUT_FILE = "test.mp3"
# PITCH= "+20Hz" 
# PITCH= "+30Hz" 
PITCH= "+40Hz" 
RATE="-15%" 

async def amain(TEXT) -> None:
    communicate = edge_tts.Communicate(text=TEXT, voice=VOICE,pitch=PITCH,rate=RATE)
    await communicate.save(OUTPUT_FILE)

def run(ask):
    ask = google_translate.translate_en(ask)
    print(f'translate ask : {ask}')
    response = google_LLM.model(ask, token)
    if(response is None):
        response = 'Please ask again'

    print('Respones: ',response)
    with open('text.txt', 'w+', encoding='UTF-8') as f:
        f.write(response)

    with open('text.txt','r', encoding='UTF-8') as f:
        TEXT = f.read()

    loop.run_until_complete(amain(response))
    playsound.playsound(OUTPUT_FILE, True)
    return response

if __name__ == '__main__':
    out_file = './message.json'
    with open(out_file,'w+') as f:
        pass 
    msg = ''
    loop = asyncio.get_event_loop_policy().get_event_loop()
    past_message = ''
    print('Start')
    while(True):
        try:
            start = time.time()
            chat = ChatDownloader().get_chat(url,timeout=1) 
            isMessage = False
            for message in chat:
                isMessage = True

        except:
            print('error')
            continue
        
        if(isMessage == False):
            continue
        ask = message['message']
        if(ask == past_message):
            time.sleep(1)
            continue
        else:
            past_message = ask
            print('\nAsk: ', ask)
        response = run(ask)
