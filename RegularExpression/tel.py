import re

text = "連絡電話: 0912345678，夜間關機。"

a_match=re.search('電話', text)
print(a_match)
# <re.Match object; span=(2, 4), match='電話'>
if a_match:
    print(a_match.group())
    print(a_match.start())
    print(a_match.end())


b_match = re.search(r'(?:0|886-?)9\d{2}-?\d{6}' , text) # Non-capturing Group 
print(b_match)
# <re.Match object; span=(6, 16), match='0912345678'> 
if b_match:
    print(b_match.group()) # group0
    print(b_match.start())
    print(b_match.end())

'''
    Using (?:) to not capture the group
    Cannot to be gotten by b_match.group(1)

    Matches if it is:
    0912345678
    0912-345678 
    886-912345678
    886912345678
    886912-345678
    886-912-345678
    ...
'''






































































































