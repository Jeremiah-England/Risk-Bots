""" I will set each continent to a number in the order of their size (unless they are equal, then from left to right on the board), and then I will number them in that order. When this is done, we see that
1 = 'Asia'
2 = 'North America'
3 = 'Europe'
4 = 'Africa'
5 = 'South America'
6 = 'Australia'

The next step in the process of identifying a game state is the assing each proper a number. We go left to right, top to bottom on each continent and label the countries.

For Aisa we hav
e--
01 = 'Ural'
02 = 'Siberia'
03 = 'Yakutsk'
04 = 'Kamchaika'
05 = 'Afghanistan'
06 = 'China'
07 = 'Mongolia'
08 = 'Irkutsk'
09 = 'Japan'
10 = 'Middle East'
11 = 'India'
12 = 'Siam'

For North America we have--
01 = 'Alaska'
02 = 'Northwest Territory'
03 = 'Greenland'
04 = 'Alberta'
05 = 'Ontario'
06 = 'Quabec'
07 = 'Western United Sates'
08 = 'Eastern United States'
09 = 'Central America'

For Europe we have--
01 = 'Iceland'
02 = 'Scandinavia'
03 = 'Ukraine'
04 = 'Great Brittain'
05 = 'Northern Europe'
06 = 'Western Europe'
07 = 'Southern Europe'

For Africa we have--
01 = 'North Africa'
02 = 'Egypt'
03 = 'Congo'
04 = 'East Africa'
05 = 'South Africa'
06 = 'Madagascar'

For South America we have--
01 = 'Venesuela'
02 = 'Peru'
03 = 'Brazil'
04 = 'Argentina'

For Australia we have--
01 = 'Indonesia'
02 = 'New Guinea'
03 = 'Western Australia'
04 = 'Eastern Australia'

Now the name of each peice of land is the number of the continent in the hundreds place, and the number of the country within the continent in the ones place.

For Aisa we have--
101 = 'Ural'
102 = 'Siberia'
103 = 'Yakutsk'
104 = 'Kamchaika'
105 = 'Afghanistan'
106 = 'China'
107 = 'Mongolia'
108 = 'Irkutsk'
109 = 'Japan'
110 = 'Middle East'
111 = 'India'
112 = 'Siam'

For North America we have--
201 = 'Alaska'
202 = 'Northwest Territory'
203 = 'Greenland'
204 = 'Alberta'
205 = 'Ontario'
206 = 'Quabec'
207 = 'Western United Sates'
208 = 'Eastern United States'
209 = 'Central America'

For Europe we have--
301 = 'Iceland'
302 = 'Scandinavia'
303 = 'Ukraine'
304 = 'Great Brittain'
305 = 'Northern Europe'
306 = 'Western Europe'
307 = 'Southern Europe'

For Africa we have--
401 = 'North Africa'
402 = 'Egypt'
403 = 'Congo'
404 = 'East Africa'
405 = 'South Africa'
406 = 'Madagascar'

For South America we have--
501 = 'Venesuela'
502 = 'Peru'
503 = 'Brazil'
504 = 'Argentina'

For Australia we have--
601 = 'Indonesia'
602 = 'New Guinea'
603 = 'Western Australia'
604 = 'Eastern Australia'
"""
'''
For indexing the players, I think it would be best if we just number them in alphabetical order--
1 = 'black'
2 = 'blue'
3 = 'gray'
4 = 'green'
5 = 'red'
6 = 'yellow'
'''
'''
The variables which define any attack is who is attacking who, with how many, from where and to where, and how many does the defender have.
However, assumging that we have an updated game-state, we should able to merely state
    - what piece is attking (from this we know who is attcking who),
    - with how many (we know how many are possible from the game-state's representaion of the countries guy_number),
    - what peice is defending (from this we know how many defenders there are, and who the defender is).

Therefore, the code for attaking should look something like this:

"105 attacks 106 with 3 men."

If the defender decides to retreat, you could print

"106 retreated 4 men to 108."

If the defender losses two men you could print

"106 lost 2 men and 105 lost 0 men"

And after the battle, you could print out how many men the attacker moves into the conqured square like this:

"105 moves 4 men into 106"
'''
'''
Now let's work through a game turn and try ever posslbe move and check to make sure that our code is comprihensive.
The senario is that Green starts his turn. The turn sequence is--
    - Trading in risk cards
    - Placing new armies
    - Attacking
    - Fortifying a position

Trading in risk cards:
    "4 trades in risk cards (105, 206, wild)"
    "recieves 10 men." (to make things simple, I think we should let them place wherever they would like)
    "4 places 2 men on 105" (these men did not come out of the ten mentioned above)

Placing armies:
    "4 recives 4 men" (from continents and such)
    "4 places 5 men on 105"
    "4 places 3 men on 601"
    "4 places 6 men on 107"

Attacking:
    "107 attacks 104 with 3 men"
    "104 lost 1 men and 107 lost 1 men"
    "107 attacks 104 with 3 men"
    "104 moves 2 men to 303"
    "104 lost 1 men and 107 lost 0 men"

Fortifying a position:
    "105 moves 4 men to 104"

Ending turn:
    "4 ends a turn"

Starting next turn:
    "6 starts a turn"
'''
''' reprisenting a game.state()

It could be done as a list of lists, where each sublist has three variables ['place#', 'player','number_of_guys'].
For example, let's say that 'green' has three men on country 402. [402, 4, 3]

But that is not the whole game.state
We need to know how many risk cards each player has, who's turn it is, and what phase of the turn the player is in. For example, if is it green's turn
and he has not yet placed his men, then we know that he is actually going to get a lot more, which is significant for the computers eveluation of the gamestate.
'''
