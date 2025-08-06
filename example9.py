import Utils2
class SecondClass:
    def display(self, item):
        """Uses FirstClass.duplicate() in a different way."""
        duplicated = Utils2.duplicate(item)
        return f"SecondClass displayed: {duplicated}"

    def print_example(self):
        print('hi')