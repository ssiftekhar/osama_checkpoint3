
Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}

def add_point():
    calls = 0
    meetings = 0
    sales = 0
    for key in Jordan_belfort:
        if calls:
            calls = calls + 10
        elif meetings:
            meetings = meetings + 30
        elif sales:
            sales = sales + 100
         

