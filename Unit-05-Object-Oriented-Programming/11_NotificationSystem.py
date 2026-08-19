# ----------------------------------------------------
# Description:
# This program demonstrates abstraction and polymorphism
# using different notification methods.
# ----------------------------------------------------

from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push notification sent: {message}")


print("1. Email")
print("2. SMS")
print("3. Push Notification")

choice = int(input("Choose notification type: "))
message = input("Enter your message: ")

if choice == 1:
    notification = EmailNotification()

elif choice == 2:
    notification = SMSNotification()

elif choice == 3:
    notification = PushNotification()

else:
    notification = None
    print("Invalid choice.")

if notification:
    notification.send(message)