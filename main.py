from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData

data_manager = DataManager()
notification_manager = NotificationManager()

data = data_manager.get_destination_data()

notification_manager.send_notification("Test alert")

print(data)

flight = FlightData(
    price=120,
    origin_airport="MUC",
    destination_airport="PAR",
    out_date="2026-08-10",
    return_date="2026-08-17",
)

print(flight.price)
print(flight.origin_airport)
print(flight.destination_airport)
print(flight.out_date)
print(flight.return_date)