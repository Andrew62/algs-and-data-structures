

def longest_palindrome(mystr):
    character_counts = {}
    for c in mystr:
        if c not in character_counts.keys():
            character_counts[c] = 1
        else:
            character_counts[c] += 1
    palindome_len = 0
    has_odd = False
    for k, v in character_counts.items():
        if v % 2 == 0: # even
            palindome_len += v
        # can only have one odd number of charaters 
        if not has_odd and v % 2 == 1:
            palindome_len += v
            has_odd = True

    return palindome_len
