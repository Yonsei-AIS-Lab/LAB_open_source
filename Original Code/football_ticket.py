import random

class Ticket:
    def __init__(self, match, seat, price, is_reserved=False):
        self.match = match
        self.seat = seat
        self.price = price
        self.is_reserved = is_reserved

class Match:
    def __init__(self, date, home_team, away_team, stadium, max_capacity):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.stadium = stadium
        self.max_capacity = max_capacity
        self.tickets = []

    def add_ticket(self, price):
        for i in range(self.max_capacity):
            ticket = Ticket(self, str(i+1), price)
            self.tickets.append(ticket)

class TicketingSystem:
    def __init__(self):
        self.matches = []

    def create_match(self, date, home_team, away_team, stadium, max_capacity, price):
        match = Match(date, home_team, away_team, stadium, max_capacity)
        self.matches.append(match)
        match.add_ticket(price)
        return match

    def reserve_ticket(self, match, seat):
        for ticket in match.tickets:
            if ticket.seat == seat and not ticket.is_reserved:
                ticket.is_reserved = True
                return ticket
        return None

    def display_available_tickets(self, match):
        available_tickets = [ticket for ticket in match.tickets if not ticket.is_reserved]
        if available_tickets:
            for ticket in available_tickets:
                print(f"경기: {match.home_team} vs {match.away_team}, 좌석: {ticket.seat}, 가격: ${ticket.price}")
        else:
            print("이 경기에 대한 사용 가능한 티켓이 없습니다.")

def main():
    ticketing_system = TicketingSystem()

    while True:
        print("\n티켓 예매 시스템 메뉴:")
        print("1. 경기 생성")
        print("2. 사용 가능한 티켓 보기")
        print("3. 티켓 예매")
        print("4. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            date = input("경기 날짜 입력: ")
            home_team = input("홈 팀 입력: ")
            away_team = input("원정 팀 입력: ")
            stadium = input("경기장 입력: ")
            max_capacity = int(input("최대 수용 가능 인원 입력: "))
            price = int(input("Enter ticket price: "))
            match = ticketing_system.create_match(date, home_team, away_team, stadium, max_capacity, price)
            print(f"경기가 생성되었습니다: {match.home_team} vs {match.away_team}")
        elif choice == "2":
            match_index = int(input("경기 인덱스 입력: ")) - 1
            if 0 <= match_index < len(ticketing_system.matches):
                match = ticketing_system.matches[match_index]
                ticketing_system.display_available_tickets(match)
            else:
                print("유효하지 않은 경기 인덱스입니다.")
        elif choice == "3":
            match_index = int(input("경기 인덱스 입력: ")) - 1
            if 0 <= match_index < len(ticketing_system.matches):
                match = ticketing_system.matches[match_index]
                seat = input("좌석 번호 입력: ")
                reserved_ticket = ticketing_system.reserve_ticket(match, seat)
                if reserved_ticket:
                    print(f"예매된 티켓: 경기: {reserved_ticket.match.home_team} vs {reserved_ticket.match.away_team}, 좌석: {reserved_ticket.seat}")
                else:
                    print("티켓을 사용할 수 없거나 이미 예약되었습니다.")
            else:
                print("유효하지 않은 경기 인덱스입니다.")
        elif choice == "4":
            print("티켓 예매 시스템을 종료합니다.")
            break
        else:
            print("유효하지 않은 선택입니다. 유효한 옵션을 선택하세요.")

if __name__ == "__main__":
    main()
