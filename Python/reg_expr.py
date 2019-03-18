import re

patterns = ['term1', 'term2']

text  = "term1"

split_term = "@"
email = "user@gmail.com"

# for pattern in patterns:
#   print("I am searching for: "+pattern)

#   if re.search(pattern,text):
#     print("Match")
#   else:
#     print("No matcht")

match = re.search('term1',text)
# print(match.start())

# split = re.split(split_term,email)
# print(re.split(split_term,email))

# print(re.findall('match','test phrase match in middle, match'))

def multi_re_find(patterns,phrase):
  for pat in patterns:
    print("Searching for pattern {}".format(pat))
    print(re.findall(pat,phrase))
    print("\n")

test_phrase_one = "sdsdsd...sssddd..ssdddddsdddd...ddsss..sdd"

# test_pattern = ["sd*"]
# test_pattern = ["sd+"]
# test_pattern = ["sd?"]
# test_pattern = ["sd{2,3}"]
test_pattern_one = ["s[sd]+"]

# multi_re_find(test_pattern_one,test_phrase_one)


test_phrase = "This is a string! But it has punctuation. How do we remove it?"

test_pattern = ["[^!.?]+"]
multi_re_find(test_pattern,test_phrase)
test_pattern = ['[a-z]+']
multi_re_find(test_pattern,test_phrase)

test_phrase = "Numbers here 12345 and a symbol #"
test_pattern = [r'\D+']
multi_re_find(test_pattern,test_phrase)
test_pattern = [r'\d+']
multi_re_find(test_pattern,test_phrase)
test_pattern = [r'\S+']
multi_re_find(test_pattern,test_phrase)
test_pattern = [r'\W+']
multi_re_find(test_pattern,test_phrase)
