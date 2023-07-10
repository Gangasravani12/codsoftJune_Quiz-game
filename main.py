def quizgame():
  print('Welcome to the quiz!')
  score = 0

  while True:
    playing = input('Do you want to play the game? (yes/no) ')
    if playing.lower() == "no":
      break
    elif playing.lower() != "yes":
      print("Invalid input. Please enter 'yes' or 'no'.")
      continue
    print('Instructions: ')
    print('You should write correct spelling otherwise your answer will be incorrect! ')
    
    print('Let\'s play!')

    answer = input('Which planet has the most moons? ')
    if answer.lower() == "saturn":
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
      print('The correct answer is Saturn.')

    answer = input('What country has won the most World Cups? ')
    if answer.lower() == "brazil":
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
      print('The correct answer is Brazil.')

    answer = input('How many faces does a Dodecahedron have? ')
    if answer == "12":
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
      print('The correct answer is 12.')

    answer = input('How many bones do we have in an ear? ')
    if answer == "3":
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
      print('The correct answer is 3.')

    print('You have completed the quiz!')
    if score == 4:
      print('Congratulations! You won the game.')
    print('Your score is', score)
    score = 0  # Reset the score for the next game

quizgame()