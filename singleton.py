class Single:
    """
    Singleton design pattern
    """

    __instance = None;

    class Singleton:
        """
        Very simple class that is now global
        """

        def __init__(self, value):
            self.value = value;

    def __init__(self, value):
        if (Single.__instance == None):
            Single.__instance = Single.Singleton(value);
        else:
            Single.Singleton.value = value;

    def __getattr__(self, name):
        """ gets the specified value from the nested singleton class """

        inst = self.__instance;
        return getattr(inst, name) if hasattr(inst, name) else None;

    def __setattr__(self, name, value):
        """ sets the specified value in singleton class """

        setattr(self.__instance, name, value)

################################################################################
a = Single(5);
b = Single(8);

b.value = 12;

print(a.value);
