from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def summarize(path=r'F:\works\A-important\A-neurals\GenAi-Verse\yt-video-summarization\Data\my_file.txt'):
    model_id = "nvidia/Llama3-ChatQA-1.5-8B"
    tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=r'D:\hugging-models')
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto", cache_dir=r'D:\hugging-models')

    with open(path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    messages = [
        {"role": "user", "content": "Please summarize the following transcript with bullet points and provide any relevant code snippets if necessary, it should be so easy to understand and student use this notes so make it students friendly"},
        {"role": "assistant", "content": transcript}
    ]

    def get_formatted_input(messages, context=""):
        system = "System: This is a chat between a user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions based on the context. The assistant should also indicate when the answer cannot be found in the context and  it should be so easy to understand and student use this notes so make it students friendly."
        conversation = '\n\n'.join(["User: " + item["content"] if item["role"] == "user" else "Assistant: " + item["content"] for item in messages]) + "\n\nAssistant:"
        formatted_input = system + "\n\n" + conversation

        return formatted_input

    formatted_input = get_formatted_input(messages)
    tokenized_prompt = tokenizer(tokenizer.bos_token + formatted_input, return_tensors="pt").to(model.device)

    eos_token_id = tokenizer.eos_token_id

    outputs = model.generate(
        input_ids=tokenized_prompt.input_ids,
        attention_mask=tokenized_prompt.attention_mask,
        max_new_tokens=1024,
        eos_token_id=eos_token_id
    )

    response = outputs[0][tokenized_prompt.input_ids.shape[-1]:]
    summary = tokenizer.decode(response, skip_special_tokens=True)
    print(summary)
    with open(r'Data\my_file.txt', 'w') as f:
        f.write(summary)

summarize()
