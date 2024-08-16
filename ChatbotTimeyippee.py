import boto3
import json
import pyttsx3
import time
import pygame
import speech_recognition as sr

engine = pyttsx3.init()
client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
modelId = 'meta.llama3-8b-instruct-v1:0'
pygame.mixer.init()
smartstuffidk=[]
while True:
    max_idiot_counter=3
    user_message = ''
    while not user_message:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            my_sound = pygame.mixer.Sound(r'C:\Users\WinstonBai\PycharmProjects\pythonProject2\megalovania-first-four-notes (1) (1).mp3')
            my_sound.play()
            audio = r.listen(source, timeout=2000)

            # ASR
            t0 = time.time()
            try:
                user_message = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said " + user_message)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            print(f'Time taken: {time.time() - t0} seconds')

            if user_message:
                if user_message.lower() == "super secret exit command":
                    print("Ciao~")
                    die_sound = pygame.mixer.Sound(r'tactical-nuke.mp3')
                    die_sound.play()
                    time.sleep(10)
                    exit()
                break

            max_idiot_counter -= 1
            if max_idiot_counter == 0:
                print("You are an idiot L bozo")
                idiot_sound = pygame.mixer.Sound(r'Circus-Theme-Entry-of-the-Gladiators-Ragtime-Version(chosic.com).mp3')
                idiot_sound.play()
                time.sleep(151.5)
                exit()

    # LLM

    me_message ={"role": "user","content": [{"text": user_message}],}
    smartstuffidk.append(me_message)
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=modelId,
        messages=smartstuffidk,
        inferenceConfig={"maxTokens":512,"temperature":0.5,"topP":0.9},
        additionalModelRequestFields={}
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    you_message ={"role": "assistant","content": [{"text": response_text}],}
    smartstuffidk.append(you_message)
    print(response_text)

    # TTS
    engine.say(response_text)
    engine.runAndWait()
