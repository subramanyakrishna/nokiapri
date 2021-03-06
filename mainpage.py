
from requests import request

def getWeatherData(lat,long,hour):
    urlWeatherBit = "https://api.weatherbit.io/v2.0/current?lat="+str(lat)+"&lon="+str(long)+"&key=f7936d7a38314c8fb59614efbf9801f2"
    res = request("GET", urlWeatherBit)
    if res.status_code==428:
        urlWeatherBit = "https://api.weatherbit.io/v2.0/current?lat="+str(lat)+"&lon="+str(long)+"&key=59f5d57433e2469496b0fb171cbadd55"
        res = request("GET", urlWeatherBit)
    resFromWebit = res.json()
    city_name = resFromWebit['data'][0]["city_name"]
    visibility = float(resFromWebit['data'][0]['vis'])
    cloudcoverage = float(resFromWebit['data'][0]['clouds'])
    temperature = float(resFromWebit['data'][0]['temp'])
    dewpoint = float(resFromWebit['data'][0]['dewpt'])
    relativehumidity = float(resFromWebit['data'][0]['rh'])
    windspeed = float(resFromWebit['data'][0]['wind_spd'])
    stationpressure = float(resFromWebit['data'][0]['pres'])
    urlAltitude = "https://api.opentopodata.org/v1/aster30m?locations="+str(lat)+","+str(long)+""  
    resAltimeter = request("GET", urlAltitude).json()
    altimeter=float(resAltimeter['results'][0]['elevation'])
    X  = [hour,cloudcoverage,visibility,temperature,dewpoint,relativehumidity,windspeed,stationpressure,altimeter]
    return X,city_name



