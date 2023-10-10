import random

class Blackjack:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.initialize_deck()
        self.shuffle_deck()

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.deck.append(f"{rank} of {suit}")

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_hand_value(self, hand):
        value = 0
        num_aces = 0
        
        # 문자열 랭크를 정수 값으로 매핑
        rank_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
                   'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
                   'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
        for card in hand:
            rank = card.split()[0]
            value += rank_values[rank] # 딕셔너리를 사용하여 값을 가져옴
            
            if rank == 'Ace':
                num_aces += 1

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value

    def display_game_status(self, reveal_dealer=False):
        print("\n--- 블랙잭 게임 ---")
        print("플레이어의 카드:", self.player_hand)
        if reveal_dealer:
            print("딜러의 카드:", self.dealer_hand)
        else:
            print("딜러의 첫 번째 카드:", [self.dealer_hand[0], "???"])

    def play(self):
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        while True:
            self.display_game_status()
            choice = input("카드를 더 받으려면 'hit'을 입력하세요. 그만 받으려면 'stand'을 입력하세요: ").lower()

            if choice == 'hit':
                self.deal_card(self.player_hand)
                if self.calculate_hand_value(self.player_hand) > 21:
                    self.display_game_status()
                    print("플레이어가 21을 초과했습니다. 딜러 승!")
                    break
            elif choice == 'stand':
                while self.calculate_hand_value(self.dealer_hand) < 17:
                    self.deal_card(self.dealer_hand)

                self.display_game_status(reveal_dealer=True)

                player_value = self.calculate_hand_value(self.player_hand)
                dealer_value = self.calculate_hand_value(self.dealer_hand)

                if dealer_value > 21:
                    print("딜러가 21을 초과했습니다. 플레이어 승!")
                elif player_value > dealer_value:
                    print("플레이어 승!")
                elif player_value < dealer_value:
                    print("딜러 승!")
                else:
                    print("무승부!")
                break

def main():
    blackjack = Blackjack()
    
    while True:
        blackjack.play()
        again = input("게임을 다시 하려면 'yes'를 입력하세요. 그만 하려면 'no'를 입력하세요: ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
