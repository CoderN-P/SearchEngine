def concordance(document):
    if not isinstance(document, str):
        raise TypeError("Document must be string")

    words = {}

    for word in document.split():
        lower = word.lower()
        if lower in words:
            words[lower] += 1
        else:
            words[lower] = 1

    return words
