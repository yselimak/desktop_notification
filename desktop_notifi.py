from plyer import notification

message = "hello yavuz, that is first notification"

title = "first message"

notification.notify(title=title,message=message,
                    timeout=5)

