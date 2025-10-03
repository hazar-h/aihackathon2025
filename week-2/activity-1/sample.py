from openai import OpenAI

client = OpenAI(
    api_key="sk_",                # your proxy key from DynamoDB
    base_url="https://openai.dplit.com/v1"       # your proxy URL
)

resp = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":"Ping"}],
    max_tokens=64
)
print(resp.choices[0].message.content)