from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5) #creates 5 dices
        self.round = 0 # Starting round count
        self.wins = 0   # Initialize wins count
        self.loses = 0  # Initialize loses count
        #import ipdb; ipdb.set_trace()
        self.reset()

    def reset(self):
        self.round += 1
        self.dice = Die.create_dice(5) 
        #self.wins = 0  #eliminate so it doesnt reset the count
        #self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value  #now it sums all the values not only the instances of object class dice
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        runner=cls()
        while True:
            runner.reset()
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                #import ipdb; ipdb.set_trace()
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
               # import ipdb; ipdb.set_trace()
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                i_just_throw_an_exception()
