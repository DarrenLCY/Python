def count_phasedout_3_missing_cards(my_hand):
        """
        This function takes the hand of the player and sorts it to suit the 
        cards that are needed for phase 3. If the hand already contains cards 
        that can be phased out for phase 3, then the result will be the 2 lists
        of the phased out cards, in a list. Else, this function returns 
        the best cards that can be formed out of the hand for phase 3, in a 
        tuple. This distinction will help to differentiate whether a complete 
        and valid phase 3 can be formed out of the hand or not, to be used 
        later in the game
        
        The tuple is of the form ([[number of cards having value1, value1],
        [number of cards having value2, value2]], number of missing cards 
        needed to complete the phase)
        """
                   
        result = []
        aces = 0
        aces_v2 = 0
        hand_copy = my_hand.copy()
        
        #Not many comments inserted for phase 3, because it is almost the same
        #as for phase 1
        phase_3_dd = defaultdict(int)
        for card in hand_copy:         
            if card[0] != 'A' and card != 'ZZ':
                phase_3_dd[card[0]] += 1
            elif card != 'ZZ':
                aces += 1
                aces_v2 += 1
            
        phase_3_dd_v2 = sorted([(v, score_dict[k]) for (k, v) in 
                                phase_3_dd.items()], reverse=True) 
        
        #Having 2 lists of cards of the same values, without any aces 
        if phase_3_dd_v2[0][0] >= 4 and phase_3_dd_v2[1][0] >= 4:         
            for tup in phase_3_dd_v2[0:2]:
                result.append([])
                count = 4
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
            for tup in phase_3_dd_v2[0:2]:
                if tup[0] == 2:
                    aces -= 2
                    max_aces = 2
                elif tup[0] == 3:
                    aces -= 1
                    max_aces = 1
                else:
                    max_aces = 0

                if aces < 0:
                    out = [[tup[0], score_dict_reverse[tup[1]]] for tup 
                           in phase_3_dd_v2[0:2]]
                    
                    number_of_missing_cards = 0
                    for lst in out:
                        if lst[0] == 1:
                            number_of_missing_cards += 3
                        if lst[0] == 2:
                            number_of_missing_cards += 2
                        if lst[0] == 3:
                            number_of_missing_cards += 1
                
                    return ([[tup[0], score_dict_reverse[tup[1]]] for tup 
                             in phase_3_dd_v2[0:2]], 
                            8 - number_of_missing_cards - aces_v2)   
        

                result.append([])
                count = 4
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
                    if len(lst) < 4:
                        out = [[tup[0], score_dict_reverse[tup[1]]] for tup 
                               in phase_3_dd_v2[0:2]]

                        number_of_missing_cards = 0
                        for lst in out:
                            if lst[0] == 1:
                                number_of_missing_cards += 3
                            if lst[0] == 2:
                                number_of_missing_cards += 2
                            if lst[0] == 3:
                                number_of_missing_cards += 1

                        return ([[tup[0], score_dict_reverse[tup[1]]] for tup 
                                 in phase_3_dd_v2[0:2]], 
                                8 - number_of_missing_cards - aces_v2)
            return result