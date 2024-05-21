#program to remove whitespaces from a sentence

sentence = "   Hello    world!   "
result = ""
for char in sentence:
    if char != ' ':
        result += char

print("Original sentence:", sentence)
print("Sentence without whitespaces:", result)
