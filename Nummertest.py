def test_nummer(nummer):
    return nummer > 256 and nummer % 34 == 4

print(test_nummer(12))
print(test_nummer(922))
print(test_nummer(914))
print(test_nummer(854))