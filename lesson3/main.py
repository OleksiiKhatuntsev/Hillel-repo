# input_example = input("Enter name: ")
# example_string = "Alex"
# result = f"Word {input_example} has {len(input_example)} letters"
# result_format = "Word {word} has {len_word} letters".format(word=input_example, len_word=len(input_example))
# print(result_format)
print(f"Word '{(input_word := input('Enter your word here: '))}' has {len(input_word)} letters.")