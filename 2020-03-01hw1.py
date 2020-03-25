class InvalidKeyArgumentsException(Exception):
    def __str__(self):
        return "Invalid Key Arguments"

class Sum():
    def __init__(self):
        self.sum = 0


    def calculate(self, *args,**kwargs):
        print(repr(list))
        l = len(list) // 2
        xs = list[:l]
        ys = list[l:]
        for i in range(0, l):
            self.sum += (xs[i]**2 + ys[i]**2 + xs[i]*ys[i])
            # print(repr(self.sum))
        return self.sum

    def append_kwargs(self, args, kwargs):
        try:
            self.__validate_args__(args, kwargs)
            for key, value in kwargs.items():
                print(key, ' appended')
                args.append(value)
            return args
        except InvalidKeyArgumentsException as err:
            print(err)
            return []

    def validate_args(self, *args, **kwargs):
        try:
            if len(args) != len(kwargs):
                raise InvalidKeyArgumentsException
            else:
                return self.calculate(args,kwargs)
        except InvalidKeyArgumentsException as e:
            print(e)



# print(Sum().one(1,y1=1))
# print(Sum().two(1,2,y1=1,y2=2))
# print(Sum().three(1,2,3,y1=1,y2=2,y3=3))
# print(Sum().four(1,2,3,4,y1=1,y2=2,y3=3,y4=4))
print(Sum().validate_args(1,2,3,4,5,y1=1,y2=2,y3=3,y4=4,y5=5))
print(Sum().validate_args(1,2,3,4,5,y1=1,y2=2,y3=3,y4=4,y5=5,y6=6))
