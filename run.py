from collections import Counter

# Open the file and read the text
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
counter = Counter(words)

# Unique list of words
unique_words = list(counter.keys())
print("Unique Words:", unique_words)

# Counts of each word
word_counts = dict(counter)
print("Word Counts:", word_counts)

# List of words sorted by count
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print("Sorted Word Counts:", sorted_word_counts)


with open('output.txt', 'w', encoding='utf-8') as f:
    for word, count in sorted_word_counts:
        f.write(f"{word}\t{count}\n")
