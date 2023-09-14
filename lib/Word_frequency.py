import string

def word_frequency(sentence):
  words = sentence.lower().split()
  words = [word.strip(string.punctuation) for word in words]
  frequency = {}

  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1

    return frequency


# Path: lib/Word_frequency_test.py
sentence = "This is a test sentence. This sentence is a test"
result = word_frequency(sentence)
print(result)






