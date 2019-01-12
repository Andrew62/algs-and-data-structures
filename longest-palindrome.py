

def longest_palindrome(mystr):
    # first step is to count up all the different characters
    # and how many times they appear
    # keeping track of the longest odd character because
    # you can only have 1 odd token for a palindrome otherwise
    # the sequence will not be balanced
    max_odd = 0
    odd_char = ''
    character_counts = {}
    for c in mystr:
        if c not in character_counts.keys():
            character_counts[c] = 1
        else:
            character_counts[c] += 1
        if character_counts[c] % 2 == 1 and character_counts[c] > max_odd:
            max_odd = character_counts[c]
            odd_char = c

    # now that we know the counts and the most frequently occuring odd character
    # we can go through and add up the lengths and make other odd character occurances
    # even
    palindrome_len = 0
    for k, v in character_counts.items():
        if k == odd_char:
            palindrome_len += v
        elif v % 2 == 1:
            palindrome_len += v - (v % 2)
        else:
            palindrome_len += v

    return palindrome_len


if __name__ == "__main__":
    a = longest_palindrome('ababbc')
    ans = 5
    assert a == ans, f"expected {ans} got {a}"

    a = longest_palindrome('cbbccd')
    ans == 5
    assert a == ans, f"expected {ans} got {a}"
