from pyspark import SparkContext
import time

def word_count(rdd):
    return rdd.flatMap(lambda line: line.split()).count()

def longest_word(rdd):
    return rdd.flatMap(lambda line: line.split()).map(lambda word: (len(word), word)).max()[1]

def word_occurrences(rdd, word):
    return rdd.flatMap(lambda line: line.split()).filter(lambda w: w == word).count()

def word_search(rdd, word):
    return rdd.filter(lambda line: word in line).count()

sc = SparkContext()

rdd = sc.textFile("PA3/Project 3/female.txt")

#take input from user
def take_input():
    words = input("Enter words to search: ")
    return words.split()

search_words = take_input()

# Start time
curr = time.time()

# Word Count
count = word_count(rdd)

# Longest Word
longest = longest_word(rdd)

# Word Occurrences
occurrences = {word: word_occurrences(rdd, word) for word in search_words}

# Word Search
search_results = {word: word_search(rdd, word) for word in search_words}

end = time.time() - curr

# Stop Spark Context
sc.stop()

# Output results
print("Word Count:", count)
print("Longest Word:", longest)
for word, occurrence in occurrences.items():
    print(f"Occurrences of '{word}':", occurrence)
for word, result in search_results.items():
    print(f"Search results of '{word}':", result)
print("time:", end)
