from openai import OpenAI
API_KEY = "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"
client = OpenAI(api_key = API_KEY)

def askGPT(prompt) -> str:
  completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )
  result = completion.choices[0].message.content
  print(result)
  return result