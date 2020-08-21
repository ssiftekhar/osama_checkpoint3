customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]
def fraud_detection(salary, taxes):
    tax_rate = []
    if len(taxes) == len(salary):
        for i in range(0, len(taxes)):
            tax_rate.append(taxes[i] / salary[i])
        return (tax_rate)
    else:
        return(None)
    print(tax_rate)
    
    
    # tax_rate = [
    #     taxes[i] / salary[i]
    #     for (taxes[i], salary[i]) in
    #     zip(taxes, salary)
    #     ]
    
        