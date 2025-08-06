from Utils import duplicate

class FirstClass:
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = duplicate(data)
        return f"FirstClass processed: {duplicated}"