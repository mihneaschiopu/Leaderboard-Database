def sorter(e): # sorts based off score
  return e['score'] # sets score as a key with a paramneter

def read_scores(filename):  # gets scores from score.tct
  scores = []
  with open(filename, "r") as file: # puts in read mode (r = read) (w = write)
    for line in file: #loops through each line of the file
      parts = line.strip().split(",")  # splits the line into parts based off commas in between from score.txt and strip removes spaces
      if len(parts) == 3:
        name = parts[0].strip()
        game = parts[1].strip()  # creates names to the parts of the txt file so we can use for code and cant go to 3 because it starts at 0 
        score = int(parts[2].strip())
        scores.append({"name": name, "game": game, "score": score})   # reads the scores through sections and defines them
  return scores
    
    
def display_scores(scores): # displays the scores variable
  print("All Player Scores") # prints header
  for record in scores:            # displays all scores from name, game and score from the other def
    print(record["name"], record["game"], record["score"])  # print name, game and score on github
  return '' # procedure
 
   
def game(scores): 
  chosen_game = input("Which game score would you like to see?") # asks what score the user would like to see
  gamers = [] # gamers is a separate list consisting of the people
  print("All gamers for " + chosen_game) # prints the game chosen and all the people inside it
  for record in scores:
    if record["game"].lower() == chosen_game:
      gamers.append({"name": record["name"], "score": record["score"]})  # gamers list is appended
      print(record["name"], record["game"], record["score"]) # prints all records
    
  gamers.sort(key=sorter) # uses key sorter 
  print("Highest scorer:")
  print(gamers[len(gamers)-1]) # because list goes to 3 you cant have a 3rd section of list so you take one away
  
        
        
 # outside functions

fname = 'score.txt'  # f name is score.txt file
sc = read_scores(fname) # sc is for reading scores from fname and runs read scores function
display_scores(sc)  # displays the scores from read scores from fname also runs the function
game(sc) # runs game function
print("Thank for checking the leaderboard")
