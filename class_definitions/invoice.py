class Invoice:
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price=dict()):
        self.__invoice_id = invoice_id
        self.__customer_id = customer_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__phone_number = phone_number
        self.__address = address
        self.__items_with_price = items_with_price.copy()

    def __str__(self):
        return "Invoice ID: " + str(self.__invoice_id) + "\n" + \
               "Customer ID: " + str(self.__customer_id) + "\n" + \
               "Last Name: " + self.__last_name + "\n" + \
               "First Name: " + self.__first_name + "\n" + \
               "Phone Number: " + self.__phone_number + "\n" + \
               "Address: " + self.__address + "\n" + \
               "Items: " + str(self.__items_with_price) + "\n"

    def __repr__(self):
        return str(self)

    def add_item(self, data):
        for key in data:
            self.__items_with_price[key] = data[key]

    def create_invoice(self):
        cost = 0
        for item in self.__items_with_price:
            cost += self.__items_with_price[item]
            print("{}.....${:<.2f}".format(item, self.__items_with_price[item]))
        tax = cost * 0.06
        cost += tax
        print("Tax.........${:<.2f}".format(tax))
        print("Total.......${:<.2f}".format(cost))


if __name__ == '__main__':
    invoice = Invoice(1, 123, "1313 Disneyland Dr, Anaheim, CA 92802", "Mouse", "Minnie", "555-867-5309")
    invoice.add_item({"iPad": 799.99})
    invoice.add_item({"Surface": 999.99})
    invoice.create_invoice()
