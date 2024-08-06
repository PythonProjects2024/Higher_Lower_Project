import random


# from game_data import data
from art import logo, vs

data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman and Self-Made Billionaire",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
]

score = 0
game_should_continue = True


def random_choices():
    """Get two distinct random choices from the data."""
    compare_A = random.choice(data)
    compare_B = random.choice(data)
    while compare_A == compare_B:
        compare_B = random.choice(data)
    return compare_A, compare_B


def comparison():
  global score, game_should_continue
  while game_should_continue:
    compare_A, compare_B = random_choices()
   
    print(logo)
    
    print(
        f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}"
    )
    print(vs)

    print(
        f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_A['country']}"
    )
    # Debugging prints
    print(
        f"Follower count A: {compare_A['follower_count']}, Follower count B: {compare_B['follower_count']}"
    )

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
   
    if (guess == "a" and compare_A["follower_count"] > compare_B["follower_count"]) or \
    (guess == "b" and compare_B["follower_count"] > compare_A["follower_count"]):
     
      score += 1
      print(f"You're right! Current score: {score}")
      
    
    elif guess != "a" and guess != "b":
      print("Invalid input. Please try again.")
       
      
    
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_should_continue = False

 

    print()


comparison()