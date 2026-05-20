# MLOps_Assignment_2 by G25AIT2096
Hugging Face Fine-Tuning, Experiment Tracking &amp; Model Deployment.

This project demonstrates an end-to-end machine learning workflow including model training, experiment tracking, model versioning, and inference using Hugging Face Transformers, Weights & Biases, and Kaggle.

Training and Fine-Tuning BERT for Classification
Classfying Goodreads Reviews By Book Genre
By Maria Antoniak, Melanie Walsh, and the AI for Humanists Team
Updated: 2024-11-05

A BERT model is fine tuned on Goodreads reviews from the UCSD Book Graph with the goal of predicting the genre of the book being reviewed. The genres include:
•	poetry
•	comics & graphic
•	fantasy & paranormal
•	history & biography
•	mystery, thriller, & crime
•	romance
•	young adult

## Setup Instructions

Install dependencies:

```bash
ppip install -r /kaggle/working/requirements.txt
```

Run training script:

```bash
mlops-assignment-2-fine-tuning-classification.ipynb
```
Run inference script:

```bash
inference.py
```

## Training Platform

Kaggle Notebook (Public Link):  
https://www.kaggle.com/code/g25ait2096/mlops-assignment-2-fine-tuning-classification/

## Results

| Metric | Value |
|--------|-------|
| Accuracy | 60.31% |
| F1 Score | 60.31% |
| Loss | 2.358 |

## Hugging Face Model

https://huggingface.co/g25ait2096/mlops-finetuned-distilbert

## W&B Project Dashboard

https://wandb.ai/g25ait2096-iitj/MLOps-Assign_2/runs/1at7xmt9?nw=nwuserg25ait2096
