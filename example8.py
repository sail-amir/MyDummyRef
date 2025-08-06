from Utils2 import Utils
class FirstClass:
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = Utils.duplicate(data)
        return f"FirstClass processed: {duplicated}"