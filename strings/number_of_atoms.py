from collections import defaultdict
import string

"""
Explanation
(Mg(OH)2)

Use a stack (consisting of dictionary elements, ( - end of merge operation, )
 - start of merge operations)
(
{'Mg' : 1}
(
{'O' : 1}
{'H' : 1}
) - Indicates it is time to merge all the values upto (
{'O' : 1, 'H' : 1}
Multiply the dictionary at the top of the stack with the number 2 
{'O' : 2, 'H' : 2}
) Merge all the dictionaries until we reach a (

{'Mg' : 1, 'O' : 2, 'H' : 2}
Finally display the string (with the keys sorted)
H2MgO2


Time Complexity: O(N), N is the size of grid matrix
Space Complexity: O(1)
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def multiply(formula_dict, k):

            for key in formula_dict:
                formula_dict[key] = formula_dict[key] * k

            return formula_dict

        def merge(formula_dict_1, formula_dict_2):

            for key in formula_dict_2:
                formula_dict_1[key] = formula_dict_1[key] + formula_dict_2[key]

            return formula_dict_1

        formula = "(" + formula + ")"
        i = 0
        stack = []
        # while loop preferable, as we can control how much to advance as we
        # encounter different characters
        # formula = "H2O", "Mg(OH)2", "K4(ON(SO3)2)2"

        while i < len(formula):
            # "(": put into stack
            if formula[i] == "(":
                stack.append(formula[i])
                i += 1

            # characters: put into stack as dict
            elif formula[i] in string.ascii_uppercase:
                atom = formula[i]
                i += 1
                while formula[i] in string.ascii_lowercase:
                    atom += formula[i]
                    i += 1
                formula_to_push = defaultdict(int)
                formula_to_push[atom] = 1
                stack.append(formula_to_push)

            # number: multiply last formula in the stack
            elif formula[i] in string.digits:
                count = ""
                while formula[i] in string.digits:
                    count += formula[i]
                    i += 1
                # Apply this multiple to the last formula on the stack
                formula_to_multiply = stack.pop()
                stack.append(multiply(formula_to_multiply, int(count)))

            # ")": pop and merge all the formula from stack until "("
            else:
                formula_to_merge = defaultdict(int)
                # print(stack)
                while stack[-1] != "(":
                    formula_to_merge = merge(formula_to_merge, stack.pop())

                stack.pop()
                stack.append(formula_to_merge)
                i += 1

        # construct formula
        formula_dict = stack.pop()
        formula = ""
        for atom in sorted(formula_dict.keys()):
            formula += atom
            if formula_dict[atom] > 1:
                formula += str(formula_dict[atom])

        return formula


