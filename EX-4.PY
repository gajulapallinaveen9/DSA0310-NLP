VOWELS = 'aeiou'

def pluralize(noun):
    noun = noun.lower()
    if noun.endswith(('ch', 'sh')) or noun[-1] in 'sxz':
        state = 'SIBILANT'
    elif noun[-1] == 'y':
        state = 'Y_AFTER_VOWEL' if noun[-2] in VOWELS else 'Y_AFTER_CONSONANT'
    else:
        state = 'REGULAR'
    action = {
        'SIBILANT': noun + 'es',
        'Y_AFTER_CONSONANT': noun[:-1] + 'ies',
        'Y_AFTER_VOWEL': noun + 's',
        'REGULAR': noun + 's',
    }
    return action[state], state

for n in ['cat', 'bus', 'box', 'church', 'dish', 'city', 'boy', 'baby']:
    plural, st = pluralize(n)
    print(f'{n:8} -> {plural:10} [{st}]')
