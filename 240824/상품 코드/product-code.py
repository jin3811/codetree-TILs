class Product:
    def __init__(self, name, code):
        self.code = code
        self.name = name
    
    def __repr__(self) -> str:
        return f"product {self.code} is {self.name}"

print(Product("codetree", "50"), Product(*input().split()), sep='\n')