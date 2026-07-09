from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()

data = data_manager.get_destination_data()

notification_manager.send_notification("Test alert")

print(data)