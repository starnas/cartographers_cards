import os
import math

# generic card class
class Card:

  # main initialization
  def __init__(
    self,
    c_width = 25,
    c_type = "NA",
    c_name = "NA",
    c_time = "NA",
    c_shape = "NA",
    c_feature = "NA",
    c_number = "NA",
    c_stars = "NA",
    c_season = "Spring",
    c_score = "NA",
    c_length = "NA",
    c_progress = "NA",
    c_ruin = False,
    c_info = "NA"):

      # variables
      self.width = c_width
      self.type = c_type
      self.name = c_name
      self.time = c_time
      self.shape = c_shape
      self.feature = c_feature
      self.number = c_number
      self.stars = c_stars
      self.season = c_season
      self.score = c_score
      self.length = c_length
      self.progress = c_progress
      self.ruin = c_ruin
      self.info = c_info
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
    if self.type == "explore" or self.type == "ambush":

      # prepare local variables
      name_lead = math.floor((self.width - 4 - len(self.name))/2)
      name_padd = math.ceil((self.width - 4 - len(self.name))/2)
      feat_lead = math.floor((self.width - 4 - len(self.feature))/2)
      feat_padd = math.ceil((self.width - 4 - len(self.feature))/2)

      # top part of card
      if self.type == "explore":
        out.append("| time: " + str(self.time) + " " * (self.width - 11) + " |")
      else:
        out.append("| loc: " + str(self.time) + " " * (self.width - 9 - len(self.time)) + " |")
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

      # display the season info
      out.append("| season: " + self.season + " " * (self.width - 12 - len(self.season)) + " |")
      out.append("| season scoring: " + self.score + " " * (self.width - 20 - len(self.score)) + " |")
      out.append("| season progress: " + str(self.progress) + "/" + str(self.length) + " " * (self.width - 22 - len(str(self.progress)) - len(str(self.length))) + " |")
      out.append(empty_row)

      # display the drawing legend
      out.append("|  [T] Tree      [H] House     [W] Water     [F] Field     [M] Monster  " + " " * (self.width - 74) + " |")
      out.append("|  -----------   -----------   -----------   -----------   -----------  " + " " * (self.width - 74) + " |") 
      out.append("|  |  o   o  |   |   ___   |   |  /\/\/  |   |   / / / |   | /\___/\ |  " + " " * (self.width - 74) + " |") 
      out.append("|  |  | o |  |   |  /   \  |   |  /\/\/  |   |  / / /  |   | \ o o / |  " + " " * (self.width - 74) + " |") 
      out.append("|  |    |    |   |  |___|  |   |  /\/\/  |   | / / /   |   |  \___/  |  " + " " * (self.width - 74) + " |") 
      out.append("|  -----------   -----------   -----------   -----------   -----------  " + " " * (self.width - 74) + " |") 
      out.append("| info: " + self.info + " " * (self.width - 10 - len(self.info)) + " |")

    # bottom border
    out.append("-" * self.width)

    # return
    return(out)

# function for handling updates to the legend
def update_legend(leg, exp):

  # if a Ruins card is revealed, update info field and the flag
  if exp.time == "R":
    leg.info = "ruin revealed, next shape on a ruin space if possible"
    leg.ruin = True
    leg.rendering = leg.render()
  
  # if a monster card is revaled, update info
  elif exp.type == "ambush":
    leg.info = "monster revealed!"
    leg.rendering = leg.render()

  # regular explore card
  else:

    # regular card - increment time 
    leg.progress = leg.progress + exp.time

    # check if ruin flag
    if leg.ruin:
      leg.info = "ruin previously revealed, draw on a ruin space if possible"
      leg.rendering = leg.render()
    
    # check for season end
    #if leg.progress >= leg.length:

      # check for game end

      # next season flag





# render a line for the display
def render_display_line(c1, c2 = "NA", c3 = "NA", c4 = "NA"):

  # output output list
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

  # return display as list
  return(out)

# print the display
def update_display(sc1, sc2, sc3, sc4, exp, leg):
  
  # render lines
  l1 = render_display_line(sc1, sc2, sc3, sc4)
  l2 = render_display_line(exp, leg)  

  # print them them
  print(*l1, sep = "\n")
  print(*l2, sep = "\n")
 
# define clear function
def clear():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')

# main
if __name__ == "__main__":

  # generate the legend
  c00 = Card(75, "legend", c_season = "Spring", c_score = "A & B", c_length = 8, c_progress = 0, c_info = "new season starts, progress reset to 0")

  # generate ambush cards
  c01 = Card(25, "ambush", "Goblin Attack", "bottom-right", ["  <---  ", " c-clock", "  --->  ", "[]      ", "  []    ", "    []  "], " ", "01")
  c02 = Card(25, "ambush", "Bugbear Assault", "top-right", ["  --->  ", "  clock ", "  <---  ", "[]  []  ", "[]  []  ", "        "], " ", "02")
  c03 = Card(25, "ambush", "Kobold Onslaught", "bottom-left", ["  --->  ", "  clock ", "  <---  ", "[]      ", "[][]    ", "[]      "], " ", "03")
  c04 = Card(25, "ambush", "Gnoll Raid", "top-left", ["  <---  ", " c-clock", "  --->  ", "[][]    ", "[]      ", "[][]    "], " ", "04")

  # generate explore cards
  c05 = Card(25, "explore", "Temple Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "05")
  c06 = Card(25, "explore", "Outpost Ruins", "R", [" __     ", " || __  ", " || ||  "], " ", "06")
  c07 = Card(25, "explore", "Great River", 1, ["[]      ", "[]      ", "[]   (C)", "      []", "    [][]", "  [][]  "], "[W]", "07")
  c08 = Card(25, "explore", "Farmland", 1, ["[]      ", "[]      ", "     (C)", "    []  ", "  [][][]", "    []  "], "[F]", "08")
  c09 = Card(25, "explore", "Hamlet", 1, ["[]      ", "[][]    ", "     (C)", "  [][][]", "  [][]  ", "        "], "[H]", "09")
  c10 = Card(25, "explore", "Forgotten Forest", 1, ["[]      ", "  []    ", "     (C)", "  []    ", "  [][]  ", "    []  "], "[T]", "10")
  c11 = Card(25, "explore", "Hinterland Stream", 2, ["[][][]  ", "[]      ", "[]      "], "[F] / [W]", "11")
  c12 = Card(25, "explore", "Homestead", 2, ["  []    ", "  [][]  ", "  []    "], "[H] / [F]", "12")
  c13 = Card(25, "explore", "Orchard", 2, ["[][][]  ", "    []  ", "        "], "[T] / [F]", "13")
  c14 = Card(25, "explore", "Treetop Village", 2, ["    [][]", "[][][]  ", "        "], "[T] / [H]", "14")
  c15 = Card(25, "explore", "Marshlands", 2, ["[]      ", "[][][]  ", "[]      "], "[T] / [W]", "15")
  c16 = Card(25, "explore", "Fishing Village", 2, ["        ", "[][][][]", "        "], "[H] / [W]", "16")
  c17 = Card(25, "explore", "Rift Lands", 0, ["        ", "  []    ", "        "], "[T]/[H]/[F]/[W]/[M]", "17")

  # generate explore deck
  deck_explore = [c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17]

  # season cards
  c18 = Card(25, "season", "Spring", "R", ["        ", "        ", "        "], "A & B", "18")
  c18 = Card(25, "season", "Spring", "R", ["        ", "        ", "        "], "A & B", "18")
  c18 = Card(25, "season", "Spring", "R", ["        ", "        ", "        "], "A & B", "18")
  c18 = Card(25, "season", "Spring", "R", ["        ", "        ", "        "], "A & B", "18")

  # edict cards
  # c22, c23, c24, c25

  

  # generate scoring cards

  # print test
  
  update_legend(c00, c05)
  clear()
  update_display(c07.rendering, c08.rendering, c09.rendering, c10.rendering, c05.rendering, c00.rendering)  

  update_legend(c00, c11)
  clear()
  update_display(c13.rendering, c14.rendering, c15.rendering, c16.rendering, c17.rendering, c00.rendering)  

  update_legend(c00, c01)
  clear()
  update_display(c01.rendering, c02.rendering, c03.rendering, c04.rendering, c01.rendering, c00.rendering)  