<div align="center">
    


  <h1>Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision</h1>

_How do multi-modaility LLMs perform on low-level computer vision?_


  <div>
      <a href="https://teowu.github.io/" target="_blank">Haoning Wu</a><sup>1</sup><sup>*</sup>,
      <a href="https://github.com/zzc-1998" target="_blank">Zicheng Zhang</a><sup>2</sup><sup>*</sup>,
      <a href="https://github.com/ZhangErliCarl/" target="_blank">Erli Zhang</a><sup>1</sup><sup>*</sup>,
      <a href="https://chaofengc.github.io" target="_blank">Chaofeng Chen</a><sup>1</sup>,
      <a href="https://liaoliang92.github.io" target="_blank">Liang Liao</a><sup>1</sup>,
  </div>

<div>
      <a href="https://github.com/AnnanWangDaniel" target="_blank">Annan Wang</a><sup>1</sup>,
      <a href="https://github.com/lcysyzxdxc" target="_blank">Chunyi Li</a><sup>2</sup>,
      <a href="https://wenxiusun.com" target="_blank">Wenxiu Sun</a><sup>3</sup>,
      <a href="https://scholar.google.com/citations?user=uT9CtPYAAAAJ&hl=en" target="_blank">Qiong Yan</a><sup>3</sup>,
      <a href="https://ee.sjtu.edu.cn/en/FacultyDetail.aspx?id=24&infoid=153&flag=153" target="_blank">Guangtao Zhai</a><sup>2</sup>,
      <a href="https://personal.ntu.edu.sg/wslin/Home.html" target="_blank">Weisi Lin</a><sup>1</sup><sup>#</sup>
  </div>
  <div>
  <sup>1</sup>Nanyang Technological University, <sup>2</sup>Shanghai Jiaotong University, <sup>3</sup>Sensetime Research
       </div>   
<div>
<sup>*</sup>Equal contribution. <sup>#</sup>Corresponding author. 
   </div>
    

<a href="https://arxiv.org/abs/2309.14181"><strong>Paper</strong></a> |
<a href="https://vqassessment.github.io/Q-Bench"><strong>Project Page</strong></a> |
<a href="https://github.com/VQAssessment/Q-Bench"><strong>Github</strong></a> |
 <a href="https://huggingface.co/datasets/nanyangtu/LLVisionQA-QBench"><strong>Data (LLVisionQA)</strong></a> |
 <a href="https://huggingface.co/datasets/nanyangtu/LLDescribe-QBench"><strong>Data (LLDescribe)</strong></a> |
<a href="https://vqassessment.github.io/Chinese-Q-Bench"><strong>质衡 (Chinese-Q-Bench)</strong></a>

    
 <div>

<a href="https://github.com/VQAssessment/"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fvqassessment%2FQ-Bench&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
    
    
<a href="https://github.com/VQAssessment/Q-Bench"><img src="https://img.shields.io/github/stars/VQAssessment/Q-Bench"/></a>
    
   </div>

    
    
  <div style="width: 80%; text-align: center; margin:auto;">
      <img style="width:80%" src="logo.png">
  </div>
    

  <div style="width: 80%; text-align: center; margin:auto;">
      <img style="width:80%" src="qbench.png">
  </div>
    


</div>

The proposed Q-Bench includes three realms for low-level vision: perception (A1), description (A2), and assessment (A3).

- For perception (A1) /description (A2), we collect two benchmark datasets LLVisionQA/LLDescribe.
- We are open to **submission-based evaluation** for the two tasks. The details for submission is as follows.
- For assessment (A3), as we use **public datasets**, we provide an abstract evaluation code for arbitrary MLLMs for anyone to test.



## GPT-4V!

![](gpt-4v-vs-human.png)

Our latest experiment suggests that [GPT-4V](https://chat.openai.com) is primarily human-level on general low-level perception, marking a new era for low-level visual perception and understanding.

Here is the comparison of [GPT-4V](https://chat.openai.com) and non-expert human on `test` set of Task A1 (Perception).

|**Participant Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
| GPT-4V | 0.7792 | 0.7918 | **0.6268** | 0.7058 | **0.7303** | 0.7466 | **0.7795** | **0.7336** (+0.1142 to best open-source)  |
| human-1 | **0.8248** | **0.7939** | 0.6029 | **0.7562** | 0.7208 | **0.7637** | 0.7300 | **0.7431** (+0.0095 to GPT-4V)  |

We sincerely hope that one day **open-source models** can also get that level and we believe that it is coming soon. Try to challenge and beat it!

## Submission Guideline for A1/A2

### Option 1: Submit Results

**New on Oct. 15! For people with bad connection to huggingface, we have also provided a GitHub-release version of all datasets. Please see our [release](https://github.com/VQAssessment/Q-Bench/releases/tag/v1.0.1.1014datarelease) as an alternative data source.**

**Important! We have released the datasets for these two tasks, for everyone to test on local machines and directly submit results. Please refer to the [data release notes](/data_release) and [example code](/example_code_for_idefics) to smoothly test these data.**



**Please email `haoning001@e.ntu.edu.sg` to submit your result in json format.**


### Option 2: Submit Model

Otherwise, you can consider submitting your model to Q-Bench (A1/A2), you can prepare a huggingface/GitHub repo (with some README for us to run it) of your MLLM with an implementation of the following single ability:

- Generate text outputs based on multi-modality inputs (`image + text`).

Specifically, it should has two important methods: `embed_image_and_text` (to allow multi-modality inputs), and `generate` (for dialog).

We recommend to wrap up the function call to your MLLM in the following format:

```python
from PIL import Image
from my_mllm_model import Model, Tokenizer, embed_image_and_text # [REPLACE with YOUR MLLM here]

model, tokenizer = Model(), Tokenizer()

prompt = '[ANY_PROMPT]'

image = Image.open("image_for_query.jpg")
input_embeds = embed_image_and_text(image, prompt) #
generated_texts = tokenizer.batch_decode(model.generate(input_embeds=input_embeds))[0]
```

*Optional: You will also need to implement the generative loss for your model if you would like to test with close-set inference (PPL-based) for perception task (A1), as follows:*

```python
loss = model(input_embeds=input_embeds, labels=input_ids).loss.item()
```

We further provide a demo implementation of IDEFICS, huggingface's open-source MLLM, for most simple question-answering (A1) and description (A2). See [example](example_code_for_idefics/README.md) on how to run the demo and provide a similar one for submission-based evaluation.

**Please email `haoning001@e.ntu.edu.sg` to submit your model if you are _outside_ China Mainland.**
**Please email `zzc1998@sjtu.edu.cn` to submit your model if you are _inside_ China Mainland.**


## A1: Perception

A snapshot for LLVisionQA benchmark dataset for MLLM low-level perception ability is as follows. See the [leaderboard](leaderboards/) here.

![Picture](llvisionqa_db.png)

We measure the answer accuracy of MLLMs (provided with the question and all choices) as the metric here.

## A2: Description

A snapshot for LLDescribe benchmark dataset for MLLM low-level description ability is as follows. See the [leaderboard](leaderboards/) here.

![Picture](lldescribe.png)

We measure the _completeness_, _precision_, and _relevance_ of MLLM descriptions as the metric here.

## A3: Assessment

_An exciting ability that MLLMs are able to predict quantitative scores for IQA!_

### Methodology

![Picture](llmiqa.png)

### Predict a Score

#### Pseudo Code

Similarly as above, as long as a model (based on causal language models) has the following two methods: `embed_image_and_text` (to allow multi-modality inputs), and `forward` (for computing logits), the Image Quality Assessment (IQA) with the model can be achieved as follows:

```python
from PIL import Image
from my_mllm_model import Model, Tokenizer, embed_image_and_text

model, tokenizer = Model(), Tokenizer()

prompt = "##User: Rate the quality of the image.\n" \
         "##Assistant: The quality of the image is" ### This line can be modified based on MLLM's default behaviour.

good_idx, poor_idx = tokenizer(["good","poor"]).tolist()

image = Image.open("image_for_iqa.jpg")
input_embeds = embed_image_and_text(image, prompt)
output_logits = model(input_embeds=input_embeds).logits[0,-1]
q_pred = (output_logits[[good_idx, poor_idx]] / 100).softmax(0)[0]
```

\*Note that you can modify the second line based on your model's default format, _e.g._ for [Shikra](https://github.com/shikras/shikra), the "##Assistant: The quality of the image is" is modified as "##Assistant: The answer is". It is okay if your MLLM will first answer "Ok, I would like to help! The image quality is", just replace this into line 2 of the prompt.

#### Example Real Code for IDEFICS

We further provide a full implementation of IDEFICS on IQA. See [example](example_code_for_idefics/README.md) on how to run IQA with this MLLM. Other MLLMs can also be modified in the same way for use in IQA.

#### Compute SRCC/PLCC with IQA databases

We have prepared JSON format human opinion scores (MOS) for the seven IQA databases as evaluated in our benchmark.

Please see [IQA_databases](a3_iqa_databases/) for details.

### Official Results on IQA Databases

Moved to [leaderboards](leaderboards/). Please click to see details.

## Contact

Please contact any of the first authors of this paper for queries.

- Haoning Wu, `haoning001@e.ntu.edu.sg`, @teowu
- Zicheng Zhang, `zzc1998@sjtu.edu.cn`, @zzc-1998
- Erli Zhang, `ezhang005@e.ntu.edu.sg`, @ZhangErliCarl

## Citation

If you find our work interesting, please feel free to cite our paper:

```bibtex
@article{wu2023qbench,
    title={Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision},
    author={Wu, Haoning and Zhang, Zicheng and Zhang, Erli and Chen, Chaofeng and Liao, Liang and Wang, Annan and Li, Chunyi and Sun, Wenxiu and Yan, Qiong and Zhai, Guangtao and Lin, Weisi},
    year={2023},
}
```
