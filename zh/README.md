# 中文

<div align="center">

  <h1>Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision</h1>

_多模态大模型在低层次计算机视觉上的表现如何？_

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

<a href="https://arxiv.org/abs/2309.14181"><strong>论文</strong></a> |
<a href="https://vqassessment.github.io/Q-Bench"><strong>网站</strong></a> |
     <a href="https://huggingface.co/datasets/nanyangtu/LLVisionQA-QBench"><strong>数据集 (LLVisionQA)</strong></a> |
 <a href="https://huggingface.co/datasets/nanyangtu/LLVisionQA-QBench"><strong>数据集 (LLDescribe)</strong></a> |
<a href="https://github.com/VQAssessment/Q-Bench"><strong>Github</strong></a>

  <div style="width: 80%; text-align: center; margin:auto;">
      <img style="width:80%" src="../qbench.png">
  </div>

</div>

Q-Bench 是一个全新的基准，专门为测试多模态语言模型（MLLMs）在低层次计算机视觉任务中的性能而设计。此基准集中于三个主要领域：感知（A1），描述（A2）和评估（A3）。这些领域分别对应于多模态语言模型在理解和描述视觉信息方面的不同能力。

- 对于感知(A1)/描述(A2)，我们收集了两个基准数据集 LLVisionQA/LLDescribe。
- 我们对这两个任务开放**基于提交的评估**。提交的详细信息如下。
- 对于评估(A3)，由于我们使用**公开数据集**，我们公开提供了一个抽象评估代码，以便测试任意 MLLMs。

## A1/A2 提交指南

## 选择1：提交结果

**重要！我们已经发布这两个任务的数据集，方便大家自行测试后直接提交结果。请参考[数据文档](../data_release)以及[示例代码](../example_code_for_idefics)以顺利测试这些数据。**

**请发送电子邮件至`haoning001@e.ntu.edu.sg`提交您的结果，以json格式存储。**

## 选择2：提交模型

另外，您也可以提交模型。要提交到 Q-Bench (A1/A2)，您可以准备一个 huggingface/GitHub 仓库（带有一些 README，以便我们运行）来实现您的 MLLM，并实现以下功能：

- 基于多模态输入（`图像 + 文本`）生成文本输出。

具体而言，它应该有两个重要的方法：`embed_image_and_text`（允许多模态输入），和`generate`（用于对话）。

我们建议将您的 MLLM 的函数调用封装成以下格式：

```python
from PIL import Image
from my_mllm_model import Model, Tokenizer, embed_image_and_text # [用您的MLLM替换此处]

model, tokenizer = Model(), Tokenizer()

prompt = '[ANY_PROMPT]'

image = Image.open("image_for_query.jpg")
input_embeds = embed_image_and_text(image, prompt)
generated_texts = tokenizer.batch_decode(model.generate(input_embeds=input_embeds))[0]
```

我们还提供了 IDEFICS 的演示实现，这是 hugginface 的开源 MLLM，用于最简单的问答（A1）和描述（A2）。请参见[示例](../example_code_for_idefics/README.md)以了解如何运行演示并为基于提交的评估提供类似的示例。

**如果您在*中国大陆外*，请发送电子邮件至`haoning001@e.ntu.edu.sg`提交您的模型。**
**如果您在*中国大陆内*，请发送电子邮件至`zzc1998@sjtu.edu.cn`提交您的模型。**

## A1: 感知

下面是 MLLM 低级感知能力的 LLVisionQA 基准数据集的快照。

![图片](../llvisionqa.png)

我们将 MLLMs 的答案准确性（提供问题和所有选择）作为这里的度量标准。

## A2: 描述

下面是 MLLM 低级描述能力的 LLDescribe 基准数据集的快照。

![图片](../lldescribe.png)

我们将 MLLM 描述的*完整性*，_准确性_，和*相关性*作为这里的度量标准。

## A3: 评估

_MLLMs 具有预测 IQA 定量分数的令人兴奋的能力！_

### 方法

![图片](../llmiqa.png)

### 抽象代码

#### 预测分数

与上面类似，只要一个模型（基于因果语言模型）具有以下两种方法：`embed_image_and_text`（允许多模态输入），和`forward`（用于计算逻辑），就可以使用该模型实现图像质量评估（IQA）：

```python
from PIL import Image
from my_mllm_model import Model, Tokenizer, embed_image_and_text

model, tokenizer = Model(), Tokenizer()

prompt = "##User: Ratge the quality of the image.\n" \
         "##Assistant: The quality of the image is" ### 此行可以基于MLLM的默认行为进行修改。

good_idx, poor_idx = tokenizer(["good","poor"]).tolist()

image = Image.open("image_for_iqa.jpg")
input_embeds = embed_image_and_text(image, prompt)
output_logits = model(input_embeds=input_embeds).logits[0,-1]
q_pred = (output_logits[[good_idx, poor_idx]] / 100).softmax(0)[0]
```

\*注意，您可以根据您的模型的默认输出格式修改第二行，例如对于 [Shikra 模型](https://github.com/shikras/shikra)，"##Assistant: The quality of the image is" 可以修改为 "##Assistant: The answer is"。如果您的 MLLM 首先回答"好的，我愿意帮忙！图片质量是"，只需将此行替换为 prompt 的第 2 行。

我们进一步在 IQA 上提供了 IDEFICS 的完整实现。请参见[示例](../example_code_for_idefics/README.md)以了解如何使用这个 MLLM 运行 IQA。其他的 MLLM 亦可以以相同方式被改造用于 IQA。

#### 用 IQA 数据库计算 SRCC/PLCC

我们已为我们的基准中评估的七个 IQA 数据库准备了 JSON 格式的质量分数（MOS）。

请参阅[IQA_databases](../a3_iqa_databases/)以获取详细信息。

### IQA 数据库官方结果

请随时在您的作品中使用 Q-Bench 中测试的这些结果。

| **Dataset Type / Model / Dataset** | **In-the-wild: KONiQ-10k** | **In-the-wild: SPAQ** | **In-the-wild: LIVE-FB** | **In-the-wild: LIVE-itw** | **Generated: CGIQA-6K** | **Generated: AGIQA-3K** | **Artificial: KADID-10K** |
| ---------------------------------- | -------------------------- | --------------------- | ------------------------ | ------------------------- | ----------------------- | ----------------------- | ------------------------- |
| NIQE                               | 0.316/0.377                | **0.669/0.693**       | 0.211/**0.288**          | **0.480/0.451**           | 0.075/0.056             | 0.562/0.517             | 0.374/0.428               |
| CLIP-ViT-Large-14                  | **0.468/0.505**            | 0.385/0.389           | 0.218/0.237              | 0.307/0.308               | **0.285/0.290**         | 0.436/0.458             | 0.376/0.388               |
| Shikra (Vicuna-7B)                 | 0.314/0.307                | 0.327/0.337           | 0.237/0.241              | 0.322/0.336               | 0.198/0.201             | **0.640/0.661**         | 0.324/0.332               |
| LLaVA-v1 (Vicuna-13B)              | **0.462/0.457**            | 0.442/0.462           | **0.264/0.280**          | 0.404/0.417               | 0.208/0.237             | 0.626/**0.684**         | 0.349/0.372               |
| MiniGPT-4 (Vicuna-13B)             | 0.239/0.257                | 0.238/0.253           | 0.170/0.183              | 0.339/0.340               | 0.252/0.246             | 0.572/0.591             | 0.239/0.233               |
| Kosmos-2                           | 0.255/0.281                | **0.644/0.641**       | 0.196/0.195              | 0.358/0.368               | 0.210/0.225             | 0.489/0.491             | 0.359/0.365               |
| LLaMA-Adapter-V2                   | 0.354/0.363                | 0.464/0.506           | **0.275/0.329**          | 0.298/0.360               | **0.257/0.271**         | 0.604/**0.666**         | **0.412/0.425**           |
| InstructBLIP (Flan-T5-XL)          | 0.334/0.362                | 0.582/0.599           | **0.248/0.267**          | 0.113/0.113               | 0.167/0.188             | 0.378/0.400             | 0.211/0.179               |
| InstructBLIP (Vicuna-7B)           | 0.359/**0.437**            | **0.683/0.689**       | 0.200/**0.283**          | 0.253/0.367               | **0.263/0.304**         | **0.629/0.663**         | 0.337/0.382               |
| Otter-v1 (MPT-7B)                  | 0.406/0.406                | 0.436/0.441           | 0.143/0.142              | -0.008/0.018              | 0.254/0.264             | 0.475/0.481             | **0.557/0.577**           |
| IDEFICS-Instruct (LLaMA-7B)        | 0.375/0.400                | 0.474/0.484           | 0.235/0.240              | **0.409/0.428**           | 0.244/0.227             | 0.562/0.622             | 0.370/0.373               |
| mPLUG-Owl (LLaMA-7B)               | **0.409/0.427**            | 0.634/**0.644**       | 0.241/0.271              | **0.437/0.487**           | 0.148/0.180             | **0.687/0.711**         | **0.466/0.486**           |

\*评价指标是 _SRCC/PLCC_.

## 联系

Q-Bench 由新加坡南洋理工大学和中国上海交通大学的研究者们开发。如有任何疑问，您可联系主要作者以获取相关信息：

- Haoning Wu, `haoning001@e.ntu.edu.sg`, @teowu
- Zicheng Zhang, `zzc1998@sjtu.edu.cn`, @zzc-1998
- Erli Zhang, `ezhang005@e.ntu.edu.sg`, @ZhangErliCarl

## Citation

如果需要引用本工作，敬请使用下述 bibtex。

```bibtex
@article{wu2023qbench,
    title={Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision},
    author={Wu, Haoning and Zhang, Zicheng and Zhang, Erli and Chen, Chaofeng and Liao, Liang and Wang, Annan and Li, Chunyi and Sun, Wenxiu and Yan, Qiong and Zhai, Guangtao and Lin, Weisi},
    year={2023},
}
```
