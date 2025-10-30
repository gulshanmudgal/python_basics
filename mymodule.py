print('Imported My Module')

test = 'This is a test string'

def find_index(to_search, target):
    """Find index of target in to_search or return -1 if not found."""
    for i in range(len(to_search)):
        if to_search[i] == target:
            return i
        
    return -1
