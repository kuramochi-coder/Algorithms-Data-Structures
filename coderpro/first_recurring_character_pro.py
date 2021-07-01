
def first_recurring_character(str):
    seen = set()

    for c in str:
        if c in seen:
            return c
        seen.add(c)

    return None


print(first_recurring_character('qwertty'))
# t

print(first_recurring_character('qwerty'))
# None