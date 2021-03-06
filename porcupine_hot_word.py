#!/usr/bin/env python3
import struct
import pyaudio
import pvporcupine

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(keywords=["computer"],
                                   access_key='OBarq6+nQZjftCadhlX1ZR1WulknlRl2PzkUEmxYU7RBZLYTP2g6QQ==')

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
finally:
    if porcupine is not None:
        porcupine.delete()