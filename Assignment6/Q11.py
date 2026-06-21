# Q11. Create Notification, EmailNotification, SMSNotification and PushNotification classes. Override send() method.
print("Q11. Create Notification, EmailNotification, SMSNotification and PushNotification classes. Override send() method.")
class Notification:
    def send(self):
        print("Sending notification.")

class EmailNotification(Notification):
    def send(self):
        print("Email sent.")

class SMSNotification(Notification):
    def send(self):
        print("SMS sent.")

class PushNotification(Notification):
    def send(self):
        print("Push notification sent.")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send()