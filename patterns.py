rows = 5

print("🔻 Lower Triangular Pattern:")
for i in range(1, rows + 1):
    print("*" * i)

print("\n🔺 Upper Triangular Pattern:")
for i in range(rows, 0, -1):
    print("*" * i)

print("\n⛰️  Pyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
