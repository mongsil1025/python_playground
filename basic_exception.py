class Life:

    def write(self):
        print("Life is Good")


class Bird(Life):

    def write(self):
        print("Bird is Cuty")

    def fly(self):
        raise NotImplementedError


# 클래스 안에서 상속받은 클래스의 함수를 쓰려면 어떻게 해야하지?
class Eagle(Bird):

    def fly(self):
        print("very fast")
    pass

eagle = Eagle()
eagle.fly() # error if not implement fly method

