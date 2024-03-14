# class Cookie:
#    pass

# a = Cookie()
# b = Cookie()

# print(a)
# print(id(a))
# print(type(a))

# print(b)
# print(id(b))
# print(type(b))

class FourCal:
    calname = "계산기"
    def __init__(self,first=1,second=1):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)
        return result
    
    def sub(self):
        result = self.first - self.second
        print(result)
        return result

    def div(self):
        result = self.first / self.second
        print(result)
        return result

# a = FourCal()
# a.setdata(2,3)
# print(a.add())
# print(a.sub())

# b = FourCal()
# b.setdata(8,2)
# print(b.add())
# print(b.sub())

# a.first = 10
# a.second = 4
# print(a.add())
    
a = FourCal()
a.add()
c = FourCal()
print(FourCal.calname, c.calname)
c.calname = "다기능계산기"

print(FourCal.calname, a.calname, c.calname)


class MoreFourCal(FourCal): #부모 클래스- 상속 받음- 
    def div(self):
        if self.second == 0:
            print("2번째 인자값은 0을 입력하면 안됨") # 메서드 오버라이딩 방지
            return 0
        else:
            result = self.first / self.second
            print(result)
            return result

b = MoreFourCal(4,0)
b.add()
b.div() 