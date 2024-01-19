# Hot Leaderboards @ Oct 30

<div align="center">
    
<div>
_Join the competition for low-level vision now!_           
</div>
    
<div>
_version_: v1.0.2.1030wip; _Timeliness_: Updated on 30th Oct.   
</div>
    
</div>

## Overall Leaderboards

<div align="center">

| Rank | [A1: Perception](#leaderboards-for-a1-perception) (dev set) | [A1: Perception](#leaderboards-for-a1-perception) (test set) | [A2: Description](#leaderboards-for-a2-description) | [A3: Assessment](#leaderboards-for-a3-assessment) |
|:----:|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|:-------------------------------------------------------------:|:----------------------------------------------------------:|
| 🥇   | InternLM-XComposer-VL (0.6535) | InternLM-XComposer-VL (0.6435)                                         |      InternLM-XComposer-VL (4.21/6)                                             | InternLM-XComposer-VL (0.542,0.581)                         |
| 🥈   | LLaVA-v1.5-13B (0.6214) | InstructBLIP-T5-XL (0.6194)                                     |  Kosmos-2 (4.03/6)                                        | Qwen-VL (0.475,0.506)                                       |
| 🥉   | InstructBLIP-T5-XL (0.6147) |  Qwen-VL (0.6167)                             | mPLUG-Owl (3.94/6)                                        | LLaVA-v1.5-13B (0.444,0.473)                                    |

</div>


## Leaderboards for (A1): Perception


About the partition of `dev` and `test` subsets, please see [our dataset release notes](../data_release/). As some models excel on original testing pipeline while some others perform better under PPL-based testing, we maintain two leaderboards for two different testing methods. See [examples](../example_code_for_idefics) for their different settings.

### Original Testing Pipeline
- 14 models tested
- via Multi-Choice Questions

#### Accuracies on Open-set (`dev`)

|**Model Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
| random guess              | 0.5000  | 0.2786  | 0.3331  | 0.3789  | 0.3848  | 0.3828  | 0.3582  | 0.3780  |
| LLaVA-v1.5 (Vicuna-v1.5-7B) | 0.6636  | 0.5819  | 0.5051  | 0.4942  | 0.6574  | 0.5461  | 0.7061  | 0.5866  |
| LLaVA-v1.5 (Vicuna-v1.5-13B) | 0.6527  | 0.6438  | 0.5659  | 0.5603  | 0.6713  | 0.6118  | 0.6735  | 0.6214  |
| InternLM-XComposer-VL (InternLM) | 0.6945  | 0.6527  | 0.6085  | 0.6167  | 0.7014  | 0.5691  | 0.7510  | 0.6535  |
| IDEFICS-Instruct (LLaMA-7B) | 0.5618  | 0.4469  | 0.4402  | 0.4280  | 0.5417  | 0.4474  | 0.5633  | 0.4870  |
| Qwen-VL (QwenLM)           | 0.6309  | 0.5819  | 0.5639  | 0.5058  | 0.6273  | 0.5789  | 0.7388  | 0.5940  |
| Shikra (Vicuna-7B)         | 0.6564  | 0.4735  | 0.4909  | 0.4883  | 0.5949  | 0.5000  | 0.6408  | 0.5465  |
| Otter-v1 (MPT-7B)          | 0.5709  | 0.4071  | 0.3955  | 0.4222  | 0.4931  | 0.4408  | 0.5265  | 0.4635  |
| InstructBLIP (Flan-T5-XL)  | 0.6764  | 0.5996  | 0.5598  | 0.5623  | 0.6551  | 0.5822  | 0.6939  | 0.6147  |
| InstructBLIP (Vicuna-7B)   | 0.7164  | 0.5265  | 0.4381  | 0.4864  | 0.6250  | 0.5559  | 0.6490  | 0.5672  |
| VisualGLM-6B (GLM-6B)      | 0.6018  | 0.5420  | 0.4625  | 0.5175  | 0.5440  | 0.5362  | 0.5714  | 0.5378  |
| mPLUG-Owl (LLaMA-7B)       | 0.6600  | 0.5487  | 0.4402  | 0.5136  | 0.5509  | 0.5428  | 0.6571  | 0.5538  |
| LLaMA-Adapter-V2           | 0.6618  | 0.5929  | 0.5213  | 0.5739  | 0.5625  | 0.6316  | 0.6490  | 0.5946  |
| LLaVA-v1 (Vicuna-13B)      | 0.5400  | 0.5310  | 0.5538  | 0.4864  | 0.5463  | 0.5559  | 0.6327  | 0.5418  |
| MiniGPT-4 (Vicuna-13B)     | 0.5582  | 0.5022  | 0.4037  | 0.4202  | 0.4838  | 0.5197  | 0.6122  | 0.4903  |



#### Accuracies on Close-set (`test`)


Results of [GPT-4V](https://chat.openai.com) and non-expert human:

|**Participant Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
| GPT-4V (Close-Source Model)   | 0.7792  | 0.7918  | 0.6268  | 0.7058  | 0.7303  | 0.7466  | 0.7795  | 0.7336  |
| Junior-level Human            | 0.8248  | 0.7939  | 0.6029  | 0.7562  | 0.7208  | 0.7637  | 0.7300  | 0.7431  |
| Senior-level Human            | 0.8431  | 0.8894  | 0.7202  | 0.7965  | 0.7947  | 0.8390  | 0.8707  | 0.8174  |

GPT-4V is primarily a Junior-level Human.

Results of Open-source models:

|**Model Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
| random guess              | 0.5000  | 0.2848  | 0.3330  | 0.3724  | 0.3850  | 0.3913  | 0.3710  | 0.3794  |
| LLaVA-v1.5 (Vicuna-v1.5-7B) | 0.6460  | 0.5922  | 0.5576  | 0.4798  | 0.6730  | 0.5890  | 0.7376  | 0.6007  |
| LLaVA-v1.5 (Vicuna-v1.5-13B) | 0.6496  | 0.6486  | 0.5412  | 0.5355  | 0.6659  | 0.5890  | 0.7148  | 0.6140  |
| InternLM-XComposer-VL (InternLM) | 0.6843  | 0.6204  | 0.6193  | 0.5681  | 0.7041  | 0.5753  | 0.7719  | 0.6435  |
| IDEFICS-Instruct (LLaMA-7B) | 0.6004  | 0.4642  | 0.4671  | 0.4038  | 0.5990  | 0.4726  | 0.6477  | 0.5151  |
| Qwen-VL (QwenLM)           | 0.6533  | 0.6074  | 0.5844  | 0.5413  | 0.6635  | 0.5822  | 0.7300  | 0.6167  |
| Shikra(Vicuna-7B)          | 0.6909  | 0.4793  | 0.4671  | 0.4731  | 0.6086  | 0.5308  | 0.6477  | 0.5532  |
| Otter-v1 (MPT-7B)          | 0.5766  | 0.3970  | 0.4259  | 0.4212  | 0.4893  | 0.4760  | 0.5417  | 0.4722  |
| InstructBLIP (Flan-T5-XL)  | 0.6953  | 0.5900  | 0.5617  | 0.5731  | 0.6551  | 0.5651  | 0.7121  | 0.6194  |
| InstructBLIP (Vicuna-7B)   | 0.7099  | 0.5141  | 0.4300  | 0.4500  | 0.6301  | 0.5719  | 0.6439  | 0.5585  |
| VisualGLM-6B (GLM-6B)      | 0.6131  | 0.5358  | 0.4403  | 0.4856  | 0.5489  | 0.5548  | 0.5779  | 0.5331  |
| mPLUG-Owl (LLaMA-7B)       | 0.7245  | 0.5488  | 0.4753  | 0.4962  | 0.6301  | 0.6267  | 0.6667  | 0.5893  |
| LLaMA-Adapter-V2           | 0.6618  | 0.5466  | 0.5165  | 0.5615  | 0.6181  | 0.5925  | 0.5455  | 0.5806  |
| LLaVA-v1 (Vicuna-13B)      | 0.5712  | 0.5488  | 0.5185  | 0.4558  | 0.5800  | 0.5719  | 0.6477  | 0.5472  |
| MiniGPT-4 (Vicuna-13B)     | 0.6077  | 0.5033  | 0.4300  | 0.4558  | 0.5251  | 0.5342  | 0.6098  | 0.5177  |


### (*Additional*) PPL-based Testing Pipeline 

- 11 models tested
- via Losses of Different Answers
- *non-finalized work-in-progress version, may update*

*No options are provided in prompts!*

#### Accuracies on Open-set (`dev`)

|**Model Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
idefics | 0.6109 | 0.5332 | 0.4422 | 0.4942 | 0.5625 | 0.4704 | 0.6327 | 0.5318 |
instructblip_t5 | 0.6200 | 0.4425 | 0.3996 | 0.4280 | 0.5347 | 0.4737 | 0.5837 | 0.4936 |
instructblip_vicuna | 0.5964 | 0.4137 | 0.4158 | 0.4689 | 0.4699 | 0.4704 | 0.5429 | 0.4816 |
kosmos_2 | 0.5800 | 0.3562 | 0.3915 | 0.3969 | 0.4606 | 0.4408 | 0.5551 | 0.4502 |
llama_adapter_v2 | 0.5691 | 0.3208 | 0.4057 | 0.3852 | 0.4491 | 0.4671 | 0.5061 | 0.4401 |
llava_v1.5 | 0.6764 | 0.4071 | 0.3469 | 0.4280 | 0.5347 | 0.4803 | 0.5306 | 0.4863 |
llava_v1 | 0.5945 | 0.4071 | 0.3671 | 0.3872 | 0.5116 | 0.4671 | 0.5306 | 0.4629 |
minigpt4_13b | 0.5509 | 0.4248 | 0.3347 | 0.4047 | 0.4722 | 0.4112 | 0.5020 | 0.4415 |
mplug_owl | 0.7909 | 0.4027 | 0.3793 | 0.4981 | 0.5602 | 0.5757 | 0.5347 | 0.5378 |
otter_v1 | 0.6782 | 0.4248 | 0.4462 | 0.4514 | 0.5833 | 0.5164 | 0.5878 | 0.5251 |
shikra | 0.6655 | 0.4690 | 0.5030 | 0.4669 | 0.6042 | 0.5230 | 0.6776 | **0.5525** (rank 1) |

#### Accuracies on Close-set (`test`)

|**Model Name** | yes-or-no | what | how | distortion | others | in-context distortion | in-context others | overall |
| - | - | - | - | - | - | -| - | -| 
idefics | 0.6752 | 0.5163 | 0.4280 | 0.4712 | 0.6396 | 0.4726 | 0.6250 | 0.5458 |
instructblip_t5 | 0.6661 | 0.4707 | 0.3971 | 0.4173 | 0.6181 | 0.4486 | 0.6364 | 0.5184 |
instructblip_vicuna | 0.6843 | 0.4469 | 0.3827 | 0.4981 | 0.5060 | 0.4726 | 0.5985 | 0.5130 |
kosmos_2 | 0.6496 | 0.3861 | 0.4239 | 0.4038 | 0.5585 | 0.4658 | 0.6061 | 0.4950 |
llama_adapter_v2 | 0.6551 | 0.3536 | 0.4012 | 0.4154 | 0.4964 | 0.4829 | 0.5758 | 0.4796 |
llava_v1.5 | 0.7500 | 0.4685 | 0.3519 | 0.4453 | 0.5776 | 0.5171 | 0.6578 | 0.5338 |
llava_v1 | 0.6642 | 0.4447 | 0.3951 | 0.4096 | 0.5847 | 0.4726 | 0.6250 | 0.5090 |
minigpt4_13b | 0.5730 | 0.4577 | 0.3580 | 0.4096 | 0.4988 | 0.4281 | 0.5758 | 0.4676 |
mplug_owl | 0.8449 | 0.4013 | 0.3951 | 0.4981 | 0.5752 | 0.6027 | 0.6212 | **0.5619** (rank 1) |
otter_v1 | 0.6971 | 0.4382 | 0.4568 | 0.4288 | 0.6372 | 0.4897 | 0.6553 | 0.5391 |
shikra | 0.6515 | 0.4729 | 0.5021 | 0.4269 | 0.6205 | 0.5034 | 0.7197 | 0.5478 |

## Leaderboards for (A2): Description


Abbreviations for dimensions: *comp: completeness, prec: precision, rele: relevance*

| **Model Name** | p_{0, comp} | p_{0, comp} | p_{2, comp} | s_{compl} | p_{0, prec} | p_{0, prec} | p_{2, prec} | s_{prec} | p_{0, rele} | p_{0, rele} | p_{2, rele} | s_{rele} | s_{sum} | 
| - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| LLaVA-v1.5 (Vicuna-v1.5-13B) | 27.68%  | 53.78%  | 18.55%  | 0.91/2.00 | 25.45%  | 21.47%  | 53.08%  | 1.28/2.00 | 6.31%   | 58.75%   | 34.94%   | 1.29/2.00 | 3.47/6.00 |
| InternLM-XComposer-VL (InternLM) | 19.94%  | 51.82%  | 28.24%  | 1.08/2.00 | 22.59%  | 28.99%  | 48.42%  | 1.26/2.00 | 1.05%   | 10.62%   | 88.32%   | 1.87/2.00 | 4.21/6.00 |
| IDEFICS-Instruct (LLaMA-7B) | 28.91%  | 59.16%  | 11.93%  | 0.83/2.00 | 34.68%  | 27.86%  | 37.46%  | 1.03/2.00 | 3.90%   | 59.66%   | 36.44%   | 1.33/2.00 | 3.18/6.00 |
| Qwen-VL (QwenLM)           | 26.34%  | 49.13%  | 24.53%  | 0.98/2.00 | 50.62%  | 23.44%  | 25.94%  | 0.75/2.00 | 0.73%   | 35.56%   | 63.72%   | 1.63/2.00 | 3.36/6.00 |
| Shikra (Vicuna-7B)         | 21.14%  | 68.33%  | 10.52%  | 0.89/2.00 | 30.33%  | 28.30%  | 41.37%  | 1.11/2.00 | 1.14%   | 64.36%   | 34.50%   | 1.33/2.00 | 3.34/6.00 |
| Otter-v1 (MPT-7B)          | 22.38%  | 59.36%  | 18.25%  | 0.96/2.00 | 40.68%  | 35.99%  | 23.33%  | 0.83/2.00 | 1.95%   | 13.2%    | 84.85%   | 1.83/2.00 | 3.61/6.00 |
| Kosmos-2                   | 8.76%   | 70.91%  | 20.33%  | 1.12/2.00 | 29.45%  | 34.75%  | 35.81%  | 1.06/2.00 | 0.16%   | 14.77%   | 85.06%   | 1.85/2.00 | 4.03/6.00 |
| InstructBLIP (Flan-T5-XL)  | 23.16%  | 66.44%  | 10.40%  | 0.87/2.00 | 34.85%  | 26.03%  | 39.12%  | 1.04/2.00 | 14.71%  | 59.87%   | 25.42%   | 1.11/2.00 | 3.02/6.00 |
| InstructBLIP (Vicuna-7B)   | 29.73%  | 61.47%  | 8.80%   | 0.79/2.00 | 27.84%  | 23.52%  | 48.65%  | 1.21/2.00 | 27.40%  | 61.29%   | 11.31%   | 0.84/2.00 | 2.84/6.00 |
| VisualGLM-6B (GLM-6B)      | 30.75%  | 56.64%  | 12.61%  | 0.82/2.00 | 38.64%  | 26.18%  | 35.18%  | 0.97/2.00 | 6.14%   | 67.15%   | 26.71%   | 1.21/2.00 | 2.99/6.00 |
| mPLUG-Owl (LLaMA-7B)       | 28.28%  | 37.69%  | 34.03%  | 1.06/2.00 | 26.75%  | 18.18%  | 55.07%  | 1.28/2.00 | 3.03%   | 33.82%   | 63.15%   | 1.6/2.00  | 3.94/6.00 |
| LLaMA-Adapter-V2           | 30.44%  | 53.99%  | 15.57%  | 0.85/2.00 | 29.41%  | 25.79%  | 44.8%   | 1.15/2.00 | 1.50%   | 52.75%   | 45.75%   | 1.44/2.00 | 3.45/6.00 |
| LLaVA-v1 (Vicuna-13B)      | 34.10%  | 40.52%  | 25.39%  | 0.91/2.00 | 30.02%  | 15.15%  | 54.83%  | 1.25/2.00 | 1.06%   | 38.03%   | 60.91%   | 1.6/2.00  | 3.76/6.00 |
| MiniGPT-4 (Vicuna-13B)     | 34.01%  | 32.15%  | 33.85%  | 1.00/2.00 | 29.20%  | 15.27%  | 55.53%  | 1.26/2.00 | 6.88%   | 45.65%   | 47.48%   | 1.41/2.00 | 3.67/6.00 |


## Leaderboards for (A3): Assessment

The datasets can be found [here](../a3_iqa_databases/).

See [IQA_outputs/eval.ipynb](IQA_outputs/eval.ipynb) for our ablation experiments.


| **Model Name**|KoNIQ-10k | SPAQ| LIVE-FB| LIVE-itw| CGIQA-6K| AGIQA-3K| KADID-10K|Average
| -| -| -| -| -| -| -| -| -| 
| NIQE | 0.316/0.377 | 0.693/0.669 | 0.211/0.288 | 0.480/0.451 | 0.075/0.056 | 0.562/0.517 | 0.374/0.428 |0.387/0.398|
| CLIP-ViT-Large-14 | 0.468/0.505 | 0.385/0.389 | 0.218/0.237 | 0.307/0.308 | 0.285/0.290 | 0.436/0.458 | 0.376/0.388 |0.354/0.368|
| LLaVA-v1.5 (Vicuna-v1.5-7B) | 0.463/0.459 | 0.443/0.467 | 0.305/0.321 | 0.344/0.358 | **0.321/0.333** | 0.672/0.738 | 0.417/0.440 |0.424/0.445|
| LLaVA-v1.5 (Vicuna-v1.5-13B) | 0.448/0.460 | 0.563/0.584 | 0.310/0.339 | 0.445/0.481 | 0.285/0.297 | 0.664/0.754 | 0.390/0.400 |0.444/0.474|
| InternLM-XComposer-VL (InternLM) | **0.568/0.616** | **0.731/0.751** | **0.358/0.413** | **0.619/0.678** | 0.246/0.268 | **0.734/0.777** | 0.540/0.563 |**0.542/0.581**|
| IDEFICS-Instruct (LLaMA-7B) | 0.375/0.400 | 0.474/0.484 | 0.235/0.24 | 0.409/0.428 | 0.244/0.227 | 0.562/0.622 | 0.370/0.373 |0.381/0.396|
| Qwen-VL (QwenLM) | 0.470/0.546 | 0.676/0.669 | 0.298/0.338 | 0.504/0.532 | 0.273/0.284 | 0.617/0.686 | 0.486/0.486 |0.475/0.506|
| Shikra (Vicuna-7B) | 0.314/0.307 | 0.32/0.337 | 0.237/0.241 | 0.322/0.336 | 0.198/0.201 | 0.640/0.661 | 0.324/0.332 |0.336/0.345|
| Otter-v1 (MPT-7B) | 0.406/0.406 | 0.436/0.441 | 0.143/0.142 | -0.008/0.018 | 0.254/0.264 | 0.475/0.481 | **0.557/0.577** |0.323/0.333|
| Kosmos-2 | 0.255/0.281 | 0.644/0.641 | 0.196/0.195 | 0.358/0.368 | 0.210/0.225 | 0.489/0.491 | 0.359/0.365 |0.359/0.367|
| InstructBLIP (Flan-T5-XL) | 0.334/0.362 | 0.582/0.599 | 0.248/0.267 | 0.113/0.113 | 0.167/0.188 | 0.378/0.400 | 0.211/0.179 |0.290/0.301|
| InstructBLIP (Vicuna-7B) | 0.359/0.437 | 0.683/0.689 | 0.200/0.283 | 0.253/0.367 | 0.263/0.304 | 0.629/0.663 | 0.337/0.382 |0.389/0.446|
| VisualGLM-6B (GLM-6B) | 0.247/0.234 | 0.498/0.507 | 0.146/0.154 | 0.110/0.116 | 0.209/0.183 | 0.342/0.349 | 0.127/0.131 |0.240/0.239|
| mPLUG-Owl (LLaMA-7B) | 0.409/0.427 | 0.634/0.644 | 0.241/0.271 | 0.437/0.487 | 0.148/0.180 | 0.687/0.711 | 0.466/0.486 |0.432/0.458|
| LLaMA-Adapter-V2 | 0.354/0.363 | 0.464/0.506 | 0.275/0.329 | 0.298/0.360 | 0.257/0.271 | 0.604/0.666 | 0.412/0.425 |0.381/0.417|
| LLaVA-v1 (Vicuna-13B) | 0.462/0.457 | 0.442/0.462 | 0.264/0.280 | 0.404/0.417 | 0.208/0.237 | 0.626/0.684 | 0.349/0.372 |0.394/0.416|
| MiniGPT-4 (Vicuna-13B) | 0.239/0.257 | 0.238/0.253 | 0.170/0.183 | 0.339/0.340 | 0.252/0.246 | 0.572/0.591 | 0.239/0.233 |0.293/0.300|

Overall, `internlm_xcomposer_vl` has the best IQA performance among the models. (30th Oct) with 6 champions among 7 datasets. `qwen-vl` and `llava-v1.5` are good runner-ups. 

We release the results of these models (as well as the post-evaluation code) in [IQA_results](IQA_outputs/) for reference.


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
