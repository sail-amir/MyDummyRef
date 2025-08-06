class Duplicator:
    @staticmethod
    def duplicate(x):
        """Static method to duplicate input."""
        return [x, x]

class FirstClass:
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = Duplicator.duplicate(data)
        return f"FirstClass processed: {duplicated}"

class SecondClass:
    def display(self, item):
        """Uses Duplicator.duplicate() in a different way."""
        duplicated = Duplicator.duplicate(item)
        return f"SecondClass displayed: {duplicated}"