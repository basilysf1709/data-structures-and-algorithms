def decimalToBinary(decimal: int) -> str:
    if decimal == 0: return 0
    if decimal == 1: return 1
    return str(decimalToBinary(decimal // 2)) + str(decimal % 2)


print(decimalToBinary(233))