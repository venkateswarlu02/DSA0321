import nltk
from nltk import RegexpTokenizer
def pluralize(noun, tokenizer=RegexpTokenizer(r'\b\w+\b'), rules=[
    ('(s|ss|sh|ch|x|z)$', r'\1es'),
    ('([^aeiou])y$', r'\1ies'),
    ('(o)$', r'\1es'),
    ('(.*[^s])$', r'\1s')
]):
    tokens = tokenizer.tokenize(noun.lower())
    if tokens:
        singular = tokens[0]
        for pattern, replacement in rules:
            if nltk.re.search(pattern + '$', singular):
                return nltk.re.sub(pattern + '$', replacement, singular)
    return singular 
pluralization_fsa = {
    'states': ['start', 's_ss_sh_ch_x_z', 'consonant_y', 'o', 'other'],
    'transitions': [
        ('start', 's_ss_sh_ch_x_z', r'(s|ss|sh|ch|x|z)$'),
        ('start', 'consonant_y', r'([^aeiou])y$'),
        ('start', 'o', r'o$'),
        ('start', 'other', r'.*[^s]$'),
        ('s_ss_sh_ch_x_z', 'start', 'add "es"'),
        ('consonant_y', 'start', 'change "y" to "ies"'),
        ('o', 'start', 'add "es"'),
        ('other', 'start', 'add "s"')
    ]
}
def print_fsa(fsa):
    print("Pluralization Finite State Automaton:")
    print("\nStates:")
    for state in fsa['states']:
        print(f"- {state}")

    print("\nTransitions:")
    for transition in fsa['transitions']:
        print(f"- From {transition[0]} to {transition[1]}: {transition[2]}")
singular_nouns = ["cat", "dog", "tree", "boy", "city", "baby", "potato", "tomato", "book", "pen", "bus", "box",
                  "church", "buzz", "kiss", "dish"]
print("\nPluralization Results:")
for noun in singular_nouns:
    plural = pluralize(noun)
    print(f"Singular: {noun}  =>  Plural: {plural}")
print_fsa(pluralization_fsa)
