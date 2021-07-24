from collections import defaultdict
import string

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
            H2O
            string.alphanumeric
            string.digits
            string.ascii_letters

        dictionary - key ascii letter, value count
        sort the keys
        return the entire string in the format key_ValueCount

        "H2O"
        """
        d = defaultdict(int)

        current_element = []
        current_count = []

        for c in formula:
            if c in string.ascii_uppercase:
                if current_element:
                    d[''.join(current_element)] = int(''.join(current_count))
                    current_element = [c]
                    current_count = ['1']
                else:
                    current_element.append(c)
            elif c in string.ascii_lowercase:
                current_element.append(c)
            elif c in string.digits:
                current_count.append(c)

        if current_element:
            d[''.join(current_element)] = int(''.join(current_count))

        result = []
        for element in sorted(d.keys()):
            if d[element] > 1:
                result.append(f'{element}{d[element]}')
            else:
                result.append(f'{element}')

        return ''.join(result)