from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def analyze_comment(comments):
    tokenizer = AutoTokenizer.from_pretrained("checkpoint-9500")
    model = AutoModelForSequenceClassification.from_pretrained("checkpoint-9500")

    inputs = tokenizer.encode_plus(comments, return_tensors='pt')
    outputs = model(**inputs)

    _, preds = torch.max(outputs.logits, dim=1)

    sentiment = "positive" if preds[0].item() == 1 else "negative"

    print(f"The sentiment of the sentence '{comments}' is {sentiment}.")

analyze_comment("고사양 게임을 돌릴 때 안정적으로 돌아가고 발열도 적당하다고 느끼고 배터리 오래 가서 굉장히 만족합니다.")
analyze_comment("ㅋㅋ 개멍청해보인다")
