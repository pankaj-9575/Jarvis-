🤖 Jarvis - Your Personal Assistant
A voice-controlled personal assistant built using Python that performs tasks like searching Wikipedia, opening applications, sending emails and WhatsApp messages, setting reminders, and more.

📌 Features
🎤 Voice Recognition – Accepts voice commands using the speech_recognition library
🔊 Text-to-Speech (TTS) – Responds using the pyttsx3 engine
🌐 Web Automation – Opens websites like YouTube, Google, and Stack Overflow
🎵 Play Music – Automatically plays music from a specified directory
📧 Email Sending – Sends emails using the smtplib and EmailMessage modules
📱 WhatsApp Messaging – Sends WhatsApp messages using pywhatkit
📋 Open Applications – Launches system applications like Notepad and Command Prompt
🔔 Set Reminders – Displays Windows notifications using win10toast
🗣️ Basic Conversation – Responds to common questions like "How are you?" and "Who created you?"

🛠️ Technologies Used
Python 3
pyttsx3 (Text-to-Speech)
speech_recognition (Speech Input)
wikipedia (Knowledge Retrieval)
pywhatkit (WhatsApp Automation)
smtplib & EmailMessage (Email)
win10toast (Windows Notifications)

🚀 How to Run
1. Clone this repository:
git clone https://github.com/pankaj-9575/jarvis-assistant.git
cd jarvis-assistant

2.Install the required packages:
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit win10toast

3.Run the assistant:
python jarvis.py


📧 Configuration
Update the email and password in the sendEmail() function.
Customize music directory and application paths as needed.
