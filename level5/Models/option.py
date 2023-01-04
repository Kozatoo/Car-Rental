import enum
class OptionType(enum.Enum):
    GPS = "gps"
    BabySeat = "baby_seat"
    AdditionalInsurance = "additional_insurance"
    
    @staticmethod
    def from_string(string: str):
        if type(string) != str:
            raise TypeError(f"parameter {string} is not a string")
        for member in OptionType:
            if member.value == string:
                return member
        raise ValueError(f"{string} is not a valid Option")