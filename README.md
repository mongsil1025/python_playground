# This is Python Playground

## Type

Python has the following data types built-in by default.
- Text Type: `str`
- Numeric Types: `int`, `float`, `complex`
- Sequence Types: `list`, `tuple`, `range`
- Mapping Type: `dict`
- Set Types: `set`, `frozenset`
- Boolean Type: `bool`
- Binary Types: `bytes`, `bytearray`, `memoryview`

String format code
|Code|Description|
|---|---|
|%s|문자열|
|%c|문자1개|
|%d|정수|
|%f|부동소수|
|%o|8진수|
|%x|16진수|
|%%|Literal %|

## Function

`*args` act as a dynamic multi parameters
`**kwargs` says that the parameter is dictionary (key-value)
lambda param1, param2, ... : expressions
```
add = lambda a, b : a + v
result = add(3, 4) #7
```