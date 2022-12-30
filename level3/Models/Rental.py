from datetime import datetime
class Rental:
    def __init__(self, car_id: int , start_date: str, end_date: str, distance: int) -> None:
        self.car_id = car_id
        date_format ="%Y-%m-%d"
        try:
            self.start_date = datetime.strptime(start_date, date_format)
            self.end_date = datetime.strptime(end_date, date_format)
        except ValueError:
            print(f"Invalid data format: {end_date, start_date} ")
            raise Exception
        self.distance = distance

    def rentalDuration(self) -> int :
        return (self.end_date-self.start_date).days + 1
        
    car_id: int 
    start_date: datetime
    end_date: datetime
    distance: int


