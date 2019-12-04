#Test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
def nb_year(p0, percent, aug, p):
    #people = 1500
    #per = 5
    #move = 100
    #target = 5000
    p0_new = p0
    n = 0
    while p0_new <= p:
        p0_new = p0_new * (1 + percent*0.01) + aug
        n = n + 1
        
    return n  
def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year
