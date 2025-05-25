import sys
from stats import how_many_words
from stats import sort_letters

def main():
    if len(sys.argv) == 2:
        which_text = sys.argv[1]

        wordcount = how_many_words(which_text)
        lettercount = sort_letters(which_text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {which_text}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for letter in lettercount:
            print(f"{letter['char']}: {letter['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

main()
