import re
def fopc_parser(expression):
    operators = set(['AND', 'OR', 'NOT', 'IMPLIES'])
    tokens = re.split(r'(\s+|\(|\))', expression)
    tokens = [token for token in tokens if token.strip()]
    parsed = []
    for token in tokens:
        if token in operators:
            parsed.append({'type': 'operator', 'value': token})
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
            parsed.append({'type': 'operand', 'value': token})
        elif token in ('(', ')'):
            parsed.append({'type': 'parenthesis', 'value': token})
    return parsed
expression = "(A AND B) IMPLIES (C OR D)"
print(fopc_parser(expression))
