"""
Given an array of positive and negative integers where each interger indicates the number of 
steps to progress forward or backward
"""

def circle_array(arr: list):
    idx = 0
    visited = {idx}
    while len(arr) > 0:
        steps = arr.pop(0)
        idx += steps
        if idx in visited:
            return True
        visited.add(idx)
    return False

if __name__ == "__main__":
    print(circle_array([2, -1, 1, 2, 2]))