import re

text = 'Contact support@example.com or sales@test.org. Call 98765-43210 on 12-11-2026.'

print('match  :', re.match(r'Contact', text).group())
print('search :', re.search(r'\d{2}-\d{2}-\d{4}', text).group())
print('emails :', re.findall(r'[\w.]+@[\w.]+\.\w+', text))
print('phones :', re.findall(r'\d{5}-\d{5}', text))
print('masked :', re.sub(r'\d', '#', text))
