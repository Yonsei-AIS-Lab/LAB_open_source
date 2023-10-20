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

    def add_ticket(self, seat, price):
        if len(self.tickets) < self.max_capacity:
            ticket = Ticket(self, seat, price)
            self.tickets.append(ticket)
            return ticket
        else:
            return None

class TicketingSystem:
    def __init__(self):
        self.matches = []

    def create_match(self, date, home_team, away_team, stadium, max_capacity):
        match = Match(date, home_team, away_team, stadium, max_capacity)
        self.matches.append(match)
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
                print(f"Match: {match.home_team} vs {match.away_team}, Seat: {ticket.seat}, Price: ${ticket.price}")
        else:
            print("No available tickets for this match.")

    def display_matchs(self):
        count = 1
        for match in self.matches:
            print(f"{count}. Match: {match.home_team} vs {match.away_team}, Stadium: {match.stadium}")
            count += 1
        return 
    
def main():
    ticketing_system = TicketingSystem()

    while True:
        print("\nTicketing System Menu:")
        print("1. Create Match")
        print("2. Display Available Tickets")
        print("3. Reserve Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter match date: ")
            home_team = input("Enter home team: ")
            away_team = input("Enter away team: ")
            stadium = input("Enter stadium: ")
            max_capacity = int(input("Enter max capacity: "))
            match = ticketing_system.create_match(date, home_team, away_team, stadium, max_capacity)
            print(f"Match created: {match.home_team} vs {match.away_team}")
        elif choice == "2":
            ticketing_system.display_matchs()
            match_index = int(input("Enter match index: ")) - 1
            if 0 <= match_index < len(ticketing_system.matches):
                match = ticketing_system.matches[match_index]
                ticketing_system.display_available_tickets(match)
            else:
                print("Invalid match index.")
        elif choice == "3":
            ticketing_system.display_matchs()
            match_index = int(input("Enter match index: ")) - 1
            if 0 <= match_index < len(ticketing_system.matches):
                match = ticketing_system.matches[match_index]
                seat = input("Enter seat number: ")
                reserved_ticket = ticketing_system.reserve_ticket(match, seat)
                if reserved_ticket:
                    print(f"Reserved Ticket: Match: {reserved_ticket.match.home_team} vs {reserved_ticket.match.away_team}, Seat: {reserved_ticket.seat}")
                else:
                    print("Ticket is not available or already reserved.")
            else:
                print("Invalid match index.")
        elif choice == "4":
            print("Exiting Ticketing System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
