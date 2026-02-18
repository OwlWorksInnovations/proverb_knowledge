import socket
from unittest.mock import patch
from transcribe import transcribe
from ai import send_ai_request
import os
import dotenv
import wave

dotenv.load_dotenv()
def env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise EnvironmentError(f'Missing required env var: "{name}"')
    return value
SYSTEM = env("SYSTEM")
MODEL  = env("MODEL")
API_KEY = env("API_KEY")

# Test no internet handling
def transcribe_test_1(test_api_key):
    try:
        with patch("socket.socket", side_effect=OSError("Network unreachable")):
            transcribe("src/tests_assets/voice.wav", test_api_key)
        
        print("[Transcribe] [+] No internet test passed.")
    except:
        print("[Transcribe] [!] No internet test did not pass!")

def transcribe_test_2(test_api_key):
    try:
        transcribe("invalid_file.wav", test_api_key)
        
        print("[Transcribe] [+] file not found tests passed.")
    except:
        print("[Transcribe] [!] file not found tests did not pass.")

def transcribe_test_3(test_api_key):
    try:
        transcribe("src/tests_assets/voice.wav", test_api_key)
        
        print("[Transcribe] [+] all tests passed.")
    except:
        print("[Transcribe] [!] some or all test did not pass.")
        
def ai_test_1(test_api_key):
    try:
        with patch("socket.socket", side_effect=OSError("Network unreachable")):
            send_ai_request(SYSTEM, "testing", MODEL, test_api_key)
        
        print("[AI] [+] No internet test passed.")
    except:
        print("[AI] [!] No internet test did not pass!")

transcribe_test_1(API_KEY)
transcribe_test_2(API_KEY)
transcribe_test_3(API_KEY)
ai_test_1(API_KEY)