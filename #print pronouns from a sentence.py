#print  pronouns from a sentence
# example-----

# input-
# We looked for Britney at her house, but she wasn't there.
# output-
# ['we','her','she']
# take the input using input function

a = "We looked for Britney at her house, but she wasn't there"
b = []
words = a.split()
pronouns = ['I', 'me', 'you', 'he', 'him', 'she', 'her', 'it', 'we', 'they', 'them']

for word in words:
    if word in pronouns:
        b.append(word)
print(b)

 
