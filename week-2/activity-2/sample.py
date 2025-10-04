from openai import OpenAI

client = OpenAI()  # reads env: OPENAI_API_KEY (+ OPENAI_BASE_URL if set)

resp = client.chat.completions.create(
    model="gpt-4o-mini",            # low-cost, solid default
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Give me 3 quick facts about the Moon."}
    ],
    max_tokens=150                  # cap output size to control cost
)

print(resp.choices[0].message.content)