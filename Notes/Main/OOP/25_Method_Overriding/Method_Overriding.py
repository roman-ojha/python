class Base:
    def sum(self, a, b):
        return a + b


class Child(Base):
    # Overriding the existing method of 'Base' class to 'Child' class
    def sum(self, a, b, c):
        # Or we can call the 'Base' class 'sum' method using 'super()' and pass the required argument
        sum = super().sum(a, b)
        return sum + c


m = Child()
sum = m.sum(30, 33, 12)
print(sum)
