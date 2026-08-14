'''
Write a function `add_tax(price, rate)` that takes a price (a number) and a tax
rate (a number, e.g. 0.1 for 10%), and returns the total price including tax.

Put it in a new file, e.g. 01-fluency/p1.py. Call the function with a couple of
example values, print() the result, run the file, and paste back both your code
and what printed into the chat.

'''
def add_tax(price,rate):
    tax= price * rate
    price= price+ tax
    return price

print(add_tax(100,2.5))


'''
Write a function `total_cart(cart)` that takes a dictionary mapping item names
(strings) to prices (numbers) — e.g. {"apple": 1.5, "bread": 3.0} — and returns
the sum of all the prices in the cart.

Add it below add_tax in the same file (or a new one, your call). Call it with
your own example dictionary, print() the result, run the file, and paste back
your code and what printed.

'''
def add_cart(cart):
    sum=0
    for item in cart.values():
        sum= sum+ item
    return sum

cart= {"apple": 1.5, "bread": 3.0}
print(add_cart(cart))

'''

Write a function `count_words(words)` that takes a list of strings (words,
possibly with repeats — e.g. ["cat", "dog", "cat", "cat"]) and returns a
dictionary mapping each word to how many times it appeared.

Expected: count_words(["cat", "dog", "cat", "cat"]) -> {"cat": 3, "dog": 1}

Use dict.get(key, 0) inside your loop to read-and-update each word's count —
this is the exact "read current value, add 1, write it back" pattern a rate
limiter uses to count requests per client. Call it with your own example list,
print() the result, run it, and paste your code + output.

'''

def count_words(words):
    count={}
    for word in words:
        count[word]= count.get(word,0)+1
    return count

words= ["cat", "dog", "cat", "cat"]
print(count_words(words))