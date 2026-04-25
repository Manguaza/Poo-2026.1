class Abastecimento:
    def__init__(self, data, km_rodado, num_litros, valor_pago):
    self.set_data(data)
    self.set_km_rodado(km_rodado)
    self.set_num_litros(num_litros)
    self.set_valor_pago(valor_pago)
    def set_data(self, data):
        self.data = data
    def set_km_rodado(self, km_rodado):
        if km_rodado > 0: