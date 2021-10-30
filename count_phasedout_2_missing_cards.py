                    
def count_phasedout_2_missing_cards(my_hand):
        """
        This function takes the hand of the player and sorts it to suit the 
        cards that are needed for phase 2. If the hand already contains cards 
        that can be phased out for phase 2, then the result will be the list
        of the phased out cards, in a list. Else, this function returns 
        the best cards that can be formed out of the hand for phase 2, in a 
        tuple. This distinction will help to differentiate whether a complete 
        and valid phase 2 can be formed out of the hand or not, to be used 
        later in the game
        
        The tuple is of the form ((number of cards being suit1, suit1), 
        number of missing cards needed to complete the phase)
        """
                
        result = []
        aces = 0
        hand_copy = my_hand.copy()

        
        #phase_2_dd is a default dictionary of the number of each suit present
        #in the player's hand at the start of the play
        phase_2_dd = defaultdict(int)
        for card in hand_copy:
            if card[0] != 'A' and card != 'ZZ':
                phase_2_dd[card[1]] += 1
            elif card != 'ZZ':
                aces += 1
            
        #phase_2_dd_v2 sorts phase_1_dd, according to the number of each suit 
        phase_2_dd_v2 = sorted([(v, k) for (k, v) in 
                                phase_2_dd.items()], reverse=True) 
                                   
        #Having a list of cards of the same suit, without any aces 
        if phase_2_dd_v2[0][0] >= 7:
            for tup in phase_2_dd_v2[0:1]:
                result.append([])

                count = 7
                while count:
                    for card in hand_copy: 
                        if card[1] == phase_2_dd_v2[0][1] and card[0] != 'A':
                            result[-1].append(card)
                            hand_copy.remove(card)                               
                            break
                    count = count - 1                        
            return result
                                                  
        if phase_2_dd_v2[0][0] + aces >= 7:
            for tup in phase_2_dd_v2[0:1]:
                result.append([])                
                max_aces = 7 - phase_2_dd_v2[0][0] 

                count = 7
                while count:
                    for card in hand_copy: 
                        if card[1] == phase_2_dd_v2[0][1]:
                            result[-1].append(card)
                            hand_copy.remove(card)                               
                            break
                        elif card[0] == 'A' and max_aces != 0:
                            result[-1].append(card)
                            hand_copy.remove(card)
                            max_aces -= 1
                            break
                    count = count - 1                        
            return result
        
        else: 
            return phase_2_dd_v2[0], 7 - phase_2_dd_v2[0][0]       