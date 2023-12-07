from chat_downloader import ChatDownloader
import google_LLM
import playsound
import asyncio
import edge_tts
import time
import google_translate

url = 'youtube channel'

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
    # if(not ask.encode('UTF-8').isalpha()):
        # ask = google_translate.translate_en(ask)
        # print(f'question translate to en : {ask}')
    # response = LLM.model(ask)

    ask = google_translate.translate_en(ask)
    print(f'translate ask : {ask}')
    response = google_LLM.model(ask)
    if(response is None):
        response = 'Please ask again'
    # response  = google_translate.translate_en(response)
    # response = str(response)
    # print(f'translate response : {response}')

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
            chat = ChatDownloader().get_chat(url,timeout=1)       # create a generator
            # chat = ChatDownloader().get_chat(url)       # create a generator
            isMessage = False
        
            for message in chat:                        # iterate over messages
                # print('message: ',message['message'])
                isMessage = True
                # if(time.time() - start > 1):
                #     break
        except:
            print('error')
            pass
        if(isMessage == False):
            # print('Wait to Start')
            continue
        ask = message['message']
        if(ask == past_message):
            # print('wait')
            time.sleep(1)
            continue
        else:
            past_message = ask
            print('\nAsk: ', ask)

        # msg += (ask + ' \n')
        # while(len(ask) > 1000):
        #     msg = msg[50:]

        response = run(ask)
        # response = run(msg)
        # msg += (response + ' \n')
        
    print('history: ')
    print(msg)
    loop.close()
    