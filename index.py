def start():
    print('This is my rock paper scissor game!')
    player_one = 'Jack'
    player_two = 'Eric'
    
    def choices(player_one_choice,player_two_choice):
        if player_one_choice == 'rock' and player_two_choice == 'paper':
            return ('paper covers rock '+ player_two +'wins!')
        elif player_one_choice == 'paper' and player_two_choice == 'rock':
            return ('paper covers rock '+ player_one +'wins!')
        elif player_one_choice == 'scissors' and player_two_choice == 'paper':
            return ('scissor cuts paper'+ player_one +'wins!')
        elif player_one_choice == 'rock' and player_two_choice == 'scissors':
            return ('rock mashes scissor'+ player_one +'wins!')
        elif player_one_choice == 'paper' and player_two_choice == 'scissors':
            return ('scissor cuts paper'+ player_two +'wins!')
        elif player_one_choice == 'scissors' and player_two_choice == 'rock':
            return ('rock mashes scissor'+ player_two +'wins!')
        elif player_one_choice == player_two_choice :
            return('Jack and Eric tied')
        else:
            return('type rock, paper,scissors')
    player_one_choice = input('Does ' + player_one+ 'choose Rock, Paper ,Scissor')
    player_two_choice = input('Does ' + player_two+ 'choose Rock, Paper ,Scissor')
    print(choices(player_one_choice, player_two_choice))
    
    def Play_Again():
        Again = input('Would you like to play again').lower()
        if Again == 'No'.lower():
            quit()
        elif Again == 'Yes'.lower():
            start()
        else:
            print('Please enter yes or no')
            Play_Again()
    Play_Again()
start()
