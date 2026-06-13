import sys

stop_words = {
    "a",
    "an",
    "the",
    "is",
    "in",
    "of",
    "to",
    "and"
}


def read_file(path):
    with open(path, "r") as file:
        return file.read()


def clean_text(text):

    punctuation = ".,!?;:()[]{}\"'"

    text = text.lower()

    for char in punctuation:
        text = text.replace(char, "")

    return text


def count_words(text):

    words = text.split()

    word_counts = {}

    for word in words:

        if word in stop_words:
            continue

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def get_top_n(word_counts, n):

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:n]


def print_chart(top_words):

    print("\nWORD FREQUENCY CHART\n")

    for word, count in top_words:
        print(f"{word:15} {'*' * count} ({count})")


if len(sys.argv) < 2:
    print("Usage: python analyzer.py sample.txt --top 10")
    exit()

file_name = sys.argv[1]

top_n = 10

if "--top" in sys.argv:
    index = sys.argv.index("--top")
    top_n = int(sys.argv[index + 1])

text = read_file(file_name)

text = clean_text(text)

unique_words = set(text.split())

word_counts = count_words(text)

top_words = get_top_n(word_counts, top_n)

print("Vocabulary Size:", len(unique_words))

print_chart(top_words)