class Family:
    lastname = "김"

a = Family()
b = Family()

print(f"{a.lastname} | {id(a.lastname)}")
print(f"{b.lastname} | {id(b.lastname)}")

Family.lastname = "박" # 클래스 변수를 수정할 경우 같은 id 주소를 가지고 있기 때문에 모든 인스턴스가 변경된다.

print(f"{a.lastname} | {id(a.lastname)}")
print(f"{b.lastname} | {id(b.lastname)}")

a.lastname = "정" # 하나의 인스턴스만 변경할 경우, 해당 객체의 id 주소가 변경되고 해당 객체만 수정된다.

print(f"{a.lastname} | {id(a.lastname)}")
print(f"{b.lastname} | {id(b.lastname)}")

