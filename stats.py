def num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    chars = {}
    for c in text:
        if c.lower() not in chars:
            chars[c.lower()] = 1
        else:
            chars[c.lower()] += 1
    return chars

def sorted_dictionary(chars):
    sorted_items = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    result = []
    for char, count in sorted_items:
        sorted_dict = {"char": char, "count":  count}
        result.append(sorted_dict)
    return result
