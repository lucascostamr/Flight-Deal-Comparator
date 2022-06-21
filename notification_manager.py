import smtplib

MIN_PRICE_NOTIFICATION = 500
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"


class NotificationManager:
    def __init__(self, date_from, date_to, places_and_prices, name, email_to):
        with smtplib.SMTP("if your email is yahoo: smtp.mail.yahoo.com"
                          "if your email is gmail: smtp.gmail.com (gmail is blocking smtp now)",
                          port=587) as self.connections:
            self.connections.starttls()
            self.connections.login(user=EMAIL, password=PASSWORD)
            for place in places_and_prices:
                price = places_and_prices[place][0]
                link = places_and_prices[place][1]
                try:
                    self.connections.sendmail(from_addr=EMAIL,
                                              to_addrs=f"{email_to}",
                                              msg="Subject:TRAVEL OPPORTUNITY ALERT!!\n\n"
                                                  f"{name} travel to {place} "
                                                  f"at {date_from} and return at {date_to}"
                                                  f" for only: {price}$\n\nBuy now: {link}")
                except UnicodeEncodeError:
                    self.connections.sendmail(from_addr=EMAIL,
                                              to_addrs=f"{email_to}",
                                              msg="Subject:TRAVEL OPPORTUNITY ALERT!!\n\n"
                                                  f"{name} travel to {place.encode('utf-8')} "
                                                  f"at {date_from} and return at {date_to}"
                                                  f" for only: {price}$\n\nBuy now: {link}")
