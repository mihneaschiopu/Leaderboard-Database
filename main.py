def sorter(e):
  return e['score']

def read_scores(filename):
  scores = []
  with open(filename, "r") as file:
    for line in file:
      parts = line.strip().split(",")  # splits the line into parts based off commas in between from score.txt and strip removes spaces
      if len(parts) == 3:
        name = parts[0].strip()
        game = parts[1].strip()
        score = int(parts[2].strip())
        scores.append({"name": name, "game": game, "score": score})   # reads the scores through sections and defines them
  return scores
    
    
def display_scores(scores):
  print("All Player Scores")
  for record in scores:            # displays all scores from name, game and score from the other def
    print(record["name"], record["game"], record["score"])  # procedure
  return ''
 
   
def game(scores):
  chosen_game = input("Which game score would you like to see?")
  gamers = []
  print("All gamers for " + chosen_game)
  for record in scores:
    if record["game"].lower() == chosen_game:
      gamers.append({"name": record["name"], "score": record["score"]})
      print(record["name"], record["game"], record["score"])
    
  gamers.sort(key=sorter)
  print("Highest scorer:")
  print(gamers[len(gamers)-1])
  
        
        
  

fname = 'score.txt'
sc = read_scores(fname)
display_scores(sc)
game(sc)
print("Thank for checking the leaderboard")
