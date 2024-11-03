INITIAL_STATE = 'q0'
ACCEPTING_STATE = 'q2'
TRANSITIONS = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
def process_string(test_strings):
    current_state = INITIAL_STATE
    for char in test_strings:
        if char in TRANSITIONS.get(current_state, {}):
            current_state = TRANSITIONS[current_state][char]
        else:
            current_state = INITIAL_STATE  
    return current_state == ACCEPTING_STATE
test_strings = ["ab", "aab", "bab", "bbaaab", "a", "b", "abc"]
for string in test_strings:
    if process_string(string):
        print(f"'{string}' is accepted by the FSA.")
    else:
        print(f"'{string}' is not accepted by the FSA.")
