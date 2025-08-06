class FirstClass:
    @staticmethod
    def duplicate(x):
        """Static method to duplicate input."""
        return [x, x]
    
    def process(self, data):
        """Uses FirstClass.duplicate() to process data."""
        duplicated = self.duplicate(data)
        return f"FirstClass processed: {duplicated}"
    
class SecondClass:
    def duplicate(self, x):
        """Static method to duplicate input."""
        return [x, x]  
    
    def display(self, item):
        """Instance method to duplicate input."""
        duplicated = self.duplicate(item)
        return f"SecondClass displayed: {duplicated}"
    
    def print_example(self):
        print('hi')
