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
    card_number = "NA",
    card_season = "NA",
    card_sTime = "NA",
    card_sLength = "NA"):

      # variables
      self.width = card_width
      self.type = card_type
      self.name = card_name
      self.time = card_time
      self.shape = card_shape
      self.feature = card_feature
      self.stars = solo_score
      self.number = card_number
      self.season = card_season
      self.sTime = card_sTime
      self.sLength = card_sLength
      self.rendering = self.render()

  # card renderer
  def render(self):

    # output list
    out = []

    # top border
    out.append("-" * self.width)
    
    # an empty row 
    empty_row = "| " + " " * (self.width - 4) + " |"

    # card type selector
    if self.type == "explore":

      # prepare local variables
      name_lead = math.floor((self.width - 4 - len(self.name))/2)
      name_padd = math.ceil((self.width - 4 - len(self.name))/2)
      feat_lead = math.floor((self.width - 4 - len(self.feature))/2)
      feat_padd = math.ceil((self.width - 4 - len(self.feature))/2)

      # top part of card
      out.append("| time: " + str(self.time) + " " * (self.width - 11) + " |")
      out.append(empty_row)
      out.append("| " + " " * name_lead + self.name + " " * name_padd + " |")
      out.append(empty_row)
      out.append("| " + " " * feat_lead + self.feature + " " * feat_padd + " |")
      out.append(empty_row)

      # check for 1 or 2 shapes
      for i in range(3):

        # single shape render
        if len(self.shape) == 3:
          out.append("| " + " " * (self.width - 18) + self.shape[i] + " " * (self.width - 19) + " |")

        # double shape render
        if len(self.shape) == 6:
          out.append("| " + " " * (self.width - 24) + self.shape[i] + " | " + self.shape[i+3] + " " * (self.width - 24) + " |")

    if self.type == "legend":

      # prepare local variables

      # display the season
      out.append("| season: " + self.season + " " * (self.width - 12 - len(self.season)) + " |")
      out.append(empty_row)

      # display time in season
      out.append("| season progress: " + str(self.sTime) + "/" + str(self.sLength) + " " * (self.width - 22 - len(str(self.sTime)) - len(str(self.sLength))) + " |")      
      out.append(empty_row)

      out.append(empty_row) 
      out.append(empty_row) 
 
      out.append(empty_row) 
      out.append(empty_row) 
      out.append(empty_row) 

    # card number
    out.append(empty_row)
    out.append("| " + " " * (self.width - 9) + self.number + "/41 |")

    # bottom border
    out.append("-" * self.width)

    # return
    return(out)

# display render
def render_display_line(c1, c2 = "NA", c3 = "NA", c4 = "NA"):

  out = []

  for i in range(len(c1)):
    out_line = c1[i]
    if c2 != "NA":
      out_line = out_line + c2[i]
    if c3 != "NA":
      out_line = out_line + c3[i]
    if c4 != "NA":
      out_line = out_line + c4[i]
    out.append(out_line)

  return(out)


# main
if __name__ == "__main__":

  # generate the legend
  c00 = Card(75, "legend", card_number = "00", card_season = "Spring", card_sTime = 0, card_sLength = 8)

  # generate explore cards
  c05 = Card(25, "explore", "Temple Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "05")
  c06 = Card(25, "explore", "Outpost Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "06")
  c07 = Card(25, "explore", "Great River", 1, ["[]      ", "[]      ", "[]   (C)", "    []  ", "  [][]  ", "[][]    "], "[W]", "NA", "07")
  c08 = Card(25, "explore", "Farmland", 1, ["[]      ", "[]      ", "     (C)", "  []    ", "[][][]  ", "  []    "], "[F]", "NA", "08")
  c09 = Card(25, "explore", "Hamlet", 1, ["[]      ", "[][]    ", "     (C)", "[][][]  ", "[][]    ", "        "], "[H]", "NA", "09")
  c10 = Card(25, "explore", "Forgotten Forest", 1, ["[]      ", "  []    ", "     (C)", "[]      ", "[][]    ", "  []    "], "[T]", "NA", "10")

  # print test
  #print(*c07.rendering, sep = "\n")
  #print(*c08.rendering, sep = "\n")
  #print(*c09.rendering, sep = "\n")
  l1 = render_display_line(c07.rendering, c08.rendering, c09.rendering, c10.rendering)
  l2 = render_display_line(c07.rendering, c00.rendering)  

  print(*l1, sep = "\n")
  print(*l2, sep = "\n")
