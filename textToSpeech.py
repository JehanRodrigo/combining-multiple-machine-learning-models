# Use a pipeline as a high-level helper
from melo import TTS

# Speed is adjustable
speed = 1.0

# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
device = 'auto' # Will automatically use GPU if available

# English 
text = "Did you ever hear a folk tale about a giant turtle?"
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id

# American accent
output_path = 'en-us.wav'
model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# British accent
output_path = 'en-br.wav'
model.tts_to_file(text, speaker_ids['EN-BR'], output_path, speed=speed)

# Indian accent
output_path = 'en-india.wav'
model.tts_to_file(text, speaker_ids['EN_INDIA'], output_path, speed=speed)

# Australian accent
output_path = 'en-au.wav'
model.tts_to_file(text, speaker_ids['EN-AU'], output_path, speed=speed)

# Default accent
output_path = 'en-default.wav'
model.tts_to_file(text, speaker_ids['EN-Default'], output_path, speed=speed)



# from transformers import pipeline

# pipe = pipeline("text-to-audio", model="facebook/musicgen-small")

# # Input text (story)
# story_text = "Once upon a time, there was a cozy cat named Whiskers who loved to nap on the sofa."

# # Generate speech from text
# audio_data = pipe(story_text)

# # Save the output audio to a file
# with open("story_audio.wav", "wb") as f:
#     f.write(audio_data[0]['generated_audio'])

# print("Story audio saved as 'story_audio.wav'")


#  189M/2.36G