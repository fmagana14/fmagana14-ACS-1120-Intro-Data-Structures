import random

user_quote = input("Your Quote: ")
quote_array = user_quote.split(" ")
random.shuffle(quote_array)
new_quote = " ".join(quote_array)
print(new_quote)