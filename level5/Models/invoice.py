
from typing import List
from Models.rental import *
import enum

class InvoiceType(enum.Enum):
    Credit = "credit"
    Debit = "debit"
    
class Invoice:
    def __init__(self, who:str, type: InvoiceType, amount: int) -> None:
        self.who= who
        self.type= type
        self.amount= amount
        
    @staticmethod
    def getRentalInvoices(rental) -> List["Invoice"]:
        return [Invoice("driver", InvoiceType.Debit, rental.price),
                Invoice("owner", InvoiceType.Credit, rental.price - rental.commission.commissioned_part),
                Invoice("insurance", InvoiceType.Credit, rental.commission.insurance_fee),
                Invoice("assistance", InvoiceType.Credit, rental.commission.assistance_fee),
                Invoice("drivy", InvoiceType.Credit, rental.commission.drivy_fee)]

    def to_json(self) -> dict : 
        return {
            "who" : self.who,
            "type" : self.type.value,
            "amount" : self.amount
        }
    
    @staticmethod
    def list_to_json(invoices: List["Invoice"]) -> dict:
        result = []
        for invoice in invoices:
            result.append(invoice.to_json())
        return result