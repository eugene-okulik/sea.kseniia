PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
new_list = PRICE_LIST.split()
prices_with_r = new_list[1::2]
prices = [int(price.strip('р')) for price in prices_with_r]
new_dict = dict(zip(new_list[::2], prices))
print(new_dict)
