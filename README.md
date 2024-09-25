# Jarvis - Voice Assistant in Python

Jarvis is a simple voice-activated assistant developed in Python. It can perform tasks such as opening applications, searching the web, sending emails, telling the time, and much more based on voice commands. This project utilizes the speech_recognition library for recognizing speech and pyttsx3 for text-to-speech output

## Features

*  Voice Commands:  Understands and responds to natural language voice commands.
* Application Launching: Open applications such as Notepad, Chrome, etc.
* Web Search: Perform Google searches through voice input.
* System Info: Provide system information like the current time and weather.
* Email: Send emails via voice command.
* Customizable: You can add more commands and functionalities.

# Requirements
* " speech_recognition" for voice recognition.
* "pyttsx3" for text-to-speech.
* "pywhatkit" for web searches and controlling apps.
* "datetime" for time-related tasks.
* "wikipedia-api" for Wikipedia searches.
* "smtplib" for sending emails.

Install the required libraries using pip:
```
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia-api

```

## How it works
Jarvis listens to your voice input, processes the command, and then executes the task based on predefined instructions. It uses speech_recognition to convert voice input into text and responds accordingly using pyttsx3 for speech output.

## Workflow:

1. Listen: Jarvis listens for the wake word (e.g., "Jarvis")
2. Process: Converts the voice input to text using speech_recognition.
3. Execute: Based on the command, Jarvis performs actions like searching the web, opening an application, telling the time, or sending an email.
4. Respond: After processing, Jarvis provides verbal feedback using pyttsx3.

## Known Issues
* Speech Recognition Accuracy: Background noise can reduce the accuracy of speech recognition.
* Internet Connection: Some functionalities (like web search) require an active internet connection

  ## Future Improvements
  * Add support for more natural language processing (NLP) to understand complex queries.
  * Improve accuracy of voice recognition with background noise reduction.
  * Add additional integrations with smart home devices, music services, etc.


# If you like the project, consider giving it a ⭐ on GitHub!

