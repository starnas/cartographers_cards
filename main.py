import math

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

        if self.type == "draw":

            feat_lead = math.floor((self.width - 4 - len(self.feature))/2)
            feat_padd = math.ceil((self.width - 4 - len(self.feature))/2)

            print("| " + self.name + " " * (self.width - len(self.name) - 4) + " |")
            print("| " +  " " * (self.width - 4) + " |")
            print("| " + " " * feat_lead + self.feature + " " * feat_padd + " |")
            print("| " +  " " * (self.width - 4) + " |")

            # check for 1 or 2 shapes
            if len(self.shape) == 3:

                print("| " + " " * (self.width - 18) + self.shape[0] + " " * (self.width - 19) + " |")
                print("| " + " " * (self.width - 18) + self.shape[1] + " " * (self.width - 19) + " |")
                print("| " + " " * (self.width - 18) + self.shape[2] + " " * (self.width - 19) + " |")

            if len(self.shape) == 6:



        print("-" * self.width)


# main
if __name__ == "__main__":

    # generate a card_width
    ec1 = Card(25, "draw", "example", 2, ["    []  ", "[][][]  ", "        "], "[H] or [W]", 20)
    ec2 = Card(25, "draw", "example", 2, ["    []  ", "[][][]  ", "        ", "  []    ", "[][][]  ", "  []    "], "[F]", 20)

    # print test
    ec1.render()
    ec2.render()
