mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}
"""Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
"""
#  Your Code Starts from here
import random
i = 0
while i < len(mobile_data.get('data')):
    model = mobile_data.get('data')[i].get('name')
    origin = mobile_data.get('data')[i].get('made')
    mobilePrice = mobile_data.get('data')[i].get('price')
    price = mobilePrice.split(' ')[0]
    BDT_price = int(mobile_data.get('exchnage_rate')*float(price))
    # template = f'{model} is made in {origin}. The price is {mobilePrice} which is almost equal to {BDT_price}'
    # print(template)
    # i+=1
    sentence_one_list = [f'{model} is made in {origin}.',
                     f'{origin} made the {model}.',
                     f'{model} is made by {origin}.',
                     f'{model} manufactured by {origin}.']
    sentence_two_list = [f'The price is {mobilePrice} which is almost equal to {BDT_price} taka.',
                    f'The price is {mobilePrice} in worldwide for this perticular device and in BD {BDT_price} taka.',
                    f'The market price in BD market is {BDT_price} taka where the price in international market is {mobilePrice}.',
                    f'The price is {mobilePrice} in international market where {BDT_price} taka in Bangladesh.'
                     ]
    sentence_one = random.choice(sentence_one_list)
    sentence_two = random.choice(sentence_two_list)
    print(sentence_one, sentence_two)
    i+=1