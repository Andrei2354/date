class Areas:
    def __init__(self, valor1, valor2) -> None:
        self.valor1 = valor1
        self.valor2 = valor2

    def areaRectangulo(self):
        return self.valor1 * self.valor2

    def areaTriangulo(self):
        return (self.valor1 * self.valor2) / 2
    

    