# DC 1. Skip Character
# Requirements
# 1.0  Always skip a certain character
# 2.0 skip a certain character n number of times only (accept a tuple (character, count))
# 3.0 Avoid generating a StopIterator exception (add support for a default return value if we have reached the end of the iterable
# 4.0 Provide an alternate implementation using generators
# 3.0 Make this work on an input stream

class SkipChar:
    def __init__(self, source: str, skipchar: str = ''):
        self.current_idx = -1
        self.source = source
        self.skipchar = skipchar

    def skip_char(self, skipchar):
        self.skipchar = skipchar

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.current_idx += 1   # Advance to the next
        if self.current_idx < len(self.source):
            return self.source[self.current_idx] if self.source[self.current_idx] != self.skipchar else self.__next__()
        raise StopIteration

def skipchar(source, skipchar=''):
    """
        This generator will not raise the StopIterator exception.
        It will just return.
        Good alternative to avoid the StopIterator exception
    """
    current = 0
    while current < len(source):
        if source[current] != skipchar:
            yield source[current]
        current += 1

for c in skipchar("Hello", 'l'):
    print(c)

sc = SkipChar("Hello", 'l')
sc_iter = iter(sc)
for i in range(10):
    print(next(sc_iter))

print('Iterator has been exhausted. Exception raised. Program terminated')
sc.skip_char('H')
sc_iter = iter(sc)
for i in range(10):
    print(next(sc_iter))

