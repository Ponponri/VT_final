from googletrans import Translator


def translate_en(text_to_translate):
    translator = Translator()

    # text_to_translate = "我是誰?"

    translation = translator.translate(text_to_translate, dest='en')

    # print(f"Translated Text: {translation.text}")
    # print(f"Source Language: {translation.src}")
    # print(f"Destination Language: {translation.dest}")

    return translation.text


if __name__ == '__main__':
    while(True):
        ask = input('input:')
        if(ask == 'q'):
            print('quit')
            break
        print('isAlpha:',ask.encode('UTF-8').isalpha())

        responese = translate_en(ask)

        print(f'respones: {responese}')