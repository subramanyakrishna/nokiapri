from requests import request

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
    
def getTime(lat,long):
    url = "http://api.timezonedb.com/v2.1/get-time-zone?key=AFCJPL4UYY4H&format=json&by=position&lat="+str(lat)+"&lng="+str(long)
    res = request("GET", url).json()
    return float(res["formatted"][11:13])

def checkLimitExceeded():
    urlWeatherBit = "https://api.weatherbit.io/v2.0/history/hourly?lat=23&lon=70&start_date=2021-05-23&end_date=2021-05-24&tz=local&key=c19308a05e44450f805946e96f0743d0"
    res = request("GET", urlWeatherBit)
    return res.status_code == 429