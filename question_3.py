# Question 3:
# The company SuperSale3000 want to rank its sales team at the end of every week. 
# Each call gives the seller 10 points, each meeting 30 points and each sale 100 points. 
# There is also a 100-point bonus for each, if you make more than 150 calls, or 20 meetings or 5 sales.
# Create a new file called “question_3.py”.

# They already have the data for each employee saved in a dictionary.
# At the top of the file set the following example dictionary for Jodan Belfort:
# Jordan_belfort = {‘calls’: 178, ‘meetings’:17,  ‘sales’:6}
# Add the following logic to calculate the total score from the dictionary and add it to the same dictionary using the key ‘score’


jordan_belfort = {'calls': 178, 'meetings':17, 'sales':6}

CALLS_M = 10
MEETINGS_M = 30
SALES_M = 100

score = 0

score = score + jordan_belfort['calls']*CALLS_M
score = score + jordan_belfort['meetings']*MEETINGS_M
score = score + jordan_belfort['sales']*SALES_M
if jordan_belfort['calls']>150:
    score = score + 100
if jordan_belfort['meetings']>20:
    score = score + 100
if jordan_belfort['sales']>5:
    score = score + 100

jordan_belfort['score'] = score
