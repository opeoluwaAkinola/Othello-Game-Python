
# Create player class
class Player:
    # Function to initialise player class
    def __init__(self):
        self.name = ""
        self.score = 0
        self.color = ""

    # Function to store name

    def name_update(self, **kwargs):
        for key, value in kwargs.items():
            self.name = kwargs[key]



    # Function to store score

    def score_update(self, **kwargs):
        for key, value in kwargs.items():
            self.score = value


    # Function to store color

    def color_update(self, **kwargs):
        for key, value in kwargs.items():
            self.color = value


    # Function to check player input
    def checkInput(self, inputs):
        if inputs[0] < 'a' or inputs[0] > 'h':
            return False
        # check if the integer part is within 1 and 8
        if inputs[1] < '1' or inputs[1] > '8':
            return False
        # if no issue,return True
        return True







player_1 = Player()
player_2 = Player()
