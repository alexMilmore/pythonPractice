# descriptors only work with class variables, so must be defined outside
class dbEntry:
    """
    Test database for practice

    data -- dictionary to set the build in variables, can contain
            -- firstName
            -- lastName
            -- age
    """

    class Field:
        """
        Manages private instance variables.
        Assures that data is stored in a private variable of a set data type

        name -- the name of the private instance variable this class manages
        dtype -- function used to set the datatype

        NOTE: This only works in Python3
        """

        def __init__(self, name, dtype):
            self.name = name;
            self.dtype = dtype;

        def __get__(self, obj, owner):
            return getattr(obj, self.name) if hasattr(obj, self.name) else None;

        def __set__(self, obj, value):
            setattr(obj, self.name, self.dtype(value));


    firstName = Field('_firstName', str);
    lastName = Field('_lastName', str);
    age = Field('_age', int);

    def __init__(self, data):
        # set instance values
        for key, value in data.items():
            setattr(self, key, value);

    # properties that are just composites of data stores here
    @property
    def fullName(self):
        """
        Composite property of first and last name
        """
        return self.firstName + ' ' + self.lastName;

    @property
    def details(self):
        """
        Composite property, displays full name and age in a dict
        """
        return {'name': self.fullName, 'age':self.age}


########################### Testing ######################################
a = dbEntry({'firstName':'Dan', 'lastName':'Johnson', 'age':25});
b = dbEntry({'firstName':'James', 'lastName':'Billings', 'age':23});

a.firstName = 'Billy'

print(vars(a));
print('');
print(vars(b));
print('');
print(vars(dbEntry));

print(a.fullName);
print(b.details);
