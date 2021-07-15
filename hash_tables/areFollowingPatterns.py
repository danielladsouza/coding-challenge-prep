"""
    Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

    Example

    For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
    areFollowingPatterns(strings, patterns) = true;
    For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
    areFollowingPatterns(strings, patterns) = false.
    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.string strings

    An array of strings, each containing only lowercase English letters.

    Guaranteed constraints:
    1 ≤ strings.length ≤ 105,
    1 ≤ strings[i].length ≤ 10.

    [input] array.string patterns

    An array of pattern strings, each containing only lowercase English letters.

    Guaranteed constraints:
    patterns.length = strings.length,
    1 ≤ patterns[i].length ≤ 10.

    [output] boolean

    Return true if strings follows patterns and false otherwise.

"""
from collections import defaultdict


def areFollowingPatterns(strings, patterns):
    """
        ["cat", "cat", "cat"]

        "cat" [0,1,2]
        ["a", "a", "a"]
        "a" [0,1,2]

        Two dictioraries
        keu - string
        value - list
        O(N)

        Compare the two lists for equality.

        Space Complexity

        O(1) * O(N) - O(N)
        Strings are all unique

        Can we assume both strings and patterns are of the same length

    """
    strings_map = defaultdict(list)

    patterns_map = defaultdict(list)
    """
    for i, s in enumerate(strings):
        strings_map[s].append(i)

    for j,p in enumerate(patterns):
        patterns_map[p].append(j)
    """

    for i, (s, p) in enumerate(zip(strings, patterns)):
        strings_map[s].append(i)
        patterns_map[p].append(i)

    for v1, v2 in zip(strings_map.values(), patterns_map.values()):
        if v1 != v2:
            return False

    return True