import speech_recognition as sr
import pyaudio

# Create a recognizer instance
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)
    
    # Create a PyAudio instance
    audio = pyaudio.PyAudio()

    # Open the microphone stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)

    # Read the audio data from the stream
    audio_data = stream.read(1024)

    try:
        # Use the recognizer to convert speech to text
        text = r.recognize_google(audio_data)
        print("Speech to Text:")
        print(text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from the Speech Recognition service; {0}".format(e))
    
    # Stop the microphone stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio instance
    audio.terminate()
