import time
import random
from colorama import Fore, Back, Style, init

class Bus:
    def __init__(self, number):
        self.number = number
        self.ordered = False

class BusStop:
    def __init__(self, name):
        self.name = name
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def order_bus(self, bus):
        bus.ordered = True
        print(f"Zamówiono autobus {bus.number} na przystanek {self.name}.")

    def list_buses(self):
        print(f"Lista autobusów dla {self.name}:")
        print(" ")
        current_time = time.localtime()
        for bus in self.buses:
            status = (Fore.GREEN+ "Zamówiony" +Style.RESET_ALL) if bus.ordered else (Fore.RED+ "Nie zamówiony" +Style.RESET_ALL)
            hour = current_time.tm_hour
            minute = current_time.tm_min + random.randint(1, 30)
            if minute >= 60:
                hour += 1
                minute -= 60
            godzina = f"{hour:02}:{minute:02}"
            print(f"| Linia: {bus.number} | Godzina: {godzina} | Status: {status}")

def main():
    stop1 = BusStop("Przystanek A")
    stop2 = BusStop("Przystanek B")

    bus1 = Bus(56)
    bus2 = Bus(34)
    bus3 = Bus(79)
    bus4 = Bus(98)

    stop1.add_bus(bus1)
    stop1.add_bus(bus2)
    stop2.add_bus(bus3)
    stop2.add_bus(bus4)

    while True:
        print("\nWybierz akcję 1/2/3:")
        print(" ")
        print("[1] <- Przystanek A")
        print("[2] <- Przystanek B")
        print("[3] <- Wyjście")
        print(" ")
        choice = input("Wybierz opcję: ")
        print(" ")

        if choice == '1':
            stop1.list_buses()
            print(" ")
            bus_number = input("Wybierz numer autobusu do zamówienia: ")
            print(" ")
            for bus in stop1.buses:
                if str(bus.number) == bus_number:
                    stop1.order_bus(bus)
                    break
            else:
                print(Back.RED+"Nieprawidłowy numer autobusu."+Style.RESET_ALL)

        elif choice == '2':
            stop2.list_buses()
            print(" ")
            bus_number = input("Wybierz numer autobusu do zamówienia: ")
            for bus in stop2.buses:
                if str(bus.number) == bus_number:
                    stop2.order_bus(bus)
                    break
            else:
                print(" ")
                print(Back.RED+"Nieprawidłowy numer autobusu."+Style.RESET_ALL)

        elif choice == '3':
            break
        else:
            print(" ")
            print(Back.RED+"Nieprawidłowa opcja."+Style.RESET_ALL)

if __name__ == "__main__":
    main()
