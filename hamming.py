

def hamming_distance(x, y):
    """
    Given two integers compute the hamming distance
    """
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]

    if len(bin_x) > len(bin_y):
        bin_x, bin_y = bin_y, bin_x
    while len(bin_x) < len(bin_y):
        bin_x = "0" + bin_x
    hamm = 0
    for idx, bit in enumerate(bin_x):
        if bit != bin_y[idx]:
            hamm += 1
    return hamm


if __name__ == "__main__":
    print(hamming_distance(12, 16))