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
    card_season = "Spring",
    card_info = "new season starts, progress reset to 0"):

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
      self.info = card_info
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

      # card number
      out.append(empty_row)
      out.append("| " + " " * (self.width - 9) + self.number + "/41 |")

    if self.type == "legend":

      # prepare local variables
      if self.season == "Spring":
        season_scoring = "A & B"
        season_length = 8
        season_progress = 0
      elif self.season == "Summer":
        season_scoring = "A & B"
        season_length = 8
        season_progress = 0
      elif self.season == "Fall":
        season_scoring = "A & B"
        season_length = 8
        season_progress = 0
      elif self.season == "Winter":
        season_scoring = "A & B"
        season_length = 8
        season_progress = 0
      else:
        season_scoring = "ERROR"
        season_length = 0
        season_progress = 0

      # display the season info
      out.append("| season: " + self.season + " " * (self.width - 12 - len(self.season)) + " |")
      out.append("| season scoring: " + season_scoring + " " * (self.width - 20 - len(season_scoring)) + " |")
      out.append("| season progress: " + str(season_progress) + "/" + str(season_length) + " " * (self.width - 22 - len(str(season_progress)) - len(str(season_length))) + " |")
      out.append(empty_row)

      # display the drawing legend
      out.append("| [T] Tree   [H] House  [W] Water  [F] Field  [M] Monster" + " " * (self.width - 59) + " |")
      out.append("| ---------  ---------  ---------  ---------  ---------  " + " " * (self.width - 59) + " |") 
      out.append("| | o   o |  |  ___  |  | /\/\/ |  |  / / /|  |/\___/\|  " + " " * (self.width - 59) + " |") 
      out.append("| | | o | |  | /   \ |  | /\/\/ |  | / / / |  |\ o o /|  " + " " * (self.width - 59) + " |") 
      out.append("| |   |   |  | |___| |  | /\/\/ |  |/ / /  |  | \___/ |  " + " " * (self.width - 59) + " |") 
      out.append("| ---------  ---------  ---------  ---------  ---------  " + " " * (self.width - 59) + " |") 
      out.append("| information: " + self.info + " " * (self.width - 17 - len(self.info)) + " |")

    # bottom border
    out.append("-" * self.width)

    # return
    return(out)

#def update_legend(leg, exp):

  # if its a Ruins card, update info field

# render a line for the display
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

# print the display
def update_display(sc1, sc2, sc3, sc4, exp, leg):
  
  # render lines
  l1 = render_display_line(sc1, sc2, sc3, sc4)
  l2 = render_display_line(exp, leg)  

  # print them them
  print(*l1, sep = "\n")
  print(*l2, sep = "\n")

# main
if __name__ == "__main__":

  # generate the legend
  c00 = Card(75, "legend", card_number = "00")

  # generate explore cards
  c05 = Card(25, "explore", "Temple Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "05")
  c06 = Card(25, "explore", "Outpost Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "NA", "06")
  c07 = Card(25, "explore", "Great River", 1, ["[]      ", "[]      ", "[]   (C)", "    []  ", "  [][]  ", "[][]    "], "[W]", "NA", "07")
  c08 = Card(25, "explore", "Farmland", 1, ["[]      ", "[]      ", "     (C)", "  []    ", "[][][]  ", "  []    "], "[F]", "NA", "08")
  c09 = Card(25, "explore", "Hamlet", 1, ["[]      ", "[][]    ", "     (C)", "[][][]  ", "[][]    ", "        "], "[H]", "NA", "09")
  c10 = Card(25, "explore", "Forgotten Forest", 1, ["[]      ", "  []    ", "     (C)", "[]      ", "[][]    ", "  []    "], "[T]", "NA", "10")

  # print test
  update_display(c07.rendering, c08.rendering, c09.rendering, c10.rendering, c05.rendering, c00.rendering)  

