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
                 solo_score = "NA",
                 card_number = "NA"
                 ):

        # variables
        self.width = card_width
        self.type = card_type
        self.name = card_name
        self.time = card_time
        self.shape = card_shape
        self.feature = card_feature
        self.stars = solo_score
        self.number = card_number
        self.rendering = self.render()

    # card renderer
    def render(self):

        # output list
        out = []

        # top border
        out.append("-" * self.width)

        # card type selector
        if self.type == "explore":

            name_lead = math.floor((self.width - 4 - len(self.name))/2)
            name_padd = math.ceil((self.width - 4 - len(self.name))/2)
            feat_lead = math.floor((self.width - 4 - len(self.feature))/2)
            feat_padd = math.ceil((self.width - 4 - len(self.feature))/2)

            out.append("| time: " + str(self.time) + " " * (self.width - 11) + " |")
            out.append("| " + " " * (self.width - 4) + " |")
            out.append("| " + " " * name_lead + self.name + " " * name_padd + " |")
            out.append("| " +  " " * (self.width - 4) + " |")
            out.append("| " + " " * feat_lead + self.feature + " " * feat_padd + " |")
            out.append("| " +  " " * (self.width - 4) + " |")

            # check for 1 or 2 shapes
            if len(self.shape) == 3:

                out.append("| " + " " * (self.width - 18) + self.shape[0] + " " * (self.width - 19) + " |")
                out.append("| " + " " * (self.width - 18) + self.shape[1] + " " * (self.width - 19) + " |")
                out.append("| " + " " * (self.width - 18) + self.shape[2] + " " * (self.width - 19) + " |")

            if len(self.shape) == 6:

                out.append("| " + " " * (self.width - 24) + self.shape[0] + " | " + self.shape[3] + " " * (self.width - 24) + " |")
                out.append("| " + " " * (self.width - 24) + self.shape[1] + " | " + self.shape[4] + " " * (self.width - 24) + " |")
                out.append("| " + " " * (self.width - 24) + self.shape[2] + " | " + self.shape[5] + " " * (self.width - 24) + " |")

        # solo score
        out.append("| " +  " " * (self.width - 4) + " |")
        out.append("| " + " " * (self.width - 9) + self.number + "/41 |")

        # bottom border
        out.append("-" * self.width)

        # return
        return(out)

# main
if __name__ == "__main__":

    # generate a card_width
    c07 = Card(25, "explore", "Great River", 1,
                ["  []    ", "  []    ", "  []   C",
                 "    []  ", "  [][]  ", "[][]    "],
                "[W]", "NA", "07")

    # print test
    print(*c07.rendering, sep = "\n")
