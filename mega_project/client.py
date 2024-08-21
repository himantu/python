from openai import OpenAI

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Maya skilled in general task like Alexa and Google Cloud."},
    {"role": "user", "content": "What is coding?"}
  ]
)

print(completion.choices[0].message.content)