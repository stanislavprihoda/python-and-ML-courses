class Card:
    values = {'Ace': [1, 11], '1': [1], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6],
              '7': [7], '8': [8], '9': [9], '10': [10], 'Jack': [10], 'Queen': [10], 'King': [10]}

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_card(self):
        return (self.value,self.color)

    def get_points(self):
        points=Card.values[self.value]
        return points
