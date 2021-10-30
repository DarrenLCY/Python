def count_phasedout_4_missing_cards(my_hand):
    """
    This function takes the hand of the player and sorts it to suit the 
    cards that are needed for phase 4. If the hand already contains cards 
    that can be phased out for phase 4, then the result will be the list
    of the phased out cards, in a list. Else, this function returns 
    the best cards that can be formed out of the hand for phase 4, in a 
    tuple. This distinction will help to differentiate whether a complete 
    and valid phase 4 can be formed out of the hand or not, to be used 
    later in the game
    
    The tuple is of the form ([values for the chosen best run which we already
    have], [values for the chosen best run which are still needed], number of 
    missing cards needed to complete the phase)
    """
    
    #The codes below helps to determine the best run which is available in the 
    #player's hand, using a dictionary of runs 
    runs = {'run_1': {'2': 0, '3': 0, '4': 0, '5': 0, 
                      '6': 0, '7': 0, '8': 0, '9': 0},
            'run_2': {'3': 0, '4': 0, '5': 0, '6': 0, 
                      '7': 0, '8': 0, '9': 0, '0': 0},
            'run_3': {'4': 0, '5': 0, '6': 0, '7': 0, 
                      '8': 0, '9': 0, '0': 0, 'J': 0},
            'run_4': {'5': 0, '6': 0, '7': 0, '8': 0, 
                      '9': 0, '0': 0, 'J': 0, 'Q': 0},
            'run_5': {'6': 0, '7': 0, '8': 0, '9': 0, 
                      '0': 0, 'J': 0, 'Q': 0, 'K': 0}}
    
    aces = 0
    hand_copy = my_hand.copy()
    
    for card in hand_copy:
        if card[0] == 'A':
            aces += 1
    
               
    for card in hand_copy:
        if card[0] != 'A' and card != 'ZZ':

            try:
                if runs['run_1'][card[0]] == 0:
                    runs['run_1'][card[0]] += 1              
            except:
                pass 
        
            try:
                if runs['run_2'][card[0]] == 0:
                    runs['run_2'][card[0]] += 1
            except:
                pass 
        
            try:
                if runs['run_3'][card[0]] == 0:
                    runs['run_3'][card[0]] += 1
            except:
                pass 
        
            try:
                if runs['run_4'][card[0]] == 0:
                    runs['run_4'][card[0]] += 1
            except:
                pass 
        
            try:
                if runs['run_5'][card[0]] == 0:
                    runs['run_5'][card[0]] += 1
            except:
                pass
           
    list_of_dict = []
    for dictionary in runs.values():
        list_of_dict.append(dictionary.items())

    totals = []
    for run in runs.values():
        totals.append(0)
        for value in run.values():
            totals[-1] += value           
    max_val = 0
    for number in totals:
        if number > max_val:
            max_val = number
    
    #Having a run of 8 cards without any aces... 
    result = [[]]       
    if max_val == 8:
        run_required = list_of_dict[totals.index(8)]        
        for value_required in run_required:
            for card in hand_copy:
                if card[0] == value_required[0]:
                    hand_copy.remove(card)
                    result[-1].append(card)
                    break
        return result 
    
    #Having a run of 8 cards with aces...    
    elif max_val + aces >= 8: 
        run_required = list_of_dict[totals.index(max_val)]
        
        run_required_v2 = []
        for tup in run_required:
            run_required_v2.append(list(tup)) 
        for value_required in run_required_v2:
            for card in hand_copy:
                if card[0] == value_required[0] and value_required[1] == 1:
                    value_required[1] -= 1
                    hand_copy.remove(card)
                    result[-1].append(card)
                    break
                elif card[0] == 'A' and value_required[1] == 0:
                    value_required[1] -= 1
                    hand_copy.remove(card)
                    result[-1].append(card) 
                    break
        return result 
    
    #Else, if we can't make any run, we return a tuple as mentioned above 
    index = -1    
    for number in totals: 
        index += 1
        if number == max_val:
            return ([(k) for (k, v) in list_of_dict[index] if v == 1],  
                    [(k) for (k, v) in list_of_dict[index] if v == 0], 
                    len([(k) for (k, v) in list_of_dict[index] if v == 0]))