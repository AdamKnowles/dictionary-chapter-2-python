# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

# After you have added them, use square bracket notation to output the definition of two of the words to the console.

# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

# """
# Create a dictionary with key value pairs to
# represent words (key) and its definition (value)
# """
# word_definitions = dict()

# """
# Add several more words and their definitions
#    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
# """

# """
# Use square bracket lookup to get the definition of two
# words and output them to the console with `print()`
# """


# """
# Loop over the dictionary to get the following output:
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
# """


word_definitions= dict()
word_definitions["lasix"] = "A loop diuretic that takes fluid systemically and stimulates the kidneys"
word_definitions["ibuprofen"] = "An NSAID that decreases general inflammation in teh muscles"
word_definitions["labetolol"] = "A beta blocker that decreases resistance in the bloodstream by dilating blood vessels"

for (key,value) in word_definitions.items():
    print(f"The definition of {key} is {value}")