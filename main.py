import random, game_data
from art import logo, vs
print(logo)
compare_a = random.choice(game_data.data)
print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']} with {compare_a['follower_count']}")
print(vs)
compare_b = random.choice(game_data.data)
print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']} with {compare_b['follower_count']}")

count = 0
guess_flag = True
while guess_flag:
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == 'A':
        if compare_a['follower_count'] > compare_b['follower_count']:
            count += 1
            print(f"You're right! Current score: {count}")
            print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']} with {compare_a['follower_count']}")
            print(vs)
            compare_b = random.choice(game_data.data)
            print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']} with {compare_b['follower_count']} ")
            guess_flag = True

        else:
            guess_flag = False
            print(f"Sorry, that's wrong. Final score: {count}")

    elif guess == 'B':
            if compare_b['follower_count'] > compare_a['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
                compare_a = compare_b
                print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']} with {compare_a['follower_count']}")
                print(vs)
                compare_b = random.choice(game_data.data)
                print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']} with {compare_b['follower_count']}")
                guess_flag = True
                
            else:
                guess_flag = False
                print(f"Sorry, that's wrong. Final score: {count}")

