import re

text = "連絡電話: 0912345678，夜間關機。"

a_match=re.search('電話', text)
print(a_match)
# <re.Match object; span=(2, 4), match='電話'>
if a_match:
    print(a_match.group())
    print(a_match.start())
    print(a_match.end())


b_match = re.search(r'09\d{2}-?\d{6}' , text) 
print(b_match)
# <re.Match object; span=(6, 16), match='0912345678'> 
if b_match:
    print(b_match.group())
    print(b_match.start())
    print(b_match.end())







































































































