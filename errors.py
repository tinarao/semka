class Error:
    def __init__(self, name, details = None) -> None:
        self.name = name
        self.details = details
        
    def __repr__(self) -> str:
        return self.to_string()
        
    def to_string(self):
        return f'{self.name}: {self.details}'
    
class IllegalError(Error):
    def __init__(self, details) -> None:
        super().__init__("Illegal Character", details)