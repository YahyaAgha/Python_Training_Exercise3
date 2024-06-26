# Python_Training_Exercise3

--object-oriented programming-- Classes and advanced OOP Tasks

By examining and executing the Python classes and methods outlined above, one can learn several important concepts in object-oriented programming (OOP) in Python:
1. Class Definition and Inheritance:
The Shape, Rectangle, Square, and Circle classes demonstrate how to define custom classes in Python.
Inheritance is shown by how Rectangle inherits from Shape, Square inherits from Rectangle, and Circle also inherits from Shape. This illustrates how a subclass can inherit properties and methods from a superclass and how it can extend or override them.
2. Encapsulation:
Each class encapsulates data and behavior that are relevant to the objects being modeled. For example, the Rectangle class encapsulates the properties width, height, and center, as well as the behavior to calculate its area.
3. Method Overriding:
The Circle class overrides the perimeter and point_on_perimeter methods to provide an implementation that is specific to circles. This is a key concept in OOP where a subclass can provide a specific implementation of a method that is different from the superclass.
4. Polymorphism:
The example demonstrates polymorphism where the Shape class provides a general interface for methods like draw and point_on_perimeter, which are then used by subclasses to perform actions that are specific to their shape.
5. Abstraction:
The Shape class acts as an abstract base class that defines a contract for its subclasses. It doesn't make sense to instantiate a Shape directly, but its subclasses like Rectangle and Circle provide concrete implementations for the abstract methods.
6. Constructor and Initialization:
The __init__ method in each class is the constructor that initializes the object's state. It is called when an object is created from the class.
7. Composition:
The Shape class uses a list of Line objects to represent its sides, which is an example of composition. This is a "has-a" relationship where a Shape is composed of multiple lines.
8. Use of External Libraries:
The use of matplotlib to draw the shapes demonstrates how classes can leverage external libraries to extend their capabilities.
9. String Representation:
The __str__ method provides a human-readable string representation of the object, which is useful for debugging and logging.
By working with these classes, one can understand how to structure code in an object-oriented manner, allowing for the creation of reusable and maintainable code. It also highlights the power of using classes to model real-world concepts and relationships within a program.

## 

The super() function in Python is a built-in function that returns a proxy object that allows you to access methods of a base class from a derived class. It is used when you want to call a method from the parent class within a method of a child class, especially when you are overriding that method.
Here are the key points related to the super() function as used in the code examples above:

Using super() helps avoid directly naming the parent class, which can be beneficial if you decide to change the base class later on. It makes the code more maintainable and adaptable to changes.

super() follows the method resolution order, which is the order in which Python looks for a method in a hierarchy of classes. It ensures the correct method gets called within complex class hierarchies.

In the Square class, super().__init__(side, side, center) is called to utilize the constructor of the Rectangle class, which Square inherits from. This initializes a Square object using the Rectangle constructor, effectively chaining constructors to ensure proper initialization.

In the Circle class, super().__init__(lines) is used to call the constructor of the Shape base class, which initializes the lines attribute that represents the sides of the polygonal approximation of the circle. This is an example of using super() to extend the functionality of an overridden method, in this case, the constructor.

