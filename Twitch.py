import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Text to convert to speech
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
text = "Five Nights at Freddy's takes place in a fictional pizza restaurant called Freddy Fazbear's Pizza, where animatronic animals, including Freddy Fazbear, Bonnie the Bunny, Chica the Chicken, and Foxy the Pirate Fox, roam free at night. The player takes on the role of a newly hired security guard who must survive five nights while avoiding being attacked and killed by the animatronics. As the game progresses, it becomes clear that the animatronics have a dark history and are haunted by the ghosts of children who were murdered at the restaurant."

# Convert the text to speech
engine.say(text)

# Play the converted speech
engine.runAndWait()

# from gtts import gTTS
# import os
#
# # Text to convert to speech
# text = "Five Nights at Freddy's takes place in a fictional pizza restaurant called Freddy Fazbear's Pizza, where animatronic animals, including Freddy Fazbear, Bonnie the Bunny, Chica the Chicken, and Foxy the Pirate Fox, roam free at night. The player takes on the role of a newly hired security guard who must survive five nights while avoiding being attacked and killed by the animatronics. As the game progresses, it becomes clear that the animatronics have a dark history and are haunted by the ghosts of children who were murdered at the restaurant."
#
# # Create a gTTS object
# tts = gTTS(text=text, lang='en')
#
# # Save the converted audio to a file
# tts.save("output.mp3")
#
# # Play the audio (Optional)
# os.system("start output.mp3")  # For Windows
