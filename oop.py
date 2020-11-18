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
        self.strength = self.strength - Soldier.hit
        return self.strength
    
    
    
sold_1 = Soldier('joe', 'shmo', 600, 60)
sold_2 = Soldier('bri', 'guy', 100, 60)
sold_3 = Soldier('queen', 'bee', 60, 60)

# print('{} {}'.format(sold_1.first, sold_1.last))

# print(sold_1.fullname())
# print(sold_1.whack())

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
