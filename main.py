import os
import pickle


class Kassa:
    TICKETS_FILE = "tickets.pickle"
    MONEY_FILE = "money.pickle"

    def __init__(self):
        self.tickets = None
        self.money = 0
        self._read_data()

    def _read_data(self):
        if os.path.exists(self.TICKETS_FILE):  # Trying to open a base if exists, appending() if not
            with open(self.TICKETS_FILE, "rb") as file:
                base = pickle.load(file)
            with open(self.MONEY_FILE, "rb") as file:
                money = pickle.load(file)
        else:
            print("База отсустсвует")
            base = self._create_base()
            money = float(input("Скока денег?"))

        self.tickets = base
        self.money = money

    @staticmethod
    def _create_base():
    # adding new elements in base
    # base format:
    #   {price1: [[start1, end1], [start2, end2]...],
    #    price2: [[start1, end1], [start2, end2]...], }
        base = {}
        while True:
            price = input("price ['' for finish]: ")
            if not price:
                break
            price = float(price)
            base[price] = []
            while True:
                input_line = input("start/end ['' for finish]: ")
                if not input_line:
                    break
                start, end = (int(i) for i in input_line.split())
                base[price].append([start, end])

        return base

    def sell(self):
        price, quantity = input("Через пробел цена и количество").split()
        price = float(price)
        quantity = int(quantity)
        bunches = self.tickets.get(price, [])
        while quantity:
            if not bunches:
                raise BaseException(f'fake tickets: ')
            bunch = bunches[0]
            bunch_size = bunch[1] - bunch[0] + 1
            if quantity < bunch_size:
                bunch[0] += quantity
                break
            else:
                del bunches[0]
                quantity -= bunch_size

        self.money += price * quantity

    def save(self):
        # save self.tickets into file
        with open(self.TICKETS_FILE, "wb") as file:  # saving in pickle file
            pickle.dump(self.tickets, file)
        with open(self.MONEY_FILE, "wb") as file:  # saving in pickle file
            pickle.dump(self.money, file)

    def debug(self):
        print(f"money: {self.money}\ntickets:\n{self.tickets}")


if __name__ == "__main__":
    k = Kassa()
    k.sell()
    k.debug()
    k.save()











