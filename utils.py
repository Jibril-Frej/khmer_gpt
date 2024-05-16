import torch


def complete_text(input_text, model, tokenizer):
    input_ids = torch.tensor([tokenizer.encode(input_text).ids])
    attention_mask = torch.ones_like(input_ids)
    model.eval()
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=64,
        num_beams=10,
        num_return_sequences=10,
        output_scores=True,
        return_dict_in_generate=True,
    )

    for score, prediction in zip(output.sequences_scores, output.sequences):
        predicted_text = tokenizer.decode(prediction.tolist(), skip_special_tokens=True)
        print(score.numpy(), predicted_text)
