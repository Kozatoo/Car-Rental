from Models.rental import *
from Models.invoice import *
from Models.option import OptionType
    
class RentalWithOptions:
    def __init__(self, rental: Rental) :
        self._rental= rental
        self.options = []
        
    def addOption(self, option: OptionType) -> None:
        if(option in self.options):
            print("You already have this option!")
            return
        self.options.append(option.value)
        if option == OptionType.GPS:
            price_added= self._rental.rentalDuration() * 500
        elif option == OptionType.BabySeat:
            price_added= self._rental.rentalDuration() * 200
        elif option == OptionType.AdditionalInsurance:
            price_added = self._rental.rentalDuration() * 1000
            self._rental.commission.drivy_fee += price_added 
            self._rental.commission.commissioned_part += price_added
        else:
            print("Wrong option inserted!") 
            return
        self._rental.price += price_added
        self._rental.invoices = Invoice.getRentalInvoices(self._rental)
        
    def to_json(self, car: Car = None)-> dict:
        # return { "id" : self.id,
        #          "price" : self.price,
        #          "commission" : self.commission.to_json() }  
        return { "id" : self._rental.id, "options": self.options,"actions": Invoice.list_to_json(self._rental.invoices)}
    
    options: List[OptionType] = []
    _rental :Rental