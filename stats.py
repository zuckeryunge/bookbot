def get_book_text(which_text):
    with open(which_text) as f:
        fs_book = f.read()
        return fs_book

def how_many_words(which_text):
    return len(get_book_text(which_text).split())

def count_letters(which_text):
    all_letters = get_book_text(which_text).lower()[::1]
    were_counted = {}

    for letter in all_letters:
        if letter in were_counted:
            were_counted[letter] += 1
        else:
            were_counted[letter] = 1
    return were_counted

def sort_letters(which_text):
    were_counted = count_letters(which_text)
    were_sorted = []

    for letter in were_counted:
        if letter.isalpha():
            dict_entry = {"char" : letter, "num" : were_counted[letter]}
            were_sorted.append(dict_entry)
    def sort_on(dict):
        return dict["num"]

    were_sorted.sort(key=sort_on, reverse=True)
    
    return were_sorted
