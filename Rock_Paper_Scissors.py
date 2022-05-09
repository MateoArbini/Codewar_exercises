Rock Paper Scissors
Lets play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!

Solution:

def rps(p1, p2):
    move1 = "rock"
    move2 = "scissors"
    move3 = "paper"
    alert1 = "Player 1 won!"
    alert2 = "Player 2 won!"
    alert3 = "Draw!"
    if p1 == p2:
        return alert3
    elif p1 == move1 and p2 == move2 or p1 == move2 and p2 == move3 or p1 == move3 and p2 == move1:
        return alert1
    else:
        return alert2
