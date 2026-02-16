from groq import Groq

def transcribe(filename: str, api_key: str):
    client = Groq(
        api_key=api_key
    )
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3",
        temperature=0,
        response_format="verbose_json",
        )
        return transcription.text
      