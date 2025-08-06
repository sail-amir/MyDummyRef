improt Utils2
class FirstClass:
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = Utils2.duplicate(data)
        return f"FirstClass processed: {duplicated}"