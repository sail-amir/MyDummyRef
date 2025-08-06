class FirstClass:
    def duplicate(x):
        """Static method to duplicate input."""
        return [x, x]
    
    def process(self, data):
        """Uses Duplicator.duplicate() to process data."""
        duplicated = self.duplicate(data)
        return f"FirstClass processed: {duplicated}"