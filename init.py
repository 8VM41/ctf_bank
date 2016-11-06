from account.models import *
from gift_card.models import *

currencies = {('RUB', 'Russian Rubles'),
              ('USD', 'US Dollars'),
              ('EUR', 'EU Euros')}

exchange_rates = {('RUB', 1.00),
                  ('USD', 62.50),
                  ('EUR', 67.18)}

gift_cards = {(1000, 'InnoCTF{csrf_exploitation_has_never_been_so_easy}', 'RUB'),
              (2000, 'InnoCTF{rounding_problem_is_still_alive_and_breathing}', 'RUB')}

# currency creation
for currency in currencies:
    Currency.objects.create(short_name=currency[0], long_name=currency[1])

currencies = Currency.objects.all()

# exchange rates creation
for ex_rate in exchange_rates:
    ExchangeRate.objects.create(currency=currencies.get(short_name=ex_rate[0]), rate=ex_rate[1])


# gift cards creation
for card in gift_cards:
    GiftCard.objects.create(value=card[0], text=card[1], currency=currencies.get(short_name=card[2]))