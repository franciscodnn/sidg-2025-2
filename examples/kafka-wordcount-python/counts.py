def count(words):
    """Count unique words in a list.

    Parameters
    ----------
    words : list
        A list of words (strings).

    Returns
    -------
    dict
        A dictionary where the keys are unique words and the values are the counts of those words.
    """
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


print(count(["apple", "banana", "apple", "orange", "banana", "apple"]))