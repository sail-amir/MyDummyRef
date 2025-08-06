from Utils2 import Utils
class SecondClass:
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = Utils.duplicate(item)
        return f"SecondClass displayed: {duplicated}"

    def print_example(self):
        print('hi')