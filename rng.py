from random import randint




class  Item:

    def __init__(self, name, ilvl, roll):
        self.name = name
        self.ilvl = ilvl
        self.roll = roll
    def fullname(self):
        return '{} {} {}'.format(self.name, self.ilvl, self.roll)

    def rolldice(self):
        return randint(0, 100)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def GetIlvl(self):
        return self.ilvl

    pass







multi_low_item = 1

item1 = Item('head',340,0)
item1.roll = 1.5 * item1.rolldice()

item2 = Item('neck',365,0)
item2.roll = 1 * item2.rolldice()

item3 = Item('shoulder',355,0)
item3.roll = 1.2* item3.rolldice()

item4 = Item('cloak',370,0)
item4.roll = 0.9 * item4.rolldice()

item5 = Item('chest',370,0)
item5.roll = 0.9 * item5.rolldice()

item6 = Item('bracer',355,0)
item6.roll = 1.2 * item6.rolldice()

item7 = Item('glove',355,0)
item7.roll = 1.2 * item7.rolldice()

item8 = Item('belt',360,0)
item8.roll = 1.1 * item8.rolldice()

item9 = Item('pants',345,0)
item9.roll = 1.4 * item9.rolldice()

item10 = Item('boots',340,0)
item10.roll = 1.5 * item10.rolldice()

item11 = Item('ring1',340,0)
item11.roll = 1.5 * item11.rolldice()

item12 = Item('ring2',340,0)
item12.roll = 1.5 * item12.rolldice()

item13 = Item('trinket1',340,0)
item13.roll = 1.5 * item13.rolldice()

item14 = Item('trinket2',355,0)
item14.roll = 1.2 * item14.rolldice()

item15 = Item('MH',340,0)
item15.roll = 1.5 * item15.rolldice()

item16 = Item('OH',345,0)
item16.roll = 1.4 * item16.rolldice()

item17 = Item('2H',340,0)
item17.roll = 1.4 * item17.rolldice()



itemlist = []
"""list dualwield"""
itemlist = (item1,item2,item3,item4,
            item5,item6,item7,item8,
            item9,item10,item11,item12,
            item13,item14,item15,item16
            )
itemlist2h = (item1.GetIlvl(),item2.GetIlvl(),item3.GetIlvl(),item4.GetIlvl(),
            item5.GetIlvl(),item6.GetIlvl(),item7.GetIlvl(),item8.GetIlvl(),
            item9.GetIlvl(),item10.GetIlvl(),item11.GetIlvl(),item12.GetIlvl(),
            item13.GetIlvl(),item14.GetIlvl(),item17.GetIlvl()
            )

itemlisttest = (item1,item2,item3,item4)

def my_min(sequence):
    """return the minimum element of sequence"""
    low = sequence[0] # need to start with some value
    for i in sequence:
        if i.ilvl < low.ilvl:
            low.ilvl = i.ilvl
            low.name = i.name
            low.roll = i.roll
    return low

def my_max(sequence):
    high = sequence[0]  # need to start with some value
    for i in sequence:
        if i.roll > high.roll:
            high.roll = i.roll
            high.name = i.name
            high.ilvl = i.ilvl
    return high





itemobjectlist = []
itemobjectlist = (item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16 )

"""print(item1.fullname())"""

print('Roll weights were added at rate of 0.1 multiplier per 5ilvl dif compared to lowest item ilvl available in the dropped gear')
print('................')
print(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,sep='\n')
print('................')
print(my_min(itemobjectlist).fullname(), 'lowest ilvl')
max = my_max(itemobjectlist)
print(max.fullname(),  'highest roll')
