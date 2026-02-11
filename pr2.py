import speech_recognition as sr

def transcribe_audio(file_path):
    # Create recognizer object
    recognizer = sr.Recognizer()

    try:
        # Load audio file
        with sr.AudioFile(file_path) as source:
            print("Listening to the audio file...")
            audio = recognizer.record(source)

        # Convert speech to text using Google Web API
        print("Transcribing...")
        text = recognizer.recognize_google(audio)

        print("Transcription Completed!")
        return text

    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."

    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service."

    except Exception as e:
        return f"Error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    file_path = "audio.wav"   # Replace with your audio file name
    result = transcribe_audio(file_path)
    print("Transcribed Text:")
    print(result)
