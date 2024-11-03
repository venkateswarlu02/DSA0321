import re
def rule_based_pos_tagging(text):
    rules = [
        (r'.*ing$', 'VBG'),
        (r'.*ed$', 'VBD'),
        (r'.*es$', 'VBZ'),
        (r'.*ould$', 'MD'),
        (r'.*\'s$', 'POS'),
        (r'.*s$', 'NNS'),
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
        (r'.*', 'NN')
    ]
    tokens = text.split()
    tagged_tokens = []
    for token in tokens:
        for pattern, tag in rules:
            if re.match(pattern, token):
                tagged_tokens.append((token, tag))
                break    
    return tagged_tokens
text = "He is running and eats apples."
print(rule_based_pos_tagging(text))
