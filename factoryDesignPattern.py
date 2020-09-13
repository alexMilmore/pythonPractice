class Counter:
    start = 100;

    def tick(self):
        self.count

class FastCounter(Counter):
    """
    Counter that counts down quickly
    """

    def __init__(self):
        self.speed = 10;
        super().__init__;

class MidCounter(Counter):
    def __init__(self):
        self.speed = 5;
        super().__init__;


class SlowCounter(Counter):
    def __init__(self):
        self.speed = 1;
        super().__init__;


class CounterFactory(Counter):
    def getCounter(self, speed):
        if (speed == 'Fast'):
            return FastCounter();
        elif (speed == 'Mid'):
            return MidCounter();
        elif (speed == 'Slow'):
            return SlowCounter();

fact = CounterFactory();

count1 = fact.getCounter('Fast');
count2 = fact.getCounter('Slow');

print(count1.start)

print(vars(count1));
print(vars(count2))
