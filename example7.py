class SecondClass:
    def duplicate(x):
        """Static method to duplicate input."""
        return [x, x]
    
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = self.duplicate(item)
        return f"SecondClass displayed: {duplicated}"

    def print_example(self):
        print('hi')