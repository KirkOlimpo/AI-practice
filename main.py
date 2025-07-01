
# GEMINI_API_KEY = "AIzaSyDH1v_lyCHglAQ3hvDAkuvTOZgcFzhoYUA"
# GEMINI_MODEL = "gemini-2.0-flash"


import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyDH1v_lyCHglAQ3hvDAkuvTOZgcFzhoYUA")
model = genai.GenerativeModel('gemini-2.0-flash')

# Initialize TTS
engine = pyttsx3.init()

def speak(text):
    print("🤖 Gemini:", text)
    engine.say(text)
    engine.runAndWait()

def listen(prompt="🎤 Listening...") -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API error: {e}"

# 🔁 Passive listening for wake word
def wait_for_wake_word(wake_word="gemini"):
    while True:
        text = listen("Waiting for wake word...")
        if wake_word in text:
            print("Wake word detected!")
            return

def run_voice_assistant():
    speak("I'm ready. Say 'gemini' to talk.")

    while True:
        wait_for_wake_word()

        speak("Yes? I'm listening.")
        user_input = listen("Say something...")

        if not user_input:
            speak("Sorry, I didn't catch that.")
            continue

        if user_input in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break

        reply = ask_gemini(user_input)
        speak(reply)

        speak("Say 'gemini' again if you need me.")

if __name__ == "__main__":
    run_voice_assistant()
