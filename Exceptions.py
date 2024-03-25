from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class TooManyMessagesException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.timestamp = getCurrentTime()
        print("TooManyMessagesException raised at:", self.timestamp)

class Messenger:
    def __init__(self, listeners=None):
        self.listeners = listeners or []
        self.message_count = 0
        self.MAX_MESSAGE_LIMIT = 10

    def send(self, message):
        if self.message_count >= self.MAX_MESSAGE_LIMIT:
            raise TooManyMessagesException("Exceeded maximun message limit")
        else:
            for listener in self.listeners:
                listener.receive(message)
            self.message_count += 1

    def receive(self, message):
        pass


if __name__ == "__main__":
    messenger = Messenger()
    num_message = int(input("Enter number of messages: "))
    for i in range(num_message):
        try:
            messenger.send("Message " + str(i + 1))
        except TooManyMessagesException as e:
            print(e)