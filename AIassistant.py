import speech_recognition as sr
import pyttsx3
import openai
from datetime import datetime
import random

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key_here'

# Function to get the current date and time as a string
def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to generate a random fact
def get_random_fact():
    facts = [
        "Did you know? Honey never spoils.",
        "A day on Venus is longer than a year on Venus.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not."
    ]
    return random.choice(facts)

# Function to generate a random joke
def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why don’t skeletons fight each other? They don’t have the guts."
    ]
    return random.choice(jokes)

# Function to query OpenAI GPT-4 for general questions
def query_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Sorry, I couldn't retrieve the answer. Error: {str(e)}"

# Function to respond to the recognized speech
def respond(phrase):
    if phrase == "":
        response = "I can't hear you, try again."
    elif "hello" in phrase.lower():
        response = "Hello! How can I assist you today?"
    elif "today" in phrase.lower():
        response = f"Today's date and time is {get_current_datetime()}."
    elif "fact" in phrase.lower():
        response = get_random_fact()
    elif "joke" in phrase.lower():
        response = get_random_joke()
    elif "how are you" in phrase.lower():
        response = "I'm just a computer program, so I don't have feelings, but thanks for asking!"
    elif "exit" in phrase.lower():
        response = "Goodbye!"
    else:
        # Use OpenAI to answer the question
        response = query_openai(phrase)
    
    return response

# Main function to run the voice assistant
def main():
    print("AshRock: I'm listening")
    
    while True:
        with sr.Microphone() as mic:
            try:
                audio = recognizer.listen(mic, timeout=5)  # Listen for audio input
                you = recognizer.recognize_google(audio)  # Recognize speech using Google API
                print("You: " + you)
            except sr.WaitTimeoutError:
                you = ""
                print("You: (timeout, no input detected)")
            except sr.UnknownValueError:
                you = ""
                print("You: (could not understand the audio)")
            except sr.RequestError:
                you = ""
                print("You: (could not request results from Google Speech Recognition service)")

        brain = respond(you)
        print("AshRock: " + brain)
        speaker.say(brain)
        speaker.runAndWait()
        
        if "exit" in you.lower():
            break

if __name__ == "__main__":
    main()
