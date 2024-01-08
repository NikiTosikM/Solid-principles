from abc import ABC, abstractmethod


# correct solution
class Notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailSender(Notification):
    def send_notification(self, message):
        # Логика отправки по Email
        print(message)

class SMSNotification(Notification):
    def send_notification(self, message):
        # Логика отправки по SMS
        print(message)

class User(Notification):
    def __init__(self, notification_service ):
        self.notification_service = notification_service
    
    def send_notification(self, message):
        self.notification_service.send_notification(message)

email_sender = EmailSender()
user = User(email_sender)
user.send_notification("Hello!")

sms_notification = SMSNotification()
user = User( sms_notification)
user.send_notification("Hi there!")


# wrong decision
class User:
    def __init__(self):
        self.email = EmailSender()
        self.sms = SMSNotification()
    
    def send_email(self, message):
        self.email.send_notification(message)

    def send_sms(self, message):
        self.sms.send_notification(message)