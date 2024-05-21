# #print vowels and positions in a string
# string='rikujntfwgvjkirnbolepqncxznjofwxnfxolzmfxpw'
# for i in range(len(string)):
#     if string[i]=='a' or string[i]=='e' or string[i]=='i'or string[i]=='o' or string[i]=='u':
#         print(f'{string[i]} at position {i}')





string='rikujntfwgvjkirnbolepqncxznjofwxnfxolzmfxpw'
vowel='aeiou'

for i in range( len(string)):
    if string[i] in vowel:
        print(string[i],i)
    