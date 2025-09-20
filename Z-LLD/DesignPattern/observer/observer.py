from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete observers
class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email Subscriber received: {message}")

class SMSSubscriber(Observer):
    def update(self, message):
        print(f"SMS Subscriber received: {message}")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete subject
class NewsAgency(Subject):
    def __init__(self):
        self.observers = []
        self.latest_news = None

    def register(self, observer: Observer):
        self.observers.append(observer)

    def unregister(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.latest_news)

    def add_news(self, news):
        self.latest_news = news
        self.notify()

# Client code
news_agency = NewsAgency()
email_sub = EmailSubscriber()
sms_sub = SMSSubscriber()

news_agency.register(email_sub)
news_agency.register(sms_sub)

news_agency.add_news("Breaking News: Observer Pattern Explained!")



# 🔹 Key Points
# 	1.	Subject → NewsAgency (maintains state and observers)
# 	2.	Observer → EmailSubscriber, SMSSubscriber (react to state changes)
# 	3.	Decoupled → Subject doesn’t care how observers handle updates
# 	4.	Dynamic → Observers can register/unregister anytime
#
# ⸻
#
# 🔹 Interview Tip
#
# “Observer pattern is useful when multiple objects need to be notified of changes
# in another object without tightly coupling them. The subject maintains a list of observers and notifies them automatically.”