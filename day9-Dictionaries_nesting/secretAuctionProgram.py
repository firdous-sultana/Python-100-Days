import os
clear = lambda: os.system('cls')

from art import logo
print(logo)

choice = True
auction_data = {}

def find_highest_bidder(bidding_record):
	# bidding_record is the dictionary passed
	highest_bid = 0
	for bidder in bidding_record:
		if(highest_bid < bidding_record[bidder]):
			winner = bidder
			highest_bid = bidding_record[bidder]
			
	print(bidder + " has the highest bid of {}".format(highest_bid))

while choice:
	name = input("What is your name? ")
	bid = int(input("What is your bid? $"))
	auction_data[name] = bid
	continue_ = input("Enter 'yes' if you want to continue, else enter 'no'")
	if continue_ == 'no':
		find_highest_bidder(auction_data)
		choice = False

	else:
		clear()

