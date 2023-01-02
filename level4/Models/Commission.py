class Commission:
    insurance_fee: int
    assistance_fee: int
    drivy_fee: int
    def __init__(self, total_price: int, number_of_days:int):
        self.commissioned_part = total_price * 30 // 100
        self.insurance_fee = self.commissioned_part // 2
        self.assistance_fee = 100 * number_of_days
        self.drivy_fee = self.commissioned_part - self.assistance_fee - self.insurance_fee
        
    def to_json(self) -> dict:
        return {
            "insurance_fee": self.insurance_fee,
            "assistance_fee": self.assistance_fee,
            "drivy_fee": self.drivy_fee
            }