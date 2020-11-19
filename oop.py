# Comment


class Soldier:

    hit = 10
    
    def __init__(self, first, last, weight, strength):
        self.first = first
        self.last = last
        self.weight = weight
        self.strength = strength
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def whack(self):
        self.strength = self.strength - self.hit
        return self.strength

    @classmethod
    def set_hit(cls, amount):
        cls.hit = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return "Soldier('{}', '{}')".format(self.fullname(), self.weight)

class Enemy(Soldier):
    hit = 5

    def __init__(self, first, last, weight, strength, type):
        super().__init__(first, last, weight, strength)
        self.type = type

class Manager(Soldier):

    def __init__(self, first, last, weight, strength, soldiers=None):
        super().__init__(first, last, weight, strength)
        if soldiers is None:
            self.soldiers = []
        else:
            self.soldiers = soldiers

    def add_sold(self, sold):
        if sold not in self.soldiers:
            self.soldiers.append(sold)

    def remove_sold(self, sold):
        if sold in self.soldiers:
            self.soldiers.remove(sold)

    def print_sold(self):
        for sold in self.soldiers:
            print('-->', sold.fullname())


bad_1 = Enemy('big', 'loser', 1000, 30, 'squeek')
bad_2 = Enemy('lil', 'baby', 1000, 30, 'chonker')

print(bad_1)

mgr_1 = Manager('boss', 'boi', 300, 700, [bad_1])

print(issubclass(Manager, Enemy))

print(mgr_1.weight)

mgr_1.add_sold(bad_2)
mgr_1.remove_sold(bad_1)

mgr_1.print_sold()
# print(help(Enemy))

sold_1 = Soldier('joe', 'shmo', 600, 60)
sold_2 = Soldier('bri', 'guy', 100, 60)
sold_3 = Soldier('queen', 'bee', 60, 60)

print(bad_1.type)
bad_1.whack()
print(bad_1.strength)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Soldier.is_workday(my_date))

# print('{} {}'.format(sold_1.first, sold_1.last))

# print(sold_1.fullname())
# print(sold_1.whack())

# print(Soldier.hit)
# print(sold_1.hit)
# print(sold_2.hit)

dude = input('Do you want to be joe, queen or bri? ')

while True:    
    if dude == 'joe':
        print('Your full name is ' + sold_1.fullname())
        break
    if dude == 'bri':
        print('Your full name is ' + sold_2.fullname())
        break
    if dude == 'queen':
        print('Your full name is ' + sold_3.fullname())
        break

question = input('Do you want to hit someone? yes or no ')

while sold_1.strength != 0 and sold_2.strength !=0 and sold_3.strength !=0:
    if question == 'yes':
        who = input('Who joe, bri, or queen ')
        if who == 'joe':
            print('You just hit joe for 10 hp')
            sold_1.stength = sold_1.whack()
            print('Joe now has', sold_1.strength,'hp')
            continue
        elif who == 'bri':
             print('You just hit bri for 10 hp')
             sold_2.stength = sold_2.whack()
             print('bri now has', sold_2.strength,'hp')
        elif who == 'queen':
             print('You just hit queen for 10 hp')
             sold_3.stength = sold_3.whack()
             print('queen now has', sold_3.strength,'hp')
        
print('You killed them!')
