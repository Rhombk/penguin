from ollama import generate

# Streaming response
print("Streaming response:")
for chunk in generate("qwen2.5-coder:0.5b", "What is an info hazard?", stream=True):
    print(chunk["response"], end="", flush=True)
print()
