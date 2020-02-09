import re

patterns = ["term1", "term2"]

text = "This is a string with term1, not the other!"

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH")
    else:
        print("NO MATCH!")


re.findall("match", "test phrase match in match middle")

text = "term1"
match = re.search("term1", text)
print(match.start())

split_term = "@"
email = "user@gmail.com"
print(re.split(split_term, email))


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = "sdsd..sssddd..sddsddd...dsds...dssssss...sddddd"

test_pattern = ["sd*"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["sd+"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["sd?"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["sd(1,3)"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["s[sd]+"]
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string! But is has punctuation. How can we remove it?"

test_pattern = ["[^!.?]+"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["[a-z]+"]
multi_re_find(test_pattern, test_phrase)

test_pattern = ["[A-Z]+"]
multi_re_find(test_pattern, test_phrase)

test_pattern = [r"\D+"]
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 12312 and a symbol #hastag"

test_pattern = [r"\S+"]
multi_re_find(test_pattern, test_phrase)
