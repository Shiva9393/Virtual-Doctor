
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Sir")
    else:
        speak("Good Evening! Sir")
    speak("I am Virtual-Doctor. Please tell me how may I help you")

def recognize_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def takeCommand():
    query = recognize_audio().lower()
    return query

def get_age():
    speak("Please specify your age")
    age_input = recognize_audio()
    try:
        age = int(age_input)
        return age
    except ValueError:
        speak("Sorry, I didn't get a valid age. Please try again.")
        return None

if __name__ == "__main__":
    print("Script started")  
    speak("Script started")  
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
      

        elif 'fever' in query:
            age = get_age()
            if age is not None:
                if age <= 10:
                    speak("Sponge bath or soaking in lukewarm water can help in bringing down high fever.")
                else:
                    speak("You can take Dolo 650.")

        elif 'cold' in query:
            speak("Specify whether you would like a natural remedy or an antibiotic")
            query = recognize_audio().lower()
            if 'natural remedy' in query:
                speak("Inhaling steam from a vaporizer device or a bowl of hot water may help.")
            elif 'antibiotic' in query:
                speak("Using medicine like Cetirizine provides relief from cold.")
            else:
                speak("Please specify your query properly.")

        elif 'cough' in query:
            speak("Specify whether you have a dry cough or productive cough")
            query = recognize_audio().lower()
            if 'dry cough' in query:
                speak("Specify whether you need a natural remedy or an antibiotic")
                query = recognize_audio().lower()
                if 'natural remedy' in query:
                    speak("Try adding honey to a cup of warm tea or warm water with lemon. Or just eat a spoonful every time the coughing returns.")
                elif 'antibiotic' in query:
                    speak("Using medicine like Zedex syrup.")
                else:
                    speak("Please specify your query properly.")
            elif 'productive cough' in query:
                speak("Specify whether you need a natural remedy or an antibiotic")
                query = recognize_audio().lower()
                if 'natural remedy' in query:
                    speak("Inhaling steam from a vaporizer device or a bowl of hot water may help.")
                elif 'antibiotic' in query:
                    speak("Using medicine like Ascoril Cough Syrup.")
                else:
                    speak("Please specify your query properly.")

        elif 'headache' in query:
            speak("Specify whether you need a natural remedy or an antibiotic")
            query = recognize_audio().lower()
            if 'natural remedy' in query:
                speak("If you have a headache, place a cold pack on your forehead. Ice cubes wrapped in a towel, a bag of frozen vegetables, or even a cold shower may ease the pain. Keep the compress on your head for 15 minutes, and then take a break for 15 minutes.")
            elif 'antibiotic' in query:
                speak("The medicines for headaches are simple pain relieving medicines. These include paracetamol, aspirin, and non-steroidal anti-inflammatory drugs (NSAIDs) such as ibuprofen. I repeat, the medicines are paracetamol, aspirin, and ibuprofen.")
            else:
                speak("Please specify your query properly.")

        elif 'loose motions' in query or 'diarrhea' in query:
            speak("Specify whether you need a natural remedy or an antibiotic")
            query = recognize_audio().lower()
            if 'natural remedy' in query:
                speak("Drink 8-10 cups of fluid per day, like water, broth, half-strength juice, weak tea, or electrolyte replacement drinks. Eat small frequent meals slowly during the day. Try sources of soluble fiber to help firm up stool. Limit fried or fatty foods since these can worsen diarrhea.")
            elif 'antibiotic' in query:
                speak("Loperamide (Imodium) slows the movement of food through your intestines, which lets your body absorb more liquid, and Bismuth subsalicylate helps in curing loose stools.")
            else:
                speak("Please specify your query properly.")

        elif 'stomach ache' in query:
            speak("Specify whether you need a natural remedy or an antibiotic")
            query = recognize_audio().lower()
            if 'natural remedy' in query:
                speak("The body needs water to efficiently digest and absorb nutrients from foods and beverages. Being dehydrated makes digestion more difficult and less effective, increasing the likelihood of an upset stomach.")
            elif 'antibiotic' in query:
                speak("If bacteria are found to be causing stomach pain. Common antibiotics prescribed for this reason include clarithromycin and metronidazole. I repeat, the medicines are clarithromycin and metronidazole.")
            else:
                speak("Please specify your query properly.")


        

       
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'thank you' in query:
            speak("thank you sir")
            exit
