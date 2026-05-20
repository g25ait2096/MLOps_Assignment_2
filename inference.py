from transformers import pipeline

classifier = pipeline(
"text-classification",
model="g25ait2096/mlops-finetuned-distilbert"
)

text = "Looks good! We can see that overall, our model is assigning the correct labels for each genre."

result = classifier(text)

print(result)
