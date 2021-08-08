# Skip Character
# Requirement
# 1.0  Always skip a certain character
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

sc = SkipChar("Hello", 'o')
sc_iter = iter(sc)
for i in range(10):
    print(next(sc_iter))

print('Iterator has been exhausted. Exception raised. Program terminated')
sc.skip_char('H')
sc_iter = iter(sc)
for i in range(10):
    print(next(sc_iter))

