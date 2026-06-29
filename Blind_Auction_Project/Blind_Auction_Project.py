import art
print(art.logo)

bid_dictionary = {}

user_count = "yes"
while user_count == "yes":

    # TODO-1: Ask the user for input

    name = input("What is your name?:  ")
    bid = int(input("What is your bid?: €"))

    # TODO-2: Save data into dictionary {name: price}
    bid_dictionary[name] = bid



    #print(bid_dictionary)
    # TODO-3: Whether if new bids need to be added
    user_count = input("Are there other users who want to bid? Type 'yes' or 'no'.").lower()

    if user_count == "yes":
        print("\n" * 20)

    # TODO-4: Compare bids in dictionary
    else:
        highest_bid = 0
        winners = []

        #max(bid_dictionary, key=bid_dictionary.get)

        for bidder in bid_dictionary:
            current_bid = bid_dictionary[bidder]

            if current_bid > highest_bid:
                highest_bid = current_bid
                winners = [bidder]

            elif current_bid == highest_bid:
                winners.append(bidder)



        if len(winners) == 1:
            print(f"The winner is {winners[0]} with a bid of ${highest_bid}.")
        else:
            print(f"It is a tie between {'and '.join(winners)} with a bid of ${highest_bid}.")






