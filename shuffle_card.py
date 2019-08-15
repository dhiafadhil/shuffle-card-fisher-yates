import random
from module.gameplay import card_suit

class FisherYates:

    def suffle(card):
        random.shuffle(card)
        len_card = len(card)
        len_cut = len_card - 1
        for i in range(len_cut, 0, -1):
            index = random.randint(0, i)
            if index == i:
                continue
            card[i], card[index] = card[index], card[i]
        return card

    def insert_blank_card(card):
        card_shuffle = card
        card_blank = card_suit.Card()
        card_blank.get_all_cards()
        tmp_index = random.randrange(166, 208)
        card_shuffle.insert(tmp_index, card_blank.get_blank_card())
        return card_shuffle



