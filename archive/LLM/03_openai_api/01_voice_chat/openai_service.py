import base64
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI()


def stt(audio):
    output_filepath = 'input.mp3'
    audio.export(output_filepath, format='mp3')

    with open(output_filepath, 'rb') as f:
        transcription = client.audio.transcriptions.create(
            file=f,
            model='whisper-1',
        )
    os.remove(output_filepath)

    return transcription.text

def ask_gpt(messages, model='gpt-5.6-luna'):
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1,
        top_p=1,
        max_completion_tokens=4096
    ).choices[0].message.content

def tts(response: str):
    filename = 'output.mp3'

    with client.audio.speech.with_streaming_response.create(
        model='tts-1',
        voice='coral',
        input=response
    ) as resp:
        resp.stream_to_file(filename)

    with open(filename, 'rb') as f:
        data = f.read()
        b64_encoded = base64.b64encode(data).decode()
        print(b64_encoded)
    os.remove(filename)

    return b64_encoded

def stt_file(uploaded_file):
    transcription = client.audio.transcriptions.create(
        file=(uploaded_file.name, uploaded_file.getvalue()),
        model='whisper-1',
    )

    return transcription.text