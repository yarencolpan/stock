class Stock:
    def __init__(self, name, sector, company, stock_price, lot_size):
        self.sector = sector
        self.company = company
        self.stock_price = stock_price
        self.lot_size = lot_size
        self.name = name

    def information(self):
        print("""
        Information about stock:
        
        Name: {}
        Sector: {}
        Company: {}
        Stock_price: {}
        lot_size: {} 
        
        """.format(self.name, self.sector, self.company, self.stock_price, self.lot_size))

    def selling_lot(self, amount):
        self.lot_size -= amount

    def buying_lot(self, amount):
        self.lot_size += amount


nvidia = Stock("nvidia", "technology", "nvidia", 123, 4)
nvidia.information()
