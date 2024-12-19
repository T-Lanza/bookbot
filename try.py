def get_text(path):
    with open(path) as f:
        text = f.read()
    return text

def word_count(text):
    count = len(text.split())
    return count

def sort_on(d):
    return d["num"]

def char_count(text):
    chars = []
    lowered = text.lower()
    for ch in lowered:
        if ch not in chars and ch.isalpha():
            chars.append(ch)
    return chars

def get_chars_dict(text):
    chars = {}
    alphas = char_count(text)
    for c in text:
        lowered = c.lower()
        if lowered in chars and lowered in alphas:
            chars[lowered] += 1
        elif lowered not in chars and lowered in alphas:
            chars[lowered] = 1
    return chars

def make_sorted_list(charst):
    sorted_list = []
    for ch in charst:
        sorted_list.append({"char": ch, "num":charst[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    path = "books/frankenstein.txt"
    title = "Frankenstein, by Mary Shelley"
    text = get_text(path)
    words = word_count(text)
    print(text)
    print("")
    print(f"=========================================================")
    print(f"=========================================================")
    print(f"===== Begin report on {title} =====")
    print(f"=========================================================")
    print("")
    print(f"There were {words} words in this document")
    print("")
    charst = get_chars_dict(text)
    sorted = make_sorted_list(charst)
    for item in sorted: 
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("")
    print(f"=========================================================")
    print(f"===================== End of Report =====================")
    print(f"=========================================================")
    print(f"=========================================================")

main()