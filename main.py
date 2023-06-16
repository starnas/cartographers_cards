
# score card class
class Card_score:

    # main initialization
    def __init__(self, table_name):

        # card name
        self.name = card_name
        self.type = card_type
        self.text = card_text
        self.image = card_image

# drawing card class

# card renderer
def render_card(tc):

    card_width = 20
    print("-" * card_width)
    print("| " + tc.name + " " * (card_width - len(tc.name) - 3) + "|")
    print(" " * card_width)


# main
if __name__ == "__main__":

    # generate a card_width
    ec = Card("example")

    # print test
    render_card(ec)
