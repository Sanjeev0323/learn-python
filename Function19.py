def words(s):
    word=s.split()
    return len(word)
n=input("Enter sentence: ")
print(words(n))