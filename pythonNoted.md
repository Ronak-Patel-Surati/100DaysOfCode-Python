# Python object Oriented Programming

## basics

        Strings
        Integers
        variables
        Float
        {} placeholders
        f for format Strings
        Boolean : True Or False , 1 or 0 
        
## typecasting

        str()
        int()
        float()
        bool()
        type() for checking type 
        using bool we can check for empyty input

## Input

        default is stirng
        functions can be passed as arguments for other functions

## Math and Arithmatics

        /*-+ % ** % //
        round()
        abs()
        pow()
        max()
        min()
        using math module 
                math.pi()
                math.e()
                math.sqrt() 
                math.ceil()
                math.floor()

## logical operators

        or and not 
        not is used for inverting the conditons

## Conditonal Expressions

        do soemthing if condition else do other thing

## String methods

        len 
        find
        rfind
        capitalize
        upper 
        lower
        isdigit
        isalpha
        count 
        replace 
        use print(help()) for other methods

## indexing

        [start:end:step]
        for reversing the list use -1 as stepper

## formtat specififers

        .2f for floating point variables upto two decimals points
        :10 for 10 spacing for printed output
        :<10 left justify
        :>10 right justify
        :^  CENTERED TEXT       
        :, IS thaousand seperator
        reversed()
        :+ for signs in the output pritns

## While loops

        while condtion meets:
                do soemthing
        else: 
                anit out comes

## for loops

        for variable in iterable:
                do something in the range of iterable
                exceutes finxed no of times
        else: 
                catch the erros i guess
        range() for producing a iterable
        list tuples dictinaries are iterabel 

## import times

## Collections

        List []
        Set {}
        dictinaries{key:value}
        tuples()

        for listing the attributes that can be used for a fucntions 
        use print(dir('something here'))
        use print(help(something here again))
        use print(len(something here returns))
        use 'in' for checking checking wheather it is in the list or not

## method for Collections

        append
        remove
        insert
        sort
        reversed
        clear
        index 
        count
        add 
        remove
        pop 
        c

## 2D lists

        <!-- will add here -->

## dictinaries

        {key : value} pair
        methods of dics 
        update 
        pop
        popitem
        clear
        keys
        values

## random

        import random
        random.randint
        random.choice
        random.shuffle

## function's args kargs

        Functions has has Args , positonal, default, keyword, arbitary
        *args means multiple arguments
        **kwargs means multiple key word arguments
        * is unpacking operator
        typles as args 
        dicts as kwargs
        method 
        value 
        get

## Iterab A collections of objects

        .values
        items

## membership operator

        in 
        not in 
        for String dics tuple lists sets 

## List comprehension

        [Expressions for value in iterable if condition]

## Match case

        switch case of Python
        match var:
                case  var :
                        do something

        | is or operator

## module

        import
        from aa import yy

## Variable scope

        Local 
        Enclosed 
        Global
        Built - in

## class variables = Shared among all instances of a class Defined outside the constructor Allow you to share data among all objects created from that class

    use __init__ for inilisation of class.
    use def for defining functions.

## Inheritance = Allows a class to inherit attributes and methods from another class Helps with code reusability and extensibility class Child(Parent)

        class Animal:
        def
        self.
        self.
        (self, name):
        name = name
        is alive
        = True
        def eat(self):
        print(f"{self.name} is eating")
        def sleep(self):
        print(f"{self.name} is sleeping")
        class Dog(Anima1):
        pass
        class Cat(Anima1):
        pass
        class Mouse(Anima1):
        passl

## multiple and multi level inharitance

        class fish(Prey,l Predator)
        multiple inheritance =
        inherit from more than one parent class
        multilevel inheritance = inherit
        c(A, B)
        c(B)
        from a
        papent which inherits from another parent

## Super functions

        used for extending class functionality of the inherited methods

## Polymorphism

        = Greek word that means to "have many forms or faces"
        Poly = Many
        Morphe = Form    
        TWO WAYS TO ACHIEVE POLYMORPHISM
        1.  Inheritance = An object could be treated of the same type as a parent classl
        2. "Duck Object must have necessary attributes/methods
        abstract methods?
        super().__init__(radius)

## Duck typing

        Another way to achieve polymorphism besides Inheritance
        Object must have the minimum necessary attributes/methods
        "If it looks lil<e a duck and quacks like a duck, it must be a duck.

## methods

    Static methods = A method that belong to a class rather than any object from that class (instance)
    Usually used for general utility functions
    Instance methods = Best for operations on instances of the class (objects)
    Static methods = Best for utility functions that do not need access to class data

## Class methods

    Allow operations related to the class itself
    Take (c Is) as the first parameter, which represents the class itself.
    
    
    Instance methods = Best for operations on instances of the class (objects)
    Static methods = Best for utility functions that do not need access to class data
    Class methods = Best for class-level data or require access to the class itself

## magic methods

    Dunder methods (double underscore) __ init __ , __ str __ , __ eq __  , __ lt __ , __ gt __ , __ getitem __ , 
    They are automatically called by many of Python's built-in operations.
    They allow developers to define or customize the behavior of objects

## @property

    Decorator used to define a method as a property (it can be accessed like an attribute)
    Benefit: Add additional logicl when read, write, or delete attributes
    Gives you getter, setter, and deleter method
    