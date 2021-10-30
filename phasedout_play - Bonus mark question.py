     
def phasedout_play(player_id, table, turn_history, phase_status, hand, 
                   discard):
    # Implement this function.
           
    dict_of_next_players = {0: 1, 1: 2, 2: 3, 3: 0}
                                                   
    current_player_phase = phase_status[player_id]
    phase_required = current_player_phase + 1 
            
    
    #For each phase, the player will either choose to draw from the discard 
    #pile or draw from the deck, depending on whether the discard pile contains
    #the card he/she wants (in that case, the player will choose to draw from 
    #the discard pile). This is based on the phase required. 
    #Else, the player draws from the deck. 
      
    if phase_required == 1 and table[player_id][0] is None:
               
        if turn_history != []:
            if (dict_of_next_players[turn_history[-1][0]] == player_id and 
                    turn_history[-1][-1][-1][0] == 5):

                #If an ace is present in the discard pile, the player would 
                #always choose to draw from the discard pile
                if discard[0] == 'A':
                    return (2, discard)
                
                if type(count_phasedout_1_missing_cards(hand)) == list:
                    return (1, None)
                
                for lst in count_phasedout_1_missing_cards(hand)[0]:
                    if discard[0] == lst[1]:
                        return (2, discard)
                    else: 
                        return (1, None)


        elif turn_history == []:
            if discard[0] == 'A':
                return (2, discard)

            if type(count_phasedout_1_missing_cards(hand)) == list:
                return (1, None)

            for lst in count_phasedout_1_missing_cards(hand)[0]:
                if discard[0] == lst[1]:
                    return (2, discard)
                else: 
                    return (1, None)
        
    if phase_required == 2 and table[player_id][0] is None:
        
        if turn_history != []:
            if (dict_of_next_players[turn_history[-1][0]] == player_id and 
                    turn_history[-1][-1][-1][0] == 5):

                if discard[0] == 'A':
                    return (2, discard)

                if type(count_phasedout_2_missing_cards(hand)) == list:
                    return (1, None)

                if discard[1] == count_phasedout_2_missing_cards(hand)[0][1]:
                    return (2, discard)
                else: 
                    return (1, None)
                
        elif turn_history == []:
            
            if discard[0] == 'A':
                return (2, discard)

            if type(count_phasedout_2_missing_cards(hand)) == list:
                return (1, None)

            if discard[1] == count_phasedout_2_missing_cards(hand)[0][1]:
                return (2, discard)
            else: 
                return (1, None)
            
            
    if phase_required == 3 and table[player_id][0] is None:
        
        if turn_history != []:
            if (dict_of_next_players[turn_history[-1][0]] == player_id and 
                    turn_history[-1][-1][-1][0] == 5):

                if discard[0] == 'A':
                    return (2, discard)
                
                if type(count_phasedout_3_missing_cards(hand)) == list:
                    return (1, None)
                
                for lst in count_phasedout_3_missing_cards(hand)[0]:
                    if discard[0] == lst[1]:
                        return (2, discard)
                    else: 
                        return (1, None)


        elif turn_history == []:
            if discard[0] == 'A':
                return (2, discard)

            if type(count_phasedout_3_missing_cards(hand)) == list:
                return (1, None)

            for lst in count_phasedout_3_missing_cards(hand)[0]:
                if discard[0] == lst[1]:
                    return (2, discard)
                else: 
                    return (1, None)
            
    if phase_required == 4 and table[player_id][0] is None:
        
        if turn_history != []:
            if (dict_of_next_players[turn_history[-1][0]] == player_id and 
                    turn_history[-1][-1][-1][0] == 5):

                if discard[0] == 'A':
                    return (2, discard)
                
                if type(count_phasedout_4_missing_cards(hand)) == list:
                    return (1, None)
                
                for value in count_phasedout_4_missing_cards(hand)[1]:
                    if discard[0] == value:
                        return (2, discard)         
                return (1, None)


        elif turn_history == []:
            if discard[0] == 'A':
                return (2, discard)

            if type(count_phasedout_4_missing_cards(hand)) == list:
                return (1, None)

            for value in count_phasedout_4_missing_cards(hand)[1]:
                if discard[0] == value:
                    return (2, discard)         
            return (1, None)
            
    if phase_required == 5 and table[player_id][0] is None:
        
        if turn_history != []:
            if (dict_of_next_players[turn_history[-1][0]] == player_id and 
                    turn_history[-1][-1][-1][0] == 5):

                if discard[0] == 'A':
                    return (2, discard)
                
                if type(count_phasedout_5_missing_cards(hand)) == list:
                    return (1, None)
                
                #For the situation where for phase 5, we miss only cards in the
                #list of cards of the same value... 
                if len(count_phasedout_5_missing_cards(hand)[0]) == 2:
                    if (discard[0] == 
                            count_phasedout_5_missing_cards(hand)[0][1][0][0]):
                        return (2, discard)
                    else:
                        return (1, None)
                    
                #For the situation where for phase 5, we miss the cards in the
                #list of cards of the same value, or the run, or both     
                elif len(count_phasedout_5_missing_cards(hand)[0]) == 3:
                    values_missing_for_run = [] 
                    for value in count_phasedout_5_missing_cards(hand
                                                                 )[0][1][1:]:
                        values_missing_for_run.append(value)
                    if (discard[0] in values_missing_for_run and 
                        my_colour[discard[1]] == 
                            count_phasedout_5_missing_cards(hand)[0][1][0]):
                        return (2, discard)
                    
                    #To check if we miss cards of the same value... 
                    if len(count_phasedout_5_missing_cards(hand)[0][2]) == 2:
                        if (discard[0] == 
                                count_phasedout_5_missing_cards(hand
                                                                )[0][2][0]):
                            return (2, discard)
                   
                    return (1, None)
                    


        elif turn_history == []:

            if discard[0] == 'A':
                return (2, discard)

            if type(count_phasedout_5_missing_cards(hand)) == list:
                return (1, None)

            if len(count_phasedout_5_missing_cards(hand)[0]) == 2:
                if (discard[0] == 
                        count_phasedout_5_missing_cards(hand)[0][1][0][0]):
                    return (2, discard)
                else:
                    return (1, None)

            elif len(count_phasedout_5_missing_cards(hand)[0]) == 3:
                values_missing_for_run = [] 
                for value in count_phasedout_5_missing_cards(hand)[0][1][1:]:
                    values_missing_for_run.append(value)
                if (discard[0] in values_missing_for_run and 
                    my_colour[discard[1]] == 
                        count_phasedout_5_missing_cards(hand)[0][1][0]):
                    return (2, discard)

                if len(count_phasedout_5_missing_cards(hand)[0][2]) == 2:
                    if (discard[0] == 
                            count_phasedout_5_missing_cards(hand)[0][2][0]):
                        return (2, discard)

                return (1, None)    
            
    #In any other cases, after the player has phased out for a hand, the player
    #will choose to get rid of the cards with the highest values... 
    if (dict_of_next_players[turn_history[-1][0]] == player_id and 
        turn_history[-1][-1][-1][0] == 5 and 
            table[player_id][0] is not None):

        max_val_in_hand = 0
        for card in hand:
            if card[0] != 'A':
                if score_dict[card[0]] > max_val_in_hand:
                    max_val_in_hand = score_dict[card[0]]

        if score_dict[discard[0]] < max_val_in_hand:
            return (2, discard)
        
        return (1, None)
                       
    #The second play will either be phasing out (if the cards in the 
    #player's hand can be phased out), or placing cards on phases which are 
    #already on the table if the player has already phased out, or both, 
    #or none of them 
    if (turn_history[-1][0] == player_id and 
        turn_history[-1][-1][-1][0] != 5 and
        turn_history[-1][-1][-1][0] != 3 and 
            table[player_id][0] is None):
                                                    
        #If the player can phase out, he/she will choose to do so.
        if (type(count_phasedout_1_missing_cards(hand)) == list and 
                phase_required == 1):        
            return (3, count_phasedout_1_missing_cards(hand))
        
        if (type(count_phasedout_2_missing_cards(hand)) == list and 
                phase_required == 2):       
            return (3, count_phasedout_2_missing_cards(hand))
        
        if (type(count_phasedout_3_missing_cards(hand)) == list and 
                phase_required == 3):
            return (3, count_phasedout_3_missing_cards(hand))
        
        if (type(count_phasedout_4_missing_cards(hand)) == list and 
                phase_required == 4): 
            return (3, count_phasedout_4_missing_cards(hand))
        
        if (type(count_phasedout_5_missing_cards(hand)) == list and 
                phase_required == 5):
            return (3, count_phasedout_5_missing_cards(hand))
        
        #If the player cannot phase out, the only move that the player has left
        #is to discard. This is based on the phase required 
        if phase_required == 1:
            max_val = 0 
            values_required = []
            for lst in count_phasedout_1_missing_cards(hand)[0]:
                values_required.append(lst[1])

            for card in hand:
                if (card[0] != 'A' and 
                    card[0] not in values_required and
                        score_dict[card[0]] > max_val):
                    max_val = score_dict[card[0]]

            for card in hand:
                if (card[0] != 'A' and 
                    card[0] not in values_required and
                        score_dict[card[0]] == max_val):
                    return (5, card)

        if phase_required == 2:
            max_val = 0 
            for card in hand:
                if (card[0] != 'A' and 
                    card[1] != count_phasedout_2_missing_cards(hand)[0][1] and
                        score_dict[card[0]] > max_val):
                    max_val = score_dict[card[0]]

            for card in hand:
                if (card[0] != 'A' and 
                    card[1] != count_phasedout_2_missing_cards(hand)[0][1] and
                        score_dict[card[0]] == max_val):
                    return (5, card)

        if phase_required == 3:
            max_val = 0 
            values_required = []
            for lst in count_phasedout_3_missing_cards(hand)[0]:
                values_required.append(lst[1])

            for card in hand:
                if (card[0] != 'A' and 
                    card[0] not in values_required and
                        score_dict[card[0]] > max_val):
                    max_val = score_dict[card[0]]

            for card in hand:
                if (card[0] != 'A' and 
                        card[0] not in values_required and
                        score_dict[card[0]] == max_val):
                    return (5, card)

        if phase_required == 4:
            max_val = 0 
            for card in hand:

                if (card[0] != 'A' and 
                    card[0] not in count_phasedout_4_missing_cards(hand)[0] and
                        score_dict[card[0]] > max_val):
                    max_val = score_dict[card[0]]

            for card in hand:
                if (card[0] != 'A' and 
                    card[0] not in count_phasedout_4_missing_cards(hand)[0] and
                        score_dict[card[0]] == max_val):
                    return (5, card)

            #There exists the rare case where all cards in hand are values that  
            #are present in the best run. In this case, the card with the 
            #highest value is discarded 
            max_val = 0
            for card in hand:
                if card[0] != 'A' and card != 'ZZ':
                    if score_dict[card[0]] > max_val:
                        max_val = score_dict[card[0]]

            for card in hand:
                if score_dict[card[0]] == max_val:
                    return (5, card) 

        if phase_required == 5:
            max_val = 0  
            
            #In the case where for phase 5, we have the run of cards of the 
            #same colour, but miss the list of cards of the same value... 
            if len(count_phasedout_5_missing_cards(hand)[0]) == 2:                                   
                for card in hand:
                    if (card[0] != 'A' and 
                        card[0] != 
                        count_phasedout_5_missing_cards(hand)[0][1][0][0] and
                        card not in 
                        count_phasedout_5_missing_cards(hand)[0][0][0] and 
                            score_dict[card[0]] > max_val):
                        max_val = score_dict[card[0]]

                for card in hand:
                    if (card[0] != 'A' and 
                        card[0] != 
                        count_phasedout_5_missing_cards(hand)[0][1][0][0] and
                        card not in 
                        count_phasedout_5_missing_cards(hand)[0][0][0] and 
                            score_dict[card[0]] == max_val):
                        return (5, card)

            #In the case where for phase 5, we miss both the run of cards of  
            #the same colour, and the list of cards of the same value...           
            if len(count_phasedout_5_missing_cards(hand)[0]) == 3:
                cards_required_for_run = []

                for card in count_phasedout_5_missing_cards(hand)[0][0]:
                    cards_required_for_run.append(card)

                for card in hand:
                    if (card[0] != 'A' and 
                        card not in cards_required_for_run and
                        card[0] != 
                        count_phasedout_5_missing_cards(hand)[0][2][0] and
                            score_dict[card[0]] > max_val):
                        max_val = score_dict[card[0]]

                for card in hand:
                    if (card[0] != 'A' and 
                        card not in cards_required_for_run and
                        card[0] != 
                        count_phasedout_5_missing_cards(hand)[0][2][0] and 
                            score_dict[card[0]] == max_val):
                        return (5, card)

            #There exists the rare case where all cards in hand are values that  
            #are present in the best run. In this case, the card with the 
            #highest value is discarded 
            max_val = 0
            for card in hand:
                if card[0] != 'A':
                    if score_dict[card[0]] > max_val:
                        max_val = score_dict[card[0]]

            for card in hand:
                if score_dict[card[0]] == max_val:
                    return (5, card)                                                   
                                                                                                                            
    #If the player has already phased out, the player can choose whether 
    #to place other cards in his/her hand in other phases on the table,
    #or to discard a card from his/her hand and end his/her turn
                   
    if (turn_history[-1][0] == player_id and
        (turn_history[-1][-1][-1][0] == 1 or
         turn_history[-1][-1][-1][0] == 2 or 
         turn_history[-1][-1][-1][0] == 3 or
         turn_history[-1][-1][-1][0] == 4) and 
            table[player_id][0] is not None):
                   
        aces = 0   
        for card in hand:
            if card[0] == 'A':
                aces += 1
                                 
        #For non-wild cards in the player's hand, the player can 
        #choose to place them on the phases on the table, which depends 
        #on the phase types
        for phase in table:
            
            if phase[0] == 5:                           
                                                      
                my_iterator = iter(phase[1][0])
                position = 0
                
                #Trying to add cards to the run of cards of the same colour
                for card in phase[1][0]:
                    position += 1 
                    if card[0] != 'A':
                        colour_required = my_colour[card[1]]
                        counter = score_dict[card[0]]
                        break

                while position:
                    counter -= 1
                    position -= 1

                if counter <= 1:
                    value_in_left_end = None
                else:
                    value_in_left_end = counter 

                for card in my_iterator:
                    if card[0] != 'A':
                        counter2 = score_dict[card[0]]
                        break

                for card in my_iterator:
                    counter2 += 1

                value_in_right_end = counter2 + 1 

                for card in hand:
                    if value_in_left_end is not None:                                
                        if (card[0] == 
                                score_dict_reverse[value_in_left_end] and 
                                my_colour[card[1]] == colour_required):
                            return (4, (card, (table.index(phase), 0, 0)))

                    if value_in_right_end <= 13:
                        if (card[0] ==
                                score_dict_reverse[value_in_right_end] and 
                                my_colour[card[1]] == colour_required):
                            return (4, (card, (table.index(phase), 0, 
                                               len(phase[1][0])))) 
                        
                #Trying to add cards to the list of cards of the same value
                for card in phase[1][1]:
                    if card[0] != 'A':
                        value_required = card[0]
                        break
                        
                for card in hand:
                    if card[0] == value_required:
                        return (4, (card, (table.index(phase), 1, 0)))
            
            values_for_phase_5_right_end = []
            values_for_phase_5_left_end = []
            if phase[0] == 5:                           
                                                      
                my_iterator = iter(phase[1][0])
                position = 0
                
                for card in phase[1][0]:
                    position += 1 
                    if card[0] != 'A':
                        colour_required = my_colour[card[1]]
                        counter = score_dict[card[0]]
                        break

                while position:
                    counter -= 1
                    position -= 1

                if counter <= 1:
                    value_in_left_end = None
                else:
                    value_in_left_end = counter 

                for card in my_iterator:
                    if card[0] != 'A':
                        counter2 = score_dict[card[0]]
                        break

                for card in my_iterator:
                    counter2 += 1

                value_in_right_end = counter2 + 1
                
                if value_in_right_end <= 13:                
                    values_for_phase_5_right_end.append(value_in_right_end)
                
                if value_in_right_end <= 12:                
                    values_for_phase_5_right_end.append(value_in_right_end + 1)
                    
                if value_in_left_end is not None:
                    if value_in_left_end >= 2:                
                        values_for_phase_5_left_end.append(value_in_left_end)
                    
                    if value_in_left_end >= 3:                
                        values_for_phase_5_left_end.append(value_in_left_end - 
                                                           1)
                
                if len(values_for_phase_5_right_end) == 2:                    
                    for card in hand:
                        if (score_dict[card[0]] == 
                            values_for_phase_5_right_end[1] and 
                            my_colour[card[1]] == colour_required and 
                                aces >= 1):
                            for card in hand:
                                if card[0] == 'A':
                                    return (4, (card, (table.index(phase), 0, 
                                                       len(phase[1][0])))) 
                                
                if len(values_for_phase_5_left_end) == 2:                   
                    for card in hand:
                        if (score_dict[card[0]] == 
                            values_for_phase_5_left_end[1] and 
                            my_colour[card[1]] == colour_required and 
                                aces >= 1):
                            for card in hand:
                                if card[0] == 'A':
                                    return (4, (card, (table.index(phase), 0, 
                                                       0))) 
                                                                                                 
            if phase[0] == 4:
                for lst in phase[1]:
                            
                            
                    my_iterator = iter(lst)
                    position = 0
                        
                    for card in lst:
                        position += 1                                
                        if card[0] != 'A':
                            counter = score_dict[card[0]]
                            break
                                    
                    while position:
                        counter -= 1
                        position -= 1
                                
                    if counter <= 1:
                        value_in_left_end = None
                    else:
                        value_in_left_end = counter 
                                
                    for card in my_iterator:
                        if card[0] != 'A':
                            counter2 = score_dict[card[0]]
                            break
                                    
                    for card in my_iterator:
                        counter2 += 1
                                
                    value_in_right_end = counter2 + 1 
                            
                    for card in hand:
                        if value_in_left_end is not None:                                
                            if (card[0] == 
                                    score_dict_reverse[value_in_left_end]):
                                return (4, (card, (table.index(phase), 
                                                   0, 0)))
                            
                        if value_in_right_end <= 13:
                            if (card[0] ==
                                    score_dict_reverse[value_in_right_end]):
                                return (4, (card, (table.index(phase), 0, 
                                                   len(lst))))
                            
            values_for_phase_4_right_end = []
            values_for_phase_4_left_end = []
            if phase[0] == 4:                           
                                                      
                my_iterator = iter(phase[1][0])
                position = 0
                
                #Trying to add cards to the run of cards of the same colour
                for card in phase[1][0]:
                    position += 1 
                    if card[0] != 'A':
                        colour_required = my_colour[card[1]]
                        counter = score_dict[card[0]]
                        break

                while position:
                    counter -= 1
                    position -= 1

                if counter <= 1:
                    value_in_left_end = None
                else:
                    value_in_left_end = counter 

                for card in my_iterator:
                    if card[0] != 'A':
                        counter2 = score_dict[card[0]]
                        break

                for card in my_iterator:
                    counter2 += 1
                
                value_in_right_end = counter2 + 1
                while value_in_right_end < 13:
                    value_in_right_end += 1  
                    values_for_phase_4_right_end.append(value_in_right_end)
                
                if value_in_left_end is not None:
                    values_for_phase_4_right_end.append(value_in_left_end)
                    while value_in_left_end > 2:
                        value_in_left_end -= 1
                        values_for_phase_4_left_end.append(value_in_left_end)
                    
                if len(values_for_phase_4_right_end) == 4:                   
                    J_present = False
                    Q_present = False
                    K_present = False
                    
                    for card in hand:
                        if card[0] == 'J':
                            J_present = True
                        if card[0] == 'Q':
                            Q_present = True
                        if card[0] == 'K':
                            K_present = True
                            
                    if J_present:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                            
                    if Q_present and J_present is False and aces >= 2:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                            
                    if (K_present and J_present is False and 
                            Q_present is False and aces >= 3):
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                                                 
                if len(values_for_phase_4_right_end) == 3:
                    Q_present = False
                    K_present = False
                    
                    for card in hand:
                        if card[0] == 'Q':
                            Q_present = True
                        if card[0] == 'K':
                            K_present = True
                            
                    if Q_present:
                        
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
 
                    if K_present and aces >= 2:                 
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                    
                                
                if len(values_for_phase_4_right_end) == 2:
                    K_present = False
                    
                    for card in hand:
                        if card[0] == 'K':
                            K_present = True
                    
                    if K_present and aces >= 1:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                
                
                if len(values_for_phase_4_left_end) == 4:                   
                    four_present = False
                    three_present = False
                    two_present = False
                    
                    for card in hand:
                        if card[0] == '4':
                            four_present = True
                        if card[0] == '3':
                            three_present = True
                        if card[0] == '2':
                            two_present = True
                            
                    if four_present:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                            
                    if three_present and four_present is False and aces >= 2:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                            
                    if (two_present and four_present is False and 
                            three_present is False and aces >= 3):
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                                                 
                if len(values_for_phase_4_right_end) == 3:
                    three_present = False
                    two_present = False
                    
                    for card in hand:
                        if card[0] == '3':
                            three_present = True
                        if card[0] == '2':
                            two_present = True
                            
                    if three_present:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                    
                    if two_present and aces >= 2:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                    
                                
                if len(values_for_phase_4_right_end) == 2:
                    two_present = False
                    
                    for card in hand:
                        if card[0] == '2':
                            two_present = True
                    
                    if two_present and aces >= 1:
                        for card in hand:
                            if card[0] == 'A':
                                return (4, (card, (table.index(phase), 0, 
                                                   len(phase[1][0]))))
                            
                #If there's is only phase 4 on the table, and no conditions 
                #above are passed, and you still have aces in your hand, you 
                #would still want to get rid of the aces if possible.
                #The code below ensures this
                for lst in phase[1]:                                                     
                    my_iterator = iter(lst)
                    position = 0
                        
                    for card in lst:
                        position += 1                                
                        if card[0] != 'A':
                            counter = score_dict[card[0]]
                            break
                                    
                    while position:
                        counter -= 1
                        position -= 1
                                
                    if counter <= 1:
                        value_in_left_end = None
                    else:
                        value_in_left_end = counter 
                                
                    for card in my_iterator:
                        if card[0] != 'A':
                            counter2 = score_dict[card[0]]
                            break
                                    
                    for card in my_iterator:
                        counter2 += 1
                                
                    value_in_right_end = counter2 + 1 
                            
                    for card in hand:
                        if card[0] == 'A' and value_in_left_end is not None:
                            return (4, (card, (table.index(phase), 0, 0)))
                        elif card[0] == 'A' and value_in_right_end <= 13:
                            return (4, (card, (table.index(phase), 0, 
                                               len(lst))))
                                                                                  
        for phase in table:
                                                                                                 
            if phase[0] == 1:                                              
                for lst in phase[1]:
                    for card in lst:
                        if card[0] != 'A':
                            value_required = card[0]
                            break
                    for card in hand:
                        if card[0] == value_required:
                            return (4, (card, (table.index(phase),
                                               phase[1].index(lst), 0)))
                        elif card[0] == 'A':
                            return (4, (card, (table.index(phase),
                                               phase[1].index(lst), 0)))
                                                                                      
            if phase[0] == 2:
                for lst in phase[1]:
                    for card in lst:
                        if card[0] != 'A':
                            suit_required = card[1]
                            break
                    for card in hand:
                        if card[1] == suit_required:
                            return (4, (card, (table.index(phase), 0, 0)))
                        elif card[0] == 'A':
                            return (4, (card, (table.index(phase), 0, 0)))
                                
            if phase[0] == 3:
                for lst in phase[1]:
                    for card in lst:
                        if card[0] != 'A':
                            value_required = card[0]
                            break
                    for card in hand:
                        if card[0] == value_required:
                            return (4, (card, (table.index(phase),
                                               phase[1].index(lst), 0)))
                        elif card[0] == 'A':
                            return (4, (card, (table.index(phase),
                                               phase[1].index(lst), 0)))
                        
            if phase[0] == 5:                           
                                                                                            
                #Trying to add cards to the list of cards of the same value
                for card in phase[1][1]:
                    if card[0] != 'A':
                        value_required = card[0]
                        break
                        
                for card in hand:
                    if card[0] == value_required:
                        return (4, (card, (table.index(phase), 1, 0)))
                    elif card[0] == 'A':
                        return (4, (card, (table.index(phase), 1, 0)))
    
    #If the player has phased out, the player will choose to discard cards 
    #with the highest values first 
    if turn_history[-1][0] == player_id and table[player_id][0] is not None:
        max_value = 0
        for card in hand:
            if score_dict[card[0]] > max_value and card[0] != 'A':
                max_value = score_dict[card[0]]
        
        if max_value != 0:
            for card in hand:
                if card[0] == score_dict_reverse[max_value] and card[0] != 'A':
                    return (5, card)
        else:
            for card in hand:
                return (5, card)
  
if __name__ == '__main__':
    # Example call to the function.
    print(phasedout_play(1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H', '0S', 'JS']]), (None, []), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (4, ('0S', (1, 0, 8))), (4, ('JS', (1, 0, 9)))])], [0, 4, 0, 0], ['5D'], '7H'))
    