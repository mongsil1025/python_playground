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

## Module

- `import` 할 때 마지막 항목은 반드시 모듈 또는 패키지여야 한다. The last thing to write when `impoirt` must be module or package
- `__init__.py` 의 용도 : `__init__.py` 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만약 이 파일이 없다면 패키지로 인식되지 않는다.
```
from game.sound import * # (1) Error
from game.sound.echo import * # (2) OK
```
(1) 과 같은 경우에는 해당 디렉터리의 `__init__.py` 에 `__all__`변수를 설정하고 import 할 수 있는 모듈을 정의해주어야 한다.
(2) 가 성공한 이유는 import의 마지막 항목이 모듈인 경우이다.

## Inner Function

- `enumerate` : 순서가 있는 자료형 (리스트, 튜플, 문자열)을 입력받아 인덱스와 값을 포함하는 객체를 돌려준다.