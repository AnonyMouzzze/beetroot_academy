def balanced_brackets(string: str) -> bool:
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    } 

    opened_brackets = []
    closed_brackets = []
    for bracket in string:
        if bracket in brackets:
            opened_brackets.append(bracket)
        elif bracket in brackets.values():
            closed_brackets.append(bracket)

    if len(closed_brackets) != len(opened_brackets):
        return False

    for bracket in opened_brackets:
        if brackets[bracket] in closed_brackets:
            opened_brackets.remove(bracket)
            closed_brackets.remove(brackets[bracket])
            continue
        return False
    return True