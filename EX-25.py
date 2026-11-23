# pip install openai
# set the key first:  export OPENAI_API_KEY='your-key'   (Windows: set OPENAI_API_KEY=your-key)
from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY from the environment

prompt = 'Write a two-line poem about artificial intelligence.'
response = client.completions.create(
    model='gpt-3.5-turbo-instruct',
    prompt=prompt,
    max_tokens=60,
    temperature=0.7,
)
print('Prompt   :', prompt)
print('Response :', response.choices[0].text.strip())
