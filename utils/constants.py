qwen_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "system": "You are a helpful assistant.",
}

gemma_template = {
    "system_format": "<bos>",
    "user_format": "<start_of_turn>user\n{content}<end_of_turn>\n<start_of_turn>model\n",
    "assistant_format": "{content}<eos>\n",
    "system": None,
}

yi_template = {
    "system_format": "<|im_start|>system\n{content}<|im_end|>\n",
    "user_format": "<|im_start|>user\n{content}<|im_end|>\n<|im_start|>assistant\n",
    "assistant_format": "{content}<|im_end|>\n",
    "system": None
}

zephyr_template = {
    "system_format": "<|system|>\n{content}</s>",
    "user_format": "<|user|>\n{content}</s>\n<|assistant|>\n",
    "assistant_format": "{content}</s>\n",
    "system": None
}

mistral_template = {
    "system_format": "<s>",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content}</s>",
    "system": "",
}

mixtral_template={
    "system_format": "<s>",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content}</s>",
    "system": "",
}

llama2_template = {
    "system_format": "<<SYS>>\n{content}\n<</SYS>>\n\n",
    "user_format": "[INST]{content}[/INST]",
    "assistant_format": "{content} </s>",
    "system": "You are a helpful, respectful and honest assistant. "
    "Always answer as helpfully as possible, while being safe. "
    "Your answers should not include any harmful, unethical, "
    "racist, sexist, toxic, dangerous, or illegal content. "
    "Please ensure that your responses are socially unbiased and positive in nature.\n\n"
    "If a question does not make any sense, or is not factually coherent, "
    "explain why instead of answering something not correct. "
    "If you don't know the answer to a question, please don't share false information.",
}

llama3_template= {
    "system_format": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{content}<|eot_id|>",
    "user_format": "<|start_header_id|>user<|end_header_id|>\n\n{content}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "assistant_format": "{content}<|eot_id|>",
    "system": None,
}

phi3_template = {
    "system_format": None,
    "user_format": "<|user|>\n{content}<|end|>\n<|assistant|>",
    "assistant_format": "{content}<|end|>\n",
    "system": None,
}


model2template = {
    # Qwen1.5
    "Qwen/Qwen1.5-0.5B": qwen_template,
    "Qwen/Qwen1.5-0.5B-Chat": qwen_template,
    "Qwen/Qwen1.5-1.8B": qwen_template,
    "Qwen/Qwen1.5-1.8B-Chat": qwen_template,
    "Qwen/Qwen1.5-4B": qwen_template,
    "Qwen/Qwen1.5-4B-Chat": qwen_template,
    "Qwen/Qwen1.5-7B": qwen_template,
    "Qwen/Qwen1.5-7B-Chat": qwen_template,
    "Qwen/Qwen1.5-14B": qwen_template,
    "Qwen/Qwen1.5-14B-Chat": qwen_template,
    # Qwen2
    "Qwen/Qwen2-0.5B": qwen_template,
    "Qwen/Qwen2-0.5B-Instruct": qwen_template,
    "Qwen/Qwen2-1.5B": qwen_template,
    "Qwen/Qwen2-1.5B-Instruct": qwen_template,
    "Qwen/Qwen2-7B": qwen_template,
    "Qwen/Qwen2-7B-Instruct": qwen_template,
    # Qwen2.5
    "Qwen/Qwen2.5-0.5B": qwen_template,
    "Qwen/Qwen2.5-0.5B-Instruct": qwen_template,
    "Qwen/Qwen2.5-1.5B": qwen_template,
    "Qwen/Qwen2.5-1.5B-Instruct": qwen_template,
    "Qwen/Qwen2.5-3B": qwen_template,
    "Qwen/Qwen2.5-3B-Instruct": qwen_template,
    "Qwen/Qwen2.5-7B": qwen_template,
    "Qwen/Qwen2.5-7B-Instruct": qwen_template,
    "Qwen/Qwen2.5-14B": qwen_template,
    "Qwen/Qwen2.5-14B-Instruct": qwen_template,
    # Yi
    "01-ai/Yi-6B": yi_template,
    "01-ai/Yi-6B-Chat": yi_template,
    "01-ai/Yi-9B": yi_template,
    # Yi 1.5
    "01-ai/Yi-1.5-6B": yi_template,
    "01-ai/Yi-1.5-6B-Chat": yi_template,
    "01-ai/Yi-1.5-9B": yi_template,
    "01-ai/Yi-1.5-9B-Chat": yi_template,
    # Mistral
    "mistralai/Mistral-7B-v0.1": mistral_template,
    "mistralai/Mistral-7B-v0.3": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.1": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.2": mistral_template,
    "mistralai/Mistral-7B-Instruct-v0.3": mistral_template,
    # Gemma
    "google/gemma-2b": gemma_template,
    "google/gemma-2b-it": gemma_template,
    "google/gemma-7b": gemma_template,
    "google/gemma-7b-it": gemma_template,
    # Gemma2
    "google/gemma-2-2b": gemma_template,
    "google/gemma-2-2b-it": gemma_template,
    "google/gemma-2-9b": gemma_template,
    "google/gemma-2-9b-it": gemma_template,
    # Zephyr
    "HuggingFaceH4/zephyr-7b-alpha": zephyr_template,
    "HuggingFaceH4/zephyr-7b-beta": zephyr_template,
    # Llama2
    "meta-llama/Llama-2-7b-hf": llama2_template,
    "meta-llama/Llama-2-7b-chat-hf": llama2_template,
    "meta-llama/Llama-2-13b-hf": llama2_template,
    "meta-llama/Llama-2-13b-chat-hf": llama2_template,
    # Llama3
    "meta-llama/Meta-Llama-3-8B": llama3_template,
    "meta-llama/Meta-Llama-3-8B-Instruct": llama3_template,
    # Llama3.1
    "meta-llama/Meta-Llama-3.1-8B": llama3_template,
    "meta-llama/Meta-Llama-3.1-8B-Instruct": llama3_template,
    # phi3
    "microsoft/Phi-3.5-mini-instruct": phi3_template,
    "microsoft/Phi-3-mini-4k-instruct": phi3_template,
    "microsoft/Phi-3-small-8k-instruct": phi3_template,
    "microsoft/Phi-3-medium-4k-instruct": phi3_template,
}

model2size = {
    # Qwen1.5
    "Qwen/Qwen1.5-0.5B": 620_000_000,
    "Qwen/Qwen1.5-0.5B-Chat": 620_000_000,
    "Qwen/Qwen1.5-1.8B": 1_840_000_000,
    "Qwen/Qwen1.5-1.8B-Chat": 1_840_000_000,
    "Qwen/Qwen1.5-4B": 3_950_000_000,
    "Qwen/Qwen1.5-4B-Chat": 3_950_000_000,
    "Qwen/Qwen1.5-7B": 7_720_000_000,
    "Qwen/Qwen1.5-7B-Chat": 7_720_000_000,
    "Qwen/Qwen1.5-14B": 14_200_000_000,
    "Qwen/Qwen1.5-14B-Chat": 14_200_000_000,
    # Qwen2
    "Qwen/Qwen2-0.5B": 494_000_000,
    "Qwen/Qwen2-0.5B-Instruct": 494_000_000,
    "Qwen/Qwen2-1.5B": 1_540_000_000,
    "Qwen/Qwen2-1.5B-Instruct": 1_540_000_000,
    "Qwen/Qwen2-7B": 7_620_000_000,
    "Qwen/Qwen2-7B-Instruct": 7_620_000_000,
    # Qwen2.5
    "Qwen/Qwen2.5-0.5B": 494_000_000,
    "Qwen/Qwen2.5-0.5B-Instruct": 494_000_000,
    "Qwen/Qwen2.5-1.5B": 1_540_000_000,
    "Qwen/Qwen2.5-1.5B-Instruct": 1_540_000_000,
    "Qwen/Qwen2.5-3B": 3_090_000_000,
    "Qwen/Qwen2.5-3B-Instruct": 3_090_000_000,
    "Qwen/Qwen2.5-7B": 7_620_000_000,
    "Qwen/Qwen2.5-7B-Instruct": 7_620_000_000,
    "Qwen/Qwen2.5-14B": 14_800_000_000,
    "Qwen/Qwen2.5-14B-Instruct": 14_800_000_000,
    # Yi
    "01-ai/Yi-6B": 6_060_000_000,
    "01-ai/Yi-6B-Chat": 6_060_000_000,
    "01-ai/Yi-9B": 8_830_000_000,
    # Yi 1.5
    "01-ai/Yi-1.5-6B": 6_060_000_000,
    "01-ai/Yi-1.5-6B-Chat": 6_060_000_000,
    "01-ai/Yi-1.5-9B": 8_830_000_000,
    "01-ai/Yi-1.5-9B-Chat": 8_830_000_000,
    # Mistral
    "mistralai/Mistral-7B-v0.1": 7_240_000_000,
    "mistralai/Mistral-7B-v0.3": 7_250_000_000,
    "mistralai/Mistral-7B-Instruct-v0.1": 7_240_000_000,
    "mistralai/Mistral-7B-Instruct-v0.2": 7_240_000_000,
    "mistralai/Mistral-7B-Instruct-v0.3": 7_250_000_000,
    # Gemma
    "google/gemma-2b": 2_510_000_000,
    "google/gemma-2b-it": 2_510_000_000,
    "google/gemma-7b": 8_540_000_000,
    "google/gemma-7b-it": 8_540_000_000,
    # Gemma2
    "google/gemma-2-2b": 2_610_000_000,
    "google/gemma-2-2b-it": 2_610_000_000,
    "google/gemma-2-9b": 9_240_000_000,
    "google/gemma-2-9b-it": 9_240_000_000,
    # Zephyr
    "HuggingFaceH4/zephyr-7b-alpha": 7_240_000_000,
    "HuggingFaceH4/zephyr-7b-beta": 7_240_000_000,
    # Llama2
    "meta-llama/Llama-2-7b-hf": 6_740_000_000,
    "meta-llama/Llama-2-7b-chat-hf": 6_740_000_000,
    "meta-llama/Llama-2-13b-hf": 13_000_000_000,
    "meta-llama/Llama-2-13b-chat-hf": 13_000_000_000,
    # Llama3
    "meta-llama/Meta-Llama-3-8B": 8_030_000_000,
    "meta-llama/Meta-Llama-3-8B-Instruct": 8_030_000_000,
    # Llama3.1
    "meta-llama/Meta-Llama-3.1-8B": 8_030_000_000,
    "meta-llama/Meta-Llama-3.1-8B-Instruct": 8_030_000_000,
    # phi3
    "microsoft/Phi-3.5-mini-instruct": 3_820_000_000,
    "microsoft/Phi-3-mini-4k-instruct": 3_820_000_000,
    "microsoft/Phi-3-small-8k-instruct": 7_390_000_000,
    "microsoft/Phi-3-medium-4k-instruct": 14_000_000_000,
}

model2base_model = {
    # Qwen1.5
    "Qwen/Qwen1.5-0.5B": "qwen1.5",
    "Qwen/Qwen1.5-0.5B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-1.8B": "qwen1.5",
    "Qwen/Qwen1.5-1.8B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-4B": "qwen1.5",
    "Qwen/Qwen1.5-4B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-7B": "qwen1.5",
    "Qwen/Qwen1.5-7B-Chat": "qwen1.5",
    "Qwen/Qwen1.5-14B": "qwen1.5",
    "Qwen/Qwen1.5-14B-Chat": "qwen1.5",
    # Qwen2
    "Qwen/Qwen2-0.5B": "qwen1.5",
    "Qwen/Qwen2-0.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2-1.5B": "qwen1.5",
    "Qwen/Qwen2-1.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2-7B": "qwen1.5",
    "Qwen/Qwen2-7B-Instruct": "qwen1.5",
    # Qwen2.5
    "Qwen/Qwen2.5-0.5B": "qwen1.5",
    "Qwen/Qwen2.5-0.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2.5-1.5B": "qwen1.5",
    "Qwen/Qwen2.5-1.5B-Instruct": "qwen1.5",
    "Qwen/Qwen2.5-3B": "qwen1.5",
    "Qwen/Qwen2.5-3B-Instruct": "qwen1.5",
    "Qwen/Qwen2.5-7B": "qwen1.5",
    "Qwen/Qwen2.5-7B-Instruct": "qwen1.5",
    "Qwen/Qwen2.5-14B": "qwen1.5",
    "Qwen/Qwen2.5-14B-Instruct": "qwen1.5",
    # Yi
    "01-ai/Yi-6B": "yi",
    "01-ai/Yi-6B-Chat": "yi",
    "01-ai/Yi-9B": "yi",
    # Yi 1.5
    "01-ai/Yi-1.5-6B": "yi",
    "01-ai/Yi-1.5-6B-Chat": "yi",
    "01-ai/Yi-1.5-9B": "yi",
    "01-ai/Yi-1.5-9B-Chat": "yi",
    # Mistral
    "mistralai/Mistral-7B-v0.1": "mistral",
    "mistralai/Mistral-7B-v0.3": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.1": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.2": "mistral",
    "mistralai/Mistral-7B-Instruct-v0.3": "mistral",
    # Gemma
    "google/gemma-2b": "gemma",
    "google/gemma-2b-it": "gemma",
    "google/gemma-7b": "gemma",
    "google/gemma-7b-it": "gemma",
    # Gemma2
    "google/gemma-2-2b": "gemma",
    "google/gemma-2-2b-it": "gemma",
    "google/gemma-2-9b": "gemma",
    "google/gemma-2-9b-it": "gemma",
    # Zephyr
    "HuggingFaceH4/zephyr-7b-alpha": "zephyr",
    "HuggingFaceH4/zephyr-7b-beta": "zephyr",
    # Llama2
    "meta-llama/Llama-2-7b-hf": "llama2",
    "meta-llama/Llama-2-7b-chat-hf": "llama2",
    "meta-llama/Llama-2-13b-hf": "llama2",
    "meta-llama/Llama-2-13b-chat-hf": "llama2",
    # Llama3
    "meta-llama/Meta-Llama-3-8B": "llama3",
    "meta-llama/Meta-Llama-3-8B-Instruct": "llama3",
    # Llama3.1
    "meta-llama/Meta-Llama-3.1-8B": "llama3",
    "meta-llama/Meta-Llama-3.1-8B-Instruct": "llama3",
    # phi3
    "microsoft/Phi-3.5-mini-instruct": "phi3",
    "microsoft/Phi-3-mini-4k-instruct": "phi3",
    "microsoft/Phi-3-small-8k-instruct": "phi3",
    "microsoft/Phi-3-medium-4k-instruct": "phi3",
}
