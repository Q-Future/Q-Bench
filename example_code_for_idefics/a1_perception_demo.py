import torch
from transformers import IdeficsForVisionText2Text, AutoProcessor
from PIL import Image
device = "cuda" if torch.cuda.is_available() else "cpu"

checkpoint = "HuggingFaceM4/idefics-9b-instruct"
model = IdeficsForVisionText2Text.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
processor = AutoProcessor.from_pretrained(checkpoint)






raw_image = Image.open("example_code_for_idefics/2415943373.jpg").convert("RGB")

message = "Which part of the human is cropped out of the image?\nChoose between one of the options as follows:\nA. His head\nB. his leg\nC. his hand\n."

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

# Generation args
exit_condition = processor.tokenizer("<end_of_utterance>", add_special_tokens=False).input_ids
bad_words_ids = processor.tokenizer(["<image>", "<fake_token_around_image>"], add_special_tokens=False).input_ids

generated_ids = model.generate(**inputs, eos_token_id=exit_condition, bad_words_ids=bad_words_ids, max_length=180)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
response = generated_text.split("Assistant:")[-1]
print(response)
