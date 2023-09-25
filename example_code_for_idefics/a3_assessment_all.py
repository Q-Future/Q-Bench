import json, random
from tqdm import tqdm
import numpy as np
import os

from scipy.stats import spearmanr, pearsonr
from scipy.stats import kendalltau

from PIL import Image
import torch
from transformers import IdeficsForVisionText2Text, AutoProcessor

os.makedirs("IQA_outputs/idefics/", exist_ok=True)
device = "cuda" if torch.cuda.is_available() else "cpu"

checkpoint = "HuggingFaceM4/idefics-9b-instruct"
model = IdeficsForVisionText2Text.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
processor = AutoProcessor.from_pretrained(checkpoint) # An implementation of 


def softmax(a, b, temperature=100):
    a /= temperature
    b /= temperature
    return np.exp(a) / (np.exp(a) + np.exp(b))



image_paths = [
    "../datasets/LIVEC/Images/",
    "../datasets/SPAQ/",
    "../datasets/1024x768/",
    "../datasets/FLIVE_Database/database/",
    "../datasets/CGIQA-6K/database/",
    "../datasets/AGIQA-3K/database/",
    "../datasets/kadid10k/images/",
]

json_prefix = "a3_iqa_databases/jsons/"
jsons = [
    json_prefix + "livec.json",
    json_prefix + "spaq.json",
    json_prefix + "koniq.json",
    json_prefix + "flive.json",
    json_prefix + "cgi.json",
    json_prefix + "agi.json",
    json_prefix + "kadid.json",
]

for image_path, input_json in zip(image_paths, jsons):
    with open(input_json) as f:
        all_data = json.load(f)

    for llddata in tqdm(all_data):
        name = llddata["img_path"]


        raw_image = Image.open(image_path + name).convert("RGB")

        message = "Rate the quality of the image."
        # We feed to the model an arbitrary sequence of text strings and images. Images can be either URLs or PIL Images.
        prompts = [
            [
                f"User: {message}",
                raw_image, #Image.open(image_path),
                "<end_of_utterance>",
                "\nAssistant: The quality of the image is",
            ],
        ]
        
        # --batched mode
        inputs = processor(prompts, add_end_of_utterance_token=False, return_tensors="pt").to(device)
        # --single sample mode
        #inputs = processor(prompts[0], return_tensors="pt").to(device)

        # Generation args

        output_logits = model(**inputs).logits[0,-1]
        
        lgood, lpoor = output_logits[1781].item(), output_logits[6460].item()
        llddata["logit_good"], llddata["logit_poor"] = lgood, lpoor
        with open(f"IQA_outputs/idefics/{input_json.split('/')[-1]}", "a") as wf:
            json.dump(llddata, wf)
            
    gts = [float(di["gt_score"]) for di in all_data]
    prs = [softmax(di["logit_good"], di["logit_poor"]) for di in all_data]
            
    print("SRCC:", spearmanr(gts, prs))
    print("PLCC:", pearsonr(gts, prs))