from operator import itemgetter


class vod:
    """Водитель"""

    def __init__(self, id, name, zp, avto_id):
        self.id = id
        self.name = name
        self.zp = zp
        self.avto_id = avto_id


class avtopark:
    """Автопарк"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class vodavto:
    """
    'Водители автопарков' для реализации
    связи многие-ко-многим
    """

    def __init__(self, vod_id, avto_id):
        self.vod_id = vod_id
        self.avto_id = avto_id


avtoparks = [
    avtopark(1, 'Yandex'),
    avtopark(2, 'Yandex'),
    avtopark(3, 'Uber'),
    avtopark(123, 'Gett'),
    avtopark(321, '777'),
]

vods = [
    vod(321, 'Bibikov', 3500, 1),
    vod(123, 'Tkachenko', 2500, 2),
    vod(13, 'Eremihin', 4500, 3),
    vod(14, 'Dolinski', 2500, 3),
    vod(154, 'Kim', 10000, 123),
    vod(21, 'Azamat', 10000, 321),
]
vodavtos = [
    vodavto(321, 1),
    vodavto(123, 2),
    vodavto(13, 3),
    vodavto(14, 3),
    vodavto(154, 123),
    vodavto(21, 321),
]

"""Основная функция"""

# Соединение данных один-ко-многим
one_to_many = [(e.name, e.zp, d.name)
               for d in avtoparks
               for e in vods
               if e.avto_id == d.id]

# Соединение данных многие-ко-многим
many_to_many_temp = [(d.name, ed.avto_id, ed.vod_id)
                     for d in avtoparks
                     for ed in vodavtos
                     if d.id == ed.avto_id]
many_to_many = [(e.name, e.zp, name)
                for name, avto_id, vod_id in many_to_many_temp
                for e in vods if e.id == vod_id]

print('Задание Б1')
res_11 = sorted(one_to_many, key=itemgetter(2))
print(res_11)

print('\nЗадание Б2')
a = list(set([i.name for i in avtoparks]))
res_12 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key=itemgetter(1))
print(res_12)

print('\nЗадание Б3')
b = [j for j in many_to_many if j[0][-1:] == 'v']
res_13 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
print(res_13)
