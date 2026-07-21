"""Implement a CardHand class that supports a person arranging a group of cards
in his or her hand. The simulator should represent the sequence of cards using
a single positional list ADT so that cards of the same suit are kept together.
Implement this strategy by means of four “fingers” into the hand, one for each
of the suits of hearts, clubs, spades, and diamonds, so that adding a new card
to the person's hand or playing a correct card from the hand can be done in
constant time.

The class should support the following methods:
	● add_card(r, s): Add a new card with rank r and suit s to the hand.
	● play(s): Remove and return a card of suit s from the player's hand; if there
		is no card of suit s, then remove and return an arbitrary card from the hand.
	● __iter__(): Iterate through all cards currently in the hand.
	● all_of_suit(s): Iterate through all cards of suit s that are currently in the
		hand.
"""


class CardHand:
    def __init__(self):
        self._hand = []
        self._fingers = {'hearts': 0, 'clubs': 0, 'spades': 0, 'diamonds': 0}

    def add_card(self, rank, suit):
        self._hand.append((rank, suit))
        self._fingers[suit] += 1

    def play(self, suit):
        if self._fingers[suit] > 0:
            for i, (r, s) in enumerate(self._hand):
                if s == suit:
                    self._fingers[suit] -= 1
                    return self._hand.pop(i)
        return self._hand.pop()

    def __iter__(self):
        return iter(self._hand)

    def all_of_suit(self, suit):
        return (card for card in self._hand if card[1] == suit)
    

if __name__ == "__main__":
    hand = CardHand()
    hand.add_card('A', 'hearts')
    hand.add_card('K', 'hearts')
    hand.add_card('Q', 'clubs')
    hand.add_card('J', 'spades')
    hand.add_card('10', 'diamonds')

    print("All cards in hand:")
    for card in hand:
        print(card)

    print("\nAll hearts in hand:")
    for card in hand.all_of_suit('hearts'):
        print(card)

    played_card = hand.play('hearts')
    print(f"\nPlayed card: {played_card}")

    print("\nAll cards in hand after playing a heart:")
    for card in hand:
        print(card)