import pandas as pd
ser = pd.Series(['amrita','school','of','engineering'])
print("Before conversion of first character to upper case:")
print(ser)
result = ser.map(lambda x: x[0].upper()+x[1:-1]+x[-1].lower())
print("\nAfter conversion:")
print(result)
