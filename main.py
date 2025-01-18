from package_creation_tutorial.string_ops import capitalize_words, count_vowels, reverse_string
def main():
 """
 Main function to demonstrate the string operations.
 """
 test_string: str = "hello world"

 print(f"Original string: {test_string}")
 print(f"Reversed: {reverse_string(test_string)}")
 print(f"Vowel count: {count_vowels(test_string)}")
 print(f"Capitalized: {capitalize_words(test_string)}")
if __name__ == "__main__":
 main()
