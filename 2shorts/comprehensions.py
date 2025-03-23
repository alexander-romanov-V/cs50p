import csv
import re


def main():
    words = get_words("2shorts/address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    # counts = {}
    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1

    save_counts(counts)







def get_words(filename):
    with open(filename, "r") as f:
        contents = f.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


main()