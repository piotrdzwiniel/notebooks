# Define the nucleotides
nucleotides = ["A", "T", "C", "G"]


# Check if the sequence is valid
def check_sequence(sequence):
    for i in sequence.upper():
        if i not in nucleotides:
            return False
    return True


# Naive pattern search
def naive_pattern_search(sequence, pattern):
    """
    This is a simple approach where you search for a specific pattern (e.g. a subseqance)
    within a DNA sequence.
    :param sequence:
    :param pattern:
    :return:
    """
    positions = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions
