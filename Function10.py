def count(sen):
    words = sen.split()
    return len(words)
x="hello world"
r=count(x)
print("number of words in the sentence is :",r)