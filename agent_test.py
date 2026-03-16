from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

# More explicit message format
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Explain AI agents simply"
            }
        ]
    }
]

response = model(messages)

# print(response.content)

print("AI Response:")
print("-" * 50)
print(response.content)
print("-" * 50)
print(f"Token usage: {response.token_usage}") 