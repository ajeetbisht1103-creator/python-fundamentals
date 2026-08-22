# ----------------------------------------------------
# Description:
# This program demonstrates multiple inheritance
# and Python's Method Resolution Order (MRO).
# ----------------------------------------------------

class Printer:
    def process(self):
        print("Processing document for printing.")


class Scanner:
    def process(self):
        print("Processing document for scanning.")


class AllInOnePrinter(Printer, Scanner):
    def process(self):
        print("All-in-one device selected.")
        Printer.process(self)
        Scanner.process(self)


device = AllInOnePrinter()

device.process()

print("\nMethod Resolution Order:")
for cls in AllInOnePrinter.mro():
    print(cls.__name__)