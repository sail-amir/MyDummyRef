from Utilities import Utils

class FirstClass:  
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = Utils.duplicate(data)
        return f"FirstClass processed: {duplicated}"
    
    def print_example(self):
        print('hi')    
        print('bye')

class SecondClass(FirstClass):
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = Utils.duplicate(item)
        self.print_example()
        return f"SecondClass displayed: {duplicated}"

