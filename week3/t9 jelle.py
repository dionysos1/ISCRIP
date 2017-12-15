import re

key_chars = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')


def t9(word: str) -> str:
    result = ""

    # Go over every char in the word
    for char in word:
        # Go over all keys
        for key_char in key_chars:
            # If our lowercased char is in the key add it to output
            if re.search("[%s]" % char.lower(), key_char):
                result += str(key_chars.index(key_char) + 2)
                break

    return result


def mobile_synonyms(a: str, b: str) -> bool:
    return t9(a) == t9(b)


def main():
    print(t9('Hallo'))
    print(t9('aanbod'))
    print(t9('bamboe'))

    print(mobile_synonyms('aanbod', 'bamboe'))
    print(mobile_synonyms('maandag', 'vrijdag'))

if __name__ == "__main__":
    main()
