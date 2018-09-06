

def binary(element, arr, idx=0):
    """
    Recursive binary search algorithm

    Parameters
    ----------
    element : float
        number to find in a list
    arr : 1-D [float]
        array to search
    idx : int
        used to recursively pass current index

    Returns
    -------
    int ; index of the element if it's in the list -1 otherwise
    """
    n_elements = len(arr)
    if n_elements == 1:
        if arr[0] == element:
            return idx
        else:
            return -1
    mid = n_elements // 2 
    if arr[mid] > element:
        return binary(element, arr[:mid], idx)
    else:
        return binary(element, arr[mid:], mid + idx)
 
