# Track 6: Choosing and adapting models

Most AI engineering is picking the right model and measuring it, not training one. This track
teaches that order: **compare models → compare embeddings → fine tune only when prompting isn't enough.**

| Project | Skill |
| --- | --- |
| M1 model selection | compare 3 local models on quality, speed, memory; pick one with evidence |
| M2 embedding comparison | which embedding model finds the right chunk on YOUR data |
| M3 LoRA fine tune | a small classifier with LoRA on a free GPU, compared with prompting |

## Budget rules for this track
- M1 and M2 run on your laptop with Ollama. $0.
- M3 runs on **Kaggle Notebooks** (free GPU, phone verification, no card). Google Colab free is a
  backup. Do not rent a GPU (SageMaker, RunPod, Lambda) for this lab: it isn't needed, and an
  instance left running is exactly how a surprise bill happens.
- Check the free GPU quota on Kaggle before you start; it resets weekly.
