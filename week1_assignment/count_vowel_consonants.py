# Take input from the user
text = input("Enter a string: ")


vowel_count = 0
consonant_count = 0


vowels = "aeiouAEIOU"


for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
