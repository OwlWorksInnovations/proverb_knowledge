import eel, os, threading, pyaudio, wave, dotenv
from transcribe import transcribe
from ai import send_ai_request
from groq import Groq

dotenv.load_dotenv()
def env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise EnvironmentError(f'Missing required env var: "{name}"')
    return value
SYSTEM = env("SYSTEM")
MODEL  = env("MODEL")
API_KEY = env("API_KEY")

FORMAT, CHANNELS, RATE, CHUNK = pyaudio.paInt16, 1, 44100, 1024
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "output.wav")

is_recording = False
frames = []

def _record_loop():
    global is_recording, frames
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    
    while is_recording:
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    with wave.open(OUTPUT_FILE, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    process_audio()

@eel.expose
def recordAudio():
    global is_recording
    if not is_recording:
        is_recording = True
        threading.Thread(target=_record_loop, daemon=True).start()

@eel.expose
def stopAudio():
    global is_recording
    is_recording = False

def process_audio():
    question = transcribe("output.wav", API_KEY)
    eel.updateQuestionText(question)
    answer = send_ai_request(SYSTEM, question, MODEL, API_KEY)
    eel.updateAnswerText(answer)
    
    os.remove("output.wav")

eel.init("www")
eel.start("index.html")