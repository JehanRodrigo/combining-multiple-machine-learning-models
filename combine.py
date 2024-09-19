# from transformers import BlipProcessor, BlipForConditionalGeneration
# from PIL import Image # Python Imaging Library

# # Load the image and model
# image = Image.open("Friends.jpg")
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# # Generate a caption for the image
# inputs = processor(image, return_tensors="pt")
# output = model.generate(**inputs)
# image_description = processor.decode(output[0], skip_special_tokens=True)
# print(f"Image description: {image_description}")


# from transformers import pipeline
# from PIL import Image

# # Load the image captioning pipeline
# image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# # Open the image
# image = Image.open("Friends.jpg")

# # Generate a caption for the image
# image_description = image_to_text(image)

# # Print the description (caption)
# print(f"Image description: {image_description[0]['generated_text']}")


# # Load the text generation pipeline
# story_generator = pipeline("text-generation", model="openai-community/gpt2")

# # Generate a story based on the image description
# story = story_generator(f"Write a story about: {image_description}", max_length=200)

# # Extract the generated text
# generated_story = story[0]['generated_text']
# print(f"Generated Story: {generated_story}")

from transformers import pipeline
from PIL import Image

# Load the image captioning pipeline
image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Open the image
image = Image.open("Friends.jpg")

# Generate a caption for the image
image_description = image_to_text(image)

# Extract the caption text
caption_text = image_description[0]['generated_text']
print(f"Image description: {caption_text}")

# Load the text generation pipeline
story_generator = pipeline("text-generation", model="distilgpt2")

# Generate a story based on the image description
story = story_generator(f"{caption_text}", max_new_tokens=100)

# Extract the generated text
generated_story = story[0]['generated_text']
print(f"Generated Story: {generated_story}")





# Load the text-to-speech pipeline
# tts = pipeline("text-to-speech", model="speechbrain/tts-transformer-en-ljspeech")

# # Input text (story)
# # story_text = "Once upon a time, there was a cozy cat named Whiskers who loved to nap on the sofa."

# # Generate speech from text
# audio_data = tts(generated_story)

# # Save the output audio to a file
# with open("story_audio.wav", "wb") as f:
#     f.write(audio_data[0]['generated_audio'])

# print("Story audio saved as 'story_audio.wav'")

