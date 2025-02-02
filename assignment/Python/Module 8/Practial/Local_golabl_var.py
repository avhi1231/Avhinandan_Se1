# Global variable
global_message = "I am a global variable"

class Demo:
    def __init__(self):
        # Instance variable
        self.local_message = "I am a local variable in the class"

    def show_messages(self):
        # Local variable inside the method
        method_message = "I am a local variable in the method"

        print(global_message)  # Accessing the global variable
        print(self.local_message)  # Accessing the class's local variable
        print(method_message)  # Accessing the method's local variable
demo = Demo()
demo.show_messages()
print(global_message)
