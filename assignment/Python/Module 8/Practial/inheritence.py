# Demonstrating various types of inheritance in a single program

# Base Class
class Grandparent:
    def show_grandparent(self):
        print("This is the Grandparent class.")

# Single Inheritance: Parent inherits from Grandparent
class Parent(Grandparent):
    def show_parent(self):
        print("This is the Parent class.")

# Multilevel Inheritance: Child inherits from Parent, which inherits from Grandparent
class Child(Parent):
    def show_child(self):
        print("This is the Child class.")

# Multiple Inheritance: Class inherits from two parent classes
class Father:
    def show_father(self):
        print("This is the Father class.")

class Mother:
    def show_mother(self):
        print("This is the Mother class.")

class Sibling(Father, Mother):
    def show_sibling(self):
        print("This is the Sibling class.")

# Hierarchical Inheritance: Two or more classes inherit from the same parent class
class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class.")

class Child2(Parent):
    def show_child2(self):
        print("This is Child2 class.")

# Hybrid Inheritance: A mix of multiple and hierarchical inheritance
class HybridChild(Child1, Mother):
    def show_hybrid(self):
        print("This is the HybridChild class.")

# Create objects and demonstrate functionality
print("** Single, Multilevel, and Hierarchical Inheritance **")
child = Child()
child.show_grandparent()  # Access Grandparent method
child.show_parent()       # Access Parent method
child.show_child()        # Access Child method

print("\n** Multiple Inheritance **")
sibling = Sibling()
sibling.show_father()     # Access Father method
sibling.show_mother()     # Access Mother method
sibling.show_sibling()    # Access Sibling method

print("\n** Hierarchical Inheritance **")
child1 = Child1()
child1.show_parent()      # Access Parent method
child1.show_child1()      # Access Child1 method

child2 = Child2()
child2.show_parent()      # Access Parent method
child2.show_child2()      # Access Child2 method

print("\n** Hybrid Inheritance **")
hybrid = HybridChild()
hybrid.show_grandparent() # Access Grandparent method
hybrid.show_child1()      # Access Child1 method
hybrid.show_mother()      # Access Mother method
hybrid.show_hybrid()      # Access HybridChild method