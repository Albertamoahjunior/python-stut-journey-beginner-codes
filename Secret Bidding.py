person = {}
bids =[]
highest_bidder = ""
more = "yes"

def add_bidder(name,bid):
    person[name] = bid

def highest_bidder():
    highest_bid = 0
    for name in person:
        bids.append(person[name])

    highest_bid = max(bids)

    for name in person:
        if person[name] == highest_bid:
            print(f"The winner is {name} with {highest_bid}$")

while(more == "yes"):
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    more = input("Are there anymore bidders? Type 'yes' or 'no':")


add_bidder(name,bid)
highest_bidder()

