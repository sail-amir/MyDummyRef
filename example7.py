from Utils import duplicate

class SecondClass:
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = duplicate(item)
        return f"SecondClass displayed: {duplicated}"

    def print_example(self):
        print('hi')