import numpy as np

import torch
from transformers import IdeficsForVisionText2Text, AutoProcessor
from PIL import Image
device = "cuda" if torch.cuda.is_available() else "cpu"

checkpoint = "HuggingFaceM4/idefics-9b-instruct"
model = IdeficsForVisionText2Text.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
processor = AutoProcessor.from_pretrained(checkpoint)






raw_image = Image.open("example_code_for_idefics/2415943373.jpg").convert("RGB")

message = "Which part of the human is cropped out of the image?\nChoose between one of the options as follows:\n"

prompts = [
        [
            f"User: {message}",
            raw_image,
            "<end_of_utterance>",
            "\nAssistant:",
        ],
]

# --batched mode
inputs = processor(prompts, add_end_of_utterance_token=False, return_tensors="pt").to(device)

answers = ["His head", "His hand", "His leg", ""]
losses = []

for answer in answers:
    if answer:
        inputs = processor([prompts[0]+[answer]], add_end_of_utterance_token=False, return_tensors="pt").to(device)
        inputs["labels"] = inputs["input_ids"]
        result = model(**inputs).loss.item()
        losses.append(result)
        
print(answers[np.argmin(losses)])
