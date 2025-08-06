class FirstClass:
    @staticmethod
    def duplicate(x):
        """Static method to duplicate input."""
        return [x, x]    
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = Duplicator.duplicate(data)
        return f"FirstClass processed: {duplicated}"
    

class SecondClass:
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = FirstClass.duplicate(item)
        return f"SecondClass displayed: {duplicated}"

    def print_example(self):
        print('hi')