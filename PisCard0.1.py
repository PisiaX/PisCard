import random

class PisCardGame:
    def __init__(self):
        self.player_name = "\033[91mPisPro\033[0m"  # Rot
        self.bot_name = "\033[94mPisCard Bot\033[0m"  # Blau
        self.player_score = 0
        self.bot_score = 0
        self.stacks = {"Stack 1": 10, "Stack 2": 10, "Stack 3": 10}

    def draw_card(self, stack_name, player):
        if self.stacks[stack_name] <= 0:
            print("Dieser Stapel ist leer.")
            return 0
        else:
            card_value = random.randint(-3, 3)
            if player == "bot":
                print(f"{self.bot_name} hat eine Karte im Stapel {stack_name} gezogen. Wert: {card_value}")
            else:
                print(f"{self.player_name} hat eine Karte im Stapel {stack_name} gezogen. Wert: {card_value}")
            self.stacks[stack_name] -= 1
            return card_value

    def bot_turn(self):
        stack_name = random.choice(list(self.stacks.keys()))
        card_value = self.draw_card(stack_name, "bot")
        self.bot_score += card_value
        print(f"{self.bot_name} hat {card_value} Punkte bekommen.")

    def play(self):
        print("Willkommen zu PisCard!")
        while True:
            print(f"\nAktueller Stand: {self.player_name}: {self.player_score} | {self.bot_name}: {self.bot_score}")
            for stack, cards_left in self.stacks.items():
                print(f"{stack}: {cards_left} Karten verbleibend")

            player_choice = input("Welchen Stapel möchtest du eine Karte ziehen (stack *, Stack *, oder nur die Zahl * - 1, 2, 3)? Oder 'quit' zum Beenden: ")
            if player_choice.lower() == 'quit':
                print("Das Spiel wurde beendet.")
                break
            
            stack_name = None
            if player_choice.lower().startswith('stack'):
                stack_name = player_choice.capitalize()
            elif player_choice.isdigit() and 1 <= int(player_choice) <= 3:
                stack_name = f"Stack {player_choice}"
            else:
                print("Ungültige Eingabe. Bitte wähle einen der Stapel (stack *, Stack *, oder nur die Zahl - 1, 2, 3).")
                continue

            card_value = self.draw_card(stack_name, "player")
            self.player_score += card_value
            print(f"{self.player_name} hat {card_value} Punkte bekommen.")
                
            if self.player_score >= 30:
                print(f"Herzlichen Glückwunsch! {self.player_name} hat gewonnen!")
                break
                
            self.bot_turn()
                
            if self.bot_score >= 30:
                print(f"Schade! {self.bot_name} hat gewonnen!")
                break


if __name__ == "__main__":
    game = PisCardGame()
    game.play()
