

def search_for_word()


def word_search(board, words):
    rows = len(board)
    cols = len(board[0])
    found_words = []

    for row in range(rows):
        for col in range(cols):
            character = board[row][col]
            words_to_check = []
            for word in words:
                if word.startswith(character):
                    words_to_check.append(word)
            if len(words_to_check) > 0:
