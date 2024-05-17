def main():
    book_path = 'books/frankenstein.txt'
    frankenstein_text = get_book_text(book_path)
    num_words = get_word_count(frankenstein_text)
    num_letters = count_letters(frankenstein_text)
    book_report = report_book(num_letters, num_words, book_path)
    # print(f"{num_words} words found in the document")
    # print(f"{num_letters} letters found in the document")
  
    

def get_word_count(text):
    words = text.split()
    return len(words)
    
def get_book_text(path):
    with open(path) as f:  
        return f.read()

def count_letters(text):
    letter_count = {}
    text_lst = text.split()
    
    for word in text_lst:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter.isalpha():
                if lower_letter in letter_count:
                    letter_count[lower_letter] += 1
                else: 
                    letter_count[lower_letter] = 1
    return letter_count


def report_book(letter_count, word_count, book_path):
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document')
    print('')
    
    # Sort the dictionary items by value in descending order
    sorted_lst = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

    # Print the sorted letter counts
    for letter, value in sorted_lst:
        print(f'The {letter} character was found {value} times')

    print('--- End Report ---')




    
main()