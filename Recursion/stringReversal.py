def stringReversal(input: str) -> str:
    if input == '': return ''
    return stringReversal(input[1:]) + input[0]

print(stringReversal("My Name is Basil!"))