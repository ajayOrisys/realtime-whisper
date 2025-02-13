import asyncio
import sounddevice as sd
import numpy as np
import faster_whisper
import websockets
import matplotlib.pyplot as plt

model_size = "tiny"  # Use "small" for better accuracy
model_path = faster_whisper.download_model(model_size)
model = faster_whisper.WhisperModel(model_path, device="cpu")

print("Using audio device:", sd.default.device)

async def transcribe_audio(websocket):
    samplerate = 16000
    blocksize = 16000 * 2 

    print("Opening microphone stream...")
    try:
        with sd.InputStream(samplerate=samplerate, blocksize=blocksize, channels=1) as stream:
            print("Microphone is now active!")
            while True:
                audio_chunk = stream.read(blocksize)[0]
                audio_chunk = np.frombuffer(audio_chunk, dtype=np.float32)
                audio_chunk = audio_chunk.astype(np.float32) / 32768.0  # Correct normalization

                # Transcribe with adjusted parameters
                segments, _ = model.transcribe(
                    audio_chunk,
                    beam_size=5,
                    language="en",
                    vad_filter=False,
                )
                
                for segment in segments:
                    transcript = segment.text.strip()
                    if transcript:
                        print("Sending transcript:", transcript)
                        await websocket.send(transcript)

    except Exception as e:
        print("Error during transcription:", e)
 
 
async def handler(websocket):
    print("Client connected from:", websocket.remote_address)
    try:
        await transcribe_audio(websocket)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected normally")
    except Exception as e:
        print("Handler error:", e)
    finally:
        print("Client disconnected:", websocket.remote_address)

async def main():
    server = await websockets.serve(
        handler,
        "localhost",
        8765,
        origins=["http://localhost:5173", "http://127.0.0.1:5173"]  
    )
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())