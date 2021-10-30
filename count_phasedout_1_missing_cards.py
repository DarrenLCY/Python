from collections import defaultdict

score_dict_reverse = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
                      8: '8', 9: '9', 10: '0', 11: 'J', 12: 'Q', 13: 'K', 
                      25: 'A'}

my_colour = {'C': 'BLACK', 'D': 'RED', 'H': 'RED', 'S': 'BLACK'}

score_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 25}

def count_phasedout_1_missing_cards(my_hand):
        """
        This function takes the hand of the player and sorts it to suit the 
        cards that are needed for phase 1. If the hand already contains cards 
        that can be phased out for phase 1, then the result will be the 2 lists
        of the phased out cards, in a list. Else, this function returns 
        the best cards that can be formed out of the hand for phase 1, in a 
        tuple. This distinction will help to differentiate whether a complete 
        and valid phase 1 can be formed out of the hand or not, to be used 
        later in the game
        
        The tuple is of the form ([[number of cards having value1, value1],
        [number of cards having value2, value2]], number of missing cards 
        needed to complete the phase)
        """
                       
        result = []
        aces = 0 
        aces_v2 = 0
        hand_copy = my_hand.copy()
        
        #phase_1_dd is a default dictionary of the number of each value present
        #in the player's hand at the start of the play
        #aces and aces_v2 are used to count the number of aces 
        phase_1_dd = defaultdict(int)
        for card in hand_copy:         
            if card[0] != 'A' and card != 'ZZ':
                phase_1_dd[card[0]] += 1
            elif card != 'ZZ':
                aces += 1
                aces_v2 += 1
            
        #phase_1_dd_v2 sorts phase_1_dd, according to the number of each value 
        #and according to the value as well. This is because, if there is a tie
        #(for example, we have 2 'KH' and 2 '5S', we would prefer to phase out
        #a list containing kings first, because they have a higher penalty 
        #point than '5'. This is specially the case when we have aces, and we
        #want to combine them with a value to phase out 
        phase_1_dd_v2 = sorted([(v, score_dict[k]) for (k, v) in 
                                phase_1_dd.items()], reverse=True) 
        
        #Having 2 lists of cards of the same values, without any aces 
        if phase_1_dd_v2[0][0] >= 3 and phase_1_dd_v2[1][0] >= 3:         
            for tup in phase_1_dd_v2[0:2]:
                result.append([])
                count = 3
                while count:
                    for card in hand_copy: 
                        if card[0] == score_dict_reverse[tup[1]]:
                            result[-1].append(card)
                            hand_copy.remove(card)                               
                            break
                    count = count - 1                        
            return result
        
        #Having 2 lists of cards of the same values, with aces
        else:
            for tup in phase_1_dd_v2[0:2]:
                if tup[0] == 2:
                    aces -= 1
                    max_aces = 1
                else:
                    max_aces = 0
                
                if aces < 0:
                    out = [[tup[0], score_dict_reverse[tup[1]]] for tup 
                           in phase_1_dd_v2[0:2]]
                    
                    number_of_missing_cards = 0
                    for lst in out:
                        if lst[0] == 1:
                            number_of_missing_cards += 3
                        if lst[0] == 2:
                            number_of_missing_cards += 2
                
                    return ([[tup[0], score_dict_reverse[tup[1]]] for tup 
                             in phase_1_dd_v2[0:2]], 
                            8 - number_of_missing_cards - aces_v2)
                    
                result.append([])
                count = 3
                while count:
                    for card in hand_copy: 
                        if card[0] == score_dict_reverse[tup[1]]:
                            result[-1].append(card)
                            hand_copy.remove(card)                               
                            break
                        elif card[0] == 'A' and max_aces != 0:
                            result[-1].append(card)
                            hand_copy.remove(card)
                            max_aces -= 1
                            break
                    count = count - 1 
                for lst in result:
                    if len(lst) < 3:
                        out = [[tup[0], score_dict_reverse[tup[1]]] for tup 
                               in phase_1_dd_v2[0:2]]

                        number_of_missing_cards = 0
                        for lst in out:
                            if lst[0] == 1:
                                number_of_missing_cards += 3
                            if lst[0] == 2:
                                number_of_missing_cards += 2

                        return ([[tup[0], score_dict_reverse[tup[1]]] for tup 
                                 in phase_1_dd_v2[0:2]], 
                                6 - number_of_missing_cards - aces_v2)
            return result
                         