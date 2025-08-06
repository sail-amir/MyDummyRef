class FirstClass:
    def duplicate(self, x):
        """Creates a duplicate (copy) of the input."""
        return [x, x]  # Same implementation in both classes
    
    def process(self, data):
        """Uses duplicate() to process data."""
        duplicated = self.duplicate(data)
        return f"FirstClass processed: {duplicated}"


class SecondClass:
    def duplicate(self, x):
        """Same implementation as in FirstClass."""
        return [x, x]  # Exact clone of FirstClass.duplicate()
    
    def display(self, item):
        """Uses duplicate() in a different way."""
        duplicated = self.duplicate(item)
        return f"SecondClass displayed: {duplicated}"