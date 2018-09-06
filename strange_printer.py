

def strangPrinter(instr: str):
    """
    strange printer does some weird shit

    https://leetcode.com/problems/strange-printer/description/
    """

    character_map = {}
    for idx, c in enumerate(instr):
        if c not in character_map.keys():
            character_map[c] = dict(start=idx, end=idx)
        else:
            character_map[c]['end'] = idx
    return len(character_map)
    # this is the actual printer. The question is looking for the number of lines
    # for characater, info in character_map.items():
    #     print(characater * (info['end'] - info['start'] + 1))


if __name__ == "__main__":
    print(strangPrinter("aacabbbc"))