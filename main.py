# generic card class
class Card:

    # main initialization
    def __init__(self,
                 card_width = 20,
                 card_type = "NA",
                 card_name = "NA",
                 card_time = "NA",
                 card_shape = "NA",
                 card_feature = "NA",
                 solo_score = "NA"
                 ):

        # variables
        self.width = card_width
        self.type = card_type
        self.name = card_name
        self.time = card_time
        self.shape = card_shape
        self.feature = card_feature
        self.stars = solo_score

    # card renderer
    def render(self):

        print("-" * self.width)
        print("| " + self.name + " " * (self.width - len(self.name) - 3) + "|")
        print(" " * self.width)


# main
if __name__ == "__main__":

    # generate a card_width
    ec = Card(25, "draw", "example", 2, ["   []  ", "[][][]  ", "        "], "[H] or [W]", 20)

    # print test
    ec.render()
