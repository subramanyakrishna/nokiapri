def getCorrectUnitPerDay(X):
    X[1] = X[1]/100
    X[2] = 0.621371 *X[2] #0.621371 
    X[6] = 2.23694 *X[6]   #2.23694 
    pmb = X[7]
    hm = X[8]
    X[7] = 0.02953 *X[7] #0.02953
    pmbmin0_3 = pmb-0.3
    pmbmin0_3toPower0_190284 = pmbmin0_3**0.190284
    hmBYpmbmin0_3toPower0_190284 = hm/pmbmin0_3toPower0_190284
    rightEq = (1+0.0000842288*hmBYpmbmin0_3toPower0_190284)**5.25530260032
    X[8] = pmbmin0_3*rightEq
    X[8]= 0.02953*X[8]
    return X

def getCorrectUnit(X):
    X[0] = X[0]/100
    X[1] = 0.621371 *X[1] #0.621371 
    X[5] = 2.23694 *X[5]   #2.23694 
    pmb = X[6]
    hm = X[7]
    X[6] = 0.02953 *X[6] #0.02953
    pmbmin0_3 = pmb-0.3
    pmbmin0_3toPower0_190284 = pmbmin0_3**0.190284
    hmBYpmbmin0_3toPower0_190284 = hm/pmbmin0_3toPower0_190284
    rightEq = (1+0.0000842288*hmBYpmbmin0_3toPower0_190284)**5.25530260032
    X[7] = pmbmin0_3*rightEq
    X[7]= 0.02953*X[7]
    return X
 