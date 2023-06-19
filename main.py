import math

# generic card class
class Card:

  # main initialization
  def __init__(
    self,
    card_width = 20,
    card_type = "NA",
    card_name = "NA",
    card_time = "NA",
    card_shape = "NA",
    card_feature = "NA",
    solo_score = "NA",
    card_number = "NA"):

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

      # prepare local variables
      name_lead = math.floor((self.width - 4 - len(self.name))/2)
      name_padd = math.ceil((self.width - 4 - len(self.name))/2)
      feat_lead = math.floor((self.width - 4 - len(self.feature))/2)
      feat_padd = math.ceil((self.width - 4 - len(self.feature))/2)
      empty_row = "| " + " " * (self.width - 4) + " |"

      # top part of card
      out.append("| time: " + str(self.time) + " " * (self.width - 11) + " |")
      out.append(empty_row)
      out.append("| " + " " * name_lead + self.name + " " * name_padd + " |")
      out.append(empty_row)
      out.append("| " + " " * feat_lead + self.feature + " " * feat_padd + " |")
      out.append(empty_row)

      # check for 1 or 2 shapes
      for i in range(3):

        if len(self.shape) == 3:
          out.append("| " + " " * (self.width - 18) + self.shape[i] + " " * (self.width - 19) + " |")

        if len(self.shape) == 6:
          out.append("| " + " " * (self.width - 24) + self.shape[i] + " | " + self.shape[i+3] + " " * (self.width - 24) + " |")

    # card number
    out.append(empty_row)
    out.append("| " + " " * (self.width - 9) + self.number + "/41 |")

    # bottom border
    out.append("-" * self.width)

    # return
    return(out)

# main
if __name__ == "__main__":

  # generate explore cards
  c05 = Card(25, "explore", "Temple Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "05")
  c06 = Card(25, "explore", "Outpost Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "06")
  c07 = Card(25, "explore", "Great River", 1, ["[]      ", "[]      ", "[]   (C)", "    []  ", "  [][]  ", "[][]    "], "[W]", "NA", "07")
  c08 = Card(25, "explore", "Farmland", 1, ["[]      ", "[]      ", "     (C)", "  []    ", "[][][]  ", "  []    "], "[F]", "NA", "08")
  c09 = Card(25, "explore", "Hamlet", 1, ["[]      ", "[][]    ", "     (C)", "[][][]  ", "[][]    ", "        "], "[H]", "NA", "09")

  # print test
  print(*c07.rendering, sep = "\n")
  print(*c08.rendering, sep = "\n")
  print(*c09.rendering, sep = "\n")

