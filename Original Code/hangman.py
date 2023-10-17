import random

class HangmanGame:
    def __init__(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = []

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def play(self):
        print("행맨 게임에 오신 것을 환영합니다!")
        print("맞춰야 할 단어를 생각하고 시작합니다.")

        while self.guesses_left > 0:
            print(f"\n현재 단어: {self.display_word()}")
            guess = input("알파벳 하나를 추측하세요: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("올바른 알파벳을 입력하세요.")
                continue

            if guess in self.guessed_letters:
                print("이미 추측한 알파벳입니다.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.secret_word:
                print("맞았습니다! 추측한 알파벳이 단어에 포함되어 있습니다.")
                if self.display_word() == self.secret_word:
                    print(f"축하합니다! 정답을 맞추었습니다. 단어는 '{self.secret_word}'입니다!")
                    break
            else:
                self.guesses_left -= 1
                print(f"틀렸습니다. {self.guesses_left}번의 시도 기회가 남았습니다.")

        if self.guesses_left == 0:
            print(f"게임 종료. 시도 기회가 모두 소진되었습니다. 정답은 '{self.secret_word}'입니다.")

def main():
    while True: # 게임을 반복할 수 있도록 무한 루프 사용
        game = HangmanGame()
        game.play()
        
        #게임이 끝난 후 게임 재시작 여부 확인
        play_again = input("다시 게임을 하시겠습니까? (y/n): ").lower()
        if play_again != "y":
            print("게임을 종료합니다.")
            break # 사용자가  y가 아닌 다른 값을 입력하면 무한 루프 종료

if __name__ == "__main__":
    main()
