Class Card:
  def__init__(self,rank,suit,isVisible='False'):
    Self.rank = rank
    Self.suit = suit
Class Table:
  Class Deck:
    def shuffle(self):
        n = len(self.cards)
        newcards = []
        for i in randperm(n):
            newcards.append(self.cards[i])
        self.cards = newcards

    def userclickhandler(self):
        opendeck = self.game.opendeck
        card = self.deal()
        if not card:
            while 1:
                card = opendeck.deal()
                if not card:
                    break
                self.add(card)
                card.showback()
        else:
            self.game.opendeck.add(card)
            card.showface()


    def randperm(n):
    """Function returning a random permutation of range(n)."""
    r = range(n)
    x = []
    while r:
        i = random.choice(r)
        x.append(i)
        r.remove(i)
    return x
