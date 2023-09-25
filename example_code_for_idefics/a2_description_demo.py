import torch
from transformers import IdeficsForVisionText2Text, AutoProcessor
from PIL import Image
device = "cuda" if torch.cuda.is_available() else "cpu"

checkpoint = "HuggingFaceM4/idefics-9b-instruct"
model = IdeficsForVisionText2Text.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
processor = AutoProcessor.from_pretrained(checkpoint)


question = "Describe the quality, aesthetics and other low-level appearance of the image in details."

    
raw_image = Image.open("example_code_for_idefics/midjourney_lowstep_036.jpg").convert("RGB")
prompts = [
        [
            f"User: {question}",
            raw_image, #Image.open(image_path),
            "<end_of_utterance>",

            "\nAssistant:",
        ],
]

inputs = processor(prompts, add_end_of_utterance_token=False, return_tensors="pt").to(device)

    # Generation args
exit_condition = processor.tokenizer("<end_of_utterance>", add_special_tokens=False).input_ids
bad_words_ids = processor.tokenizer(["<image>", "<fake_token_around_image>"], add_special_tokens=False).input_ids

generated_ids = model.generate(**inputs, eos_token_id=exit_condition, bad_words_ids=bad_words_ids, max_length=240)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
response = generated_text.split("Assistant:")[-1].strip()
print(f"###Response:", response)
