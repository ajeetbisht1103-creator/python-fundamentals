# ----------------------------------------------------
# Description:
# This program demonstrates runtime polymorphism
# by allowing different notification classes to
# implement the same send() method differently.
# ----------------------------------------------------

class Notification:

    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push notification sent: {message}")


message = input("Enter notification message: ")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send(message)