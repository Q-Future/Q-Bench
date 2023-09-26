# Example Code for Q-Bench

In this folder, we provide example code we use to evaluate [IDEFICS](https://huggingface.co/blog/idefics), the open-source MLLM published by Huggingface. As it does not require any extra dependency other than the `transformers` library, we use it as an example to show how our three tasks in the Q-bench works.

### Running a Demo for Perception (A1) / Description (A2) ability

To run the IDEFICS demo for Q-Bench, you can first install the dependencies:

`shell
pip install pillow
pip install transformers>=4.33.1
`

and then run `python example_code_for_idefics/a1_perception_demo.py` or `python example_code_for_idefics/a2_description_demo.py` to run IDEFICS for LLVisionQA and LLDescribe respectively.

As our evaluation is submission-based, it will be very nice of incoming models to submit with similar simple files as a demo for us to conduct the evaluation. Make sure that your demo can successfully answer the visual question related to `2415943374.jpg`, and describe the low-level information of `midjourney_lowstep_036.jpg` before your submission.


### Evaluating Assessment (A3) ability


As the 7 IQA databases we use in the Q-Bench are open-source, and there is no known strategies for MLLMs to overfit on IQA scores for enormous images, the Assessment (A3) ability can be directly evaluated by any user (including publisher of MLLMs). To run the evaluation code, download all IQA datasets as listed in [IQA databases](../a3_iqa_databases/), additionally install `pip install scipy` in shell, and run the script as follows:

```shell
python example_code_for_idefics/a3_assessment_all.py
```

The results will be stored in the `IQA_outputs/idefics` directory.

## Contact

Please contact any of the first authors of this paper for queries.

- Haoning Wu, `haoning001@e.ntu.edu.sg`
- Zicheng Zhang, `zzc1998@sjtu.edu.cn`
- Erli Zhang, `ezhang005@e.ntu.edu.sg`

## Citation

If you find our work interesting, please feel free to cite our paper:

```bibtex
@article{wu2023qbench,
    title={Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision},
    author={Wu, Haoning and Zhang, Zicheng and Zhang, Erli and Chen, Chaofeng and Liao, Liang and Wang, Annan and Li, Chunyi and Sun, Wenxiu and Yan, Qiong and Zhai, Guangtao and Lin, Weisi},
    year={2023},
}
```
