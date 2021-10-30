def count_phasedout_5_missing_cards(my_hand):
    """
    This function takes the hand of the player and sorts it to suit the 
    cards that are needed for phase 5. If the hand already contains cards 
    that can be phased out for phase 5, then the result will be the 2 lists
    of the phased out cards, in a list. Else, this function returns 
    the best cards that can be formed out of the hand for phase 5, in a 
    tuple. This distinction will help to differentiate whether a complete 
    and valid phase 5 can be formed out of the hand or not, to be used 
    later in the game
    
    The tuples for phase 5 are of 3 distinct forms, depend on which cards are
    needed, and which cards we already have:
    
    Form 1, where we have the run of cards, but we still miss the list of cards
    of the same value:
    ([[[best run of cards which we already have]], [[value1, number of cards 
    being value1, 'RED/BLACK']]], number of missing cards needed to complete 
    the phase)
    
    Form 2, where we have neither the run of cards, not the list of cards of 
    the same value:
    ([[best run of cards which we already have], [colour of the run, missing
    values to complete the run], [value1, number of cards which we already have
    for value1]], number of missing cards needed to complete the phase)
    
    Form 3, where we don't have the run of cards, but we have the list of cards
    of the same value:
    ([[best run of cards which we already have], [colour of the run, missing
    values to complete the run], [cards which are of the same value]], 
    number of missing cards needed to complete the phase) 
    """
    
    #The codes below helps to determine the best run which is available in the 
    #player's hand, using a dictionary of runs, for runs of red, and runs of 
    #black
    runs_of_red = {'run_1': {'2': 0, '3': 0, '4': 0, '5': 0},
                   'run_2': {'3': 0, '4': 0, '5': 0, '6': 0},
                   'run_3': {'4': 0, '5': 0, '6': 0, '7': 0},
                   'run_4': {'5': 0, '6': 0, '7': 0, '8': 0},
                   'run_5': {'6': 0, '7': 0, '8': 0, '9': 0},
                   'run_6': {'7': 0, '8': 0, '9': 0, '0': 0},
                   'run_7': {'8': 0, '9': 0, '0': 0, 'J': 0},
                   'run_8': {'9': 0, '0': 0, 'J': 0, 'Q': 0},
                   'run_9': {'0': 0, 'J': 0, 'Q': 0, 'K': 0}}
    
    runs_of_black = {'run_1': {'2': 0, '3': 0, '4': 0, '5': 0},
                     'run_2': {'3': 0, '4': 0, '5': 0, '6': 0},
                     'run_3': {'4': 0, '5': 0, '6': 0, '7': 0},
                     'run_4': {'5': 0, '6': 0, '7': 0, '8': 0},
                     'run_5': {'6': 0, '7': 0, '8': 0, '9': 0},
                     'run_6': {'7': 0, '8': 0, '9': 0, '0': 0},
                     'run_7': {'8': 0, '9': 0, '0': 0, 'J': 0},
                     'run_8': {'9': 0, '0': 0, 'J': 0, 'Q': 0},
                     'run_9': {'0': 0, 'J': 0, 'Q': 0, 'K': 0}}
    
    aces = 0
    result = []
    hand_copy = my_hand.copy()
    red_run = False
    black_run = False
    
    for card in hand_copy:
        if card[0] == 'A':
            aces += 1
    
    for card in hand_copy:
        if card != 'ZZ':
            if card[0] != 'A' and my_colour[card[1]] == 'RED':

                try:
                    if runs_of_red['run_1'][card[0]] == 0:
                        runs_of_red['run_1'][card[0]] += 1              
                except:
                    pass 

                try:
                    if runs_of_red['run_2'][card[0]] == 0:
                        runs_of_red['run_2'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_red['run_3'][card[0]] == 0:
                        runs_of_red['run_3'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_red['run_4'][card[0]] == 0:
                        runs_of_red['run_4'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_red['run_5'][card[0]] == 0:
                        runs_of_red['run_5'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_red['run_6'][card[0]] == 0:
                        runs_of_red['run_6'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_red['run_7'][card[0]] == 0:
                        runs_of_red['run_7'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_red['run_8'][card[0]] == 0:
                        runs_of_red['run_8'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_red['run_9'][card[0]] == 0:
                        runs_of_red['run_9'][card[0]] += 1
                except:
                    pass
            
    for card in hand_copy:
        if card != 'ZZ':
            if card[0] != 'A' and my_colour[card[1]] == 'BLACK':

                try:
                    if runs_of_black['run_1'][card[0]] == 0:
                        runs_of_black['run_1'][card[0]] += 1              
                except:
                    pass 

                try:
                    if runs_of_black['run_2'][card[0]] == 0:
                        runs_of_black['run_2'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_black['run_3'][card[0]] == 0:
                        runs_of_black['run_3'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_black['run_4'][card[0]] == 0:
                        runs_of_black['run_4'][card[0]] += 1
                except:
                    pass 

                try:
                    if runs_of_black['run_5'][card[0]] == 0:
                        runs_of_black['run_5'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_black['run_6'][card[0]] == 0:
                        runs_of_black['run_6'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_black['run_7'][card[0]] == 0:
                        runs_of_black['run_7'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_black['run_8'][card[0]] == 0:
                        runs_of_black['run_8'][card[0]] += 1
                except:
                    pass

                try:
                    if runs_of_black['run_9'][card[0]] == 0:
                        runs_of_black['run_9'][card[0]] += 1
                except:
                    pass
           
           
    list_of_dict_red = []
    for dictionary in runs_of_red.values():
        list_of_dict_red.append(dictionary.items())
        
    list_of_dict_black = []
    for dictionary in runs_of_black.values():
        list_of_dict_black.append(dictionary.items())
        
    totals_red = []
    for lst in list_of_dict_red:
        totals_red.append([0, lst, 'RED'])
        for tup in lst:
            totals_red[-1][0] += tup[1]
    
    max_val_red = 0
    for lst in totals_red:
        if lst[0] > max_val_red:
            max_val_red = lst[0]
    if max_val_red == 4:
        red_run = True
    elif max_val_red + aces >= 4:
        red_run = True
               

    totals_black = []
    for lst in list_of_dict_black:
        totals_black.append([0, lst, 'BLACK'])
        for tup in lst:
            totals_black[-1][0] += tup[1]
    
    max_val_black = 0
    for lst in totals_black:
        if lst[0] > max_val_black:
            max_val_black = lst[0]
    if max_val_black == 4:
        black_run = True
    elif max_val_black + aces >= 4:
        black_run = True
     
    out_red = []
    for lst in totals_red: 
        if lst[0] == max_val_red:
            out_red.append([[(k) for (k, v) in lst[1] if v == 1],
                            [(k) for (k, v) in lst[1] if v == 0], 'RED'])
            break
                                     
    out_black = []
    for lst in totals_black: 
        if lst[0] == max_val_black:
            out_black.append([[(k) for (k, v) in lst[1] if v == 1],
                              [(k) for (k, v) in lst[1] if v == 0], 'BLACK'])
            break
     
    #For the situation where you have a run of red cards
    if red_run and max_val_red >= max_val_black:
        for lst in totals_red:
            if lst[0] == max_val_red:
                result.append([])
                for tup in lst[1]:
                    for card in hand_copy:
                        if (card[0] == tup[0] and 
                            my_colour[card[1]] == lst[2] and 
                                tup[1] == 1):
                            hand_copy.remove(card)
                            result[-1].append(card)
                            break
                        elif card[0] == 'A' and tup[1] == 0:
                            hand_copy.remove(card)
                            result[-1].append(card)
                            break
                break
        
        #The codes below are for the list of cards of the same value 
        phase_5_dd = defaultdict(int)
        aces_v2 = 0 
        for card in hand_copy:         
            if card[0] != 'A' and card != 'ZZ':
                phase_5_dd[card[0]] += 1
            elif card != 'ZZ':
                aces_v2 += 1

    
        phase_5_dd_v2 = sorted([(v, k) for (k, v) in 
                                phase_5_dd.items()], reverse=True)      
        
        phase_5_dd_v3 = []
        for tup in phase_5_dd_v2:
            phase_5_dd_v3.append([tup[1], tup[0]])
                
        for lst in phase_5_dd_v3[0:1]:
            
            #If we have a list of 4 cards of the same value... 
            if lst[1] >= 2:
                
                if lst[1] == 2:
                    max_ace = 2              
                if lst[1] == 3:
                    max_ace = 1 
                if lst[1] >= 4:
                    max_ace = 0 
                    
                if lst[1] >= 4 or lst[1] + aces_v2 >= 4:
                    result.append([])
                    count = 4
                    while count:
                        for card in hand_copy:
                            if card[0] == lst[0]:
                                hand_copy.remove(card)
                                result[-1].append(card)
                                break
                            elif (card[0] == 'A' and 
                                  aces_v2 != 0 and 
                                  max_ace != 0):
                                hand_copy.remove(card)
                                result[-1].append(card)
                                max_ace -= 1
                                break
                        count -= 1                        
                    return result
                
            #Else, if we don't have a list of 4 cards of the same value, a 
            #tuple is returned, as mentioned above 
            out = [[lst[0], lst[1], 'RED/BLACK']for lst 
                   in phase_5_dd_v3[0:1]] 
            number_of_missing_cards = 0
            number_of_missing_cards += (4 - out[0][1])
            return [result, [[lst[0], lst[1], 'RED/BLACK']for lst in 
                    phase_5_dd_v3[0:1]]], number_of_missing_cards - aces_v2
                                             
    #For the situation where you have a run of black cards
    elif black_run and max_val_black > max_val_red:
        for lst in totals_black:
            if lst[0] == max_val_black:
                result.append([])
                for tup in lst[1]:
                    for card in hand_copy:
                        if (card[0] == tup[0] and 
                            my_colour[card[1]] == lst[2] and
                                tup[1] == 1):
                            hand_copy.remove(card)
                            result[-1].append(card)
                            break
                        elif card[0] == 'A' and tup[1] == 0:
                            hand_copy.remove(card)
                            result[-1].append(card)
                            break
                break
        
        #The codes below are for the list of cards of the same value 
        phase_5_dd = defaultdict(int)
        aces_v2 = 0 
        for card in hand_copy:         
            if card[0] != 'A' and card != 'ZZ':
                phase_5_dd[card[0]] += 1
            elif card != 'ZZ':
                aces_v2 += 1
  
    
        phase_5_dd_v2 = sorted([(v, k) for (k, v) in 
                                phase_5_dd.items()], reverse=True)      
        
        phase_5_dd_v3 = []
        for tup in phase_5_dd_v2:
            phase_5_dd_v3.append([tup[1], tup[0]])
      
        for lst in phase_5_dd_v3[0:1]:
            
            #If we have a list of 4 cards of the same value...
            if lst[1] >= 2:
                
                if lst[1] == 2:
                    max_ace = 2
                if lst[1] == 3:
                    max_ace = 1
                if lst[1] >= 4:
                    max_ace = 0
                    
                if lst[1] >= 4 or lst[1] + aces_v2 >= 4:                 
                    result.append([])
                    count = 4
                    while count:
                        for card in hand_copy:
                            if card[0] == lst[0]:
                                hand_copy.remove(card)
                                result[-1].append(card)
                                break
                            elif (card[0] == 'A' and 
                                  aces_v2 != 0 and 
                                  max_ace != 0):
                                hand_copy.remove(card)
                                result[-1].append(card)
                                max_ace -= 1
                                break
                        count -= 1
                    return result
                
            #Else, if we don't have a list of 4 cards of the same value, a 
            #tuple is returned, as mentioned above
            out = [[lst[0], lst[1], 'RED/BLACK']for lst 
                   in phase_5_dd_v3[0:1]] 
            number_of_missing_cards = 0
            number_of_missing_cards += (4 - out[0][1])
            return [result, [[lst[0], lst[1], 'RED/BLACK']for lst 
                    in phase_5_dd_v3[0:1]]], number_of_missing_cards - aces_v2

            
    
    else:
        #For the situation where we don't have any completed runs of cards,
        #we can still have a list of 4 cards of the same value, or not 
        best_run_of_card = []
        
        #We choose the best hand based on whether the run of red cards is 
        #better than the run of black cards, or vice versa 
        if max_val_red >= max_val_black:                 
            for lst in totals_red:
                if lst[0] == max_val_red:
                    best_run_of_card.append([])
                    best_run_of_card.append(['RED'])                       
                    for tup in lst[1]:
                        if tup[1] == 0:
                            best_run_of_card[-1].append(tup[0])
                            
                            
                        for card in hand_copy:
                            if (card[0] == tup[0] and 
                                my_colour[card[1]] == lst[2] and 
                                    tup[1] == 1):
                                hand_copy.remove(card)
                                best_run_of_card[-2].append(card)
                                break
                            elif card[0] == 'A' and tup[1] == 0:
                                hand_copy.remove(card)
                                best_run_of_card[-2].append(card)
                                break
                    break
                    
            #Based on the remaining cards in hands, we then try to form the 
            #second list 
            phase_5_dd = defaultdict(int)
            for card in hand_copy:         
                if card[0] != 'A' and card != 'ZZ':
                    phase_5_dd[card[0]] += 1

            phase_5_dd_v2 = sorted([(v, k) for (k, v) in 
                                    phase_5_dd.items()], reverse=True)      

            phase_5_dd_v3 = []
            for tup in phase_5_dd_v2:
                phase_5_dd_v3.append([tup[1], tup[0]])

            for lst in phase_5_dd_v3[0:1]:
                
                #Here, we have a list of 4 cards of the same value 
                if lst[1] >= 4:
                    best_run_of_card.append([])
                    count = 4
                    while count:
                        for card in hand_copy:
                            if card[0] == lst[0]:
                                hand_copy.remove(card)
                                best_run_of_card[-1].append(card)
                                break
                        count -= 1
                    return best_run_of_card, 4 - len(best_run_of_card[0])
                
                #And here, we don't 
                else:                    
                    best_run_of_card.append(phase_5_dd_v3[0]) 
                    return (best_run_of_card, 8 - 
                            len(best_run_of_card[0]) - 
                            best_run_of_card[2][1])

        #Same situation as above, but for a black run 
        elif max_val_black > max_val_red:
            for lst in totals_black:
                if lst[0] == max_val_black:
                    best_run_of_card.append([])
                    best_run_of_card.append(['BLACK'])                       
                    for tup in lst[1]:
                        if tup[1] == 0:
                            best_run_of_card[-1].append(tup[0])
                                                      
                        for card in hand_copy:
                            if (card[0] == tup[0] and 
                                my_colour[card[1]] == lst[2] and 
                                    tup[1] == 1):
                                hand_copy.remove(card)
                                best_run_of_card[-2].append(card)
                                break
                            elif card[0] == 'A' and tup[1] == 0:
                                hand_copy.remove(card)
                                best_run_of_card[-2].append(card)
                                break
                    break

            phase_5_dd = defaultdict(int)
            for card in hand_copy:         
                if card[0] != 'A' and card != 'ZZ':
                    phase_5_dd[card[0]] += 1

            phase_5_dd_v2 = sorted([(v, k) for (k, v) in 
                                    phase_5_dd.items()], reverse=True)      

            phase_5_dd_v3 = []
            for tup in phase_5_dd_v2:
                phase_5_dd_v3.append([tup[1], tup[0]])

            for lst in phase_5_dd_v3[0:1]:
                if lst[1] >= 4:
                    best_run_of_card.append([])
                    count = 4
                    while count:
                        for card in hand_copy:
                            if card[0] == lst[0]:
                                hand_copy.remove(card)
                                best_run_of_card[-1].append(card)
                                break
                        count -= 1
                    return best_run_of_card, 4 - len(best_run_of_card[0]) 
                            
                else:                    
                    best_run_of_card.append(phase_5_dd_v3[0]) 
                    return (best_run_of_card, 
                            8 - len(best_run_of_card[0]) - 
                            best_run_of_card[2][1])      
          