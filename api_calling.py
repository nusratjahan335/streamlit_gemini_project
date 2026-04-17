from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io


#loading env
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#clint 
client= genai.Client(api_key=my_api_key)

#for note
def note_generator(images):
    prompt = """summarize the picture in note formet at most 100 worsd 
    and make sure to markdown diffrent difficultys """
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

def audio(text):
    speech = gTTS(text,lang='en',slow=False)
    speech.save("welcome.mp3")
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_genaretor(images,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty} make sure to add markdown to differentiate the options"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text