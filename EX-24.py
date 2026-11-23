import re

RULES = [
    ('Greeting', r'^(hi|hello|hey|good (morning|evening))\b'),
    ('Thanks',   r'\b(thanks|thank you)\b'),
    ('Goodbye',  r'\b(bye|goodbye|see you)\b'),
    ('Request',  r'^(please|can you|could you|would you)\b'),
    ('Accept',   r'^(yes|yeah|sure|ok|okay)\b'),
    ('Question', r'^(who|what|when|where|why|how|is|are|do|does)\b|\?$'),
]

def dialog_act(utterance):
    u = utterance.lower().strip()
    for label, pattern in RULES:
        if re.search(pattern, u):
            return label
    return 'Statement'

dialog = [
    ('A', 'Hello!'),
    ('B', 'How can I help you?'),
    ('A', 'Can you book a table for two tonight?'),
    ('B', 'Sure, what time?'),
    ('A', 'Around 8 pm.'),
    ('B', 'Done. Your table is booked.'),
    ('A', 'Thank you so much!'),
    ('B', 'Goodbye!'),
]
for speaker, utt in dialog:
    print(f'{speaker}: {utt}  =>  {dialog_act(utt)}')
