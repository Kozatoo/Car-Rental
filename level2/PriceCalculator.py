sales =  [
    {
        "day": 1,
        "decrease" : 10
    },
    {
        "day": 4,
        "decrease" : 30
    },
    {
        "day": 10,
        "decrease" : 50
    }    
]

def CalculatePrice(number_of_days: int, original_price: int) -> int :
    # We assume that the first day  always costs the original price
    total_price = original_price
    for index, sale in enumerate(sales):
        counted_days = 0
        if index == len(sales) - 1 or number_of_days < sales[index + 1 ]["day"] :
            counted_days = number_of_days - sale["day"] if number_of_days > sale["day"] else 0
        
        else: 
            counted_days = sales[index + 1 ]["day"] - sale["day"] 

        total_price += ( counted_days * original_price *  ( 100 - sale["decrease"]) )// 100  
        
    return total_price