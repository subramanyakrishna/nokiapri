import mainpage
import perday
import monthly
import utils
from flask import Flask,render_template,request
from pickle import load
model = load(open('gbr1.pkl','rb'))
from datetime import date, timedelta

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('index.html') #this by itself selects template folder

def getPerDayChart(lat,long,endDate,startDate):
    resFromWebit = perday.getWeatherDataForPerDay(lat,long,endDate,startDate)
    altimeter = perday.locElevationForPerDay(lat, long)
    solarOutputPerhours = list()
    time = list()
    for i in range(0,24):
        X = perday.refinedDataForPerDay(resFromWebit, i)
        X.append(altimeter)
        X = utils.getCorrectUnitPerDay(X)
        if (X[0]>=0 and X[0]<=5) or (X[0]>=18 and X[0]<=24):
                solarOutputPerhours.append(0)
                time.append(X[0])
                continue
        time.append(X[0])
        X = list([X])
        pred = model.predict(X)
        solarOutputPerhours.append(pred[0])
        X = []
    solarOutputPerDay = sum(solarOutputPerhours)
    return solarOutputPerhours,time,solarOutputPerDay


@app.route('/perday',methods=['POST'])
def home():
    lat = float(request.form['lat'])
    long = float(request.form['long'])
    endDate = request.form['endDate']
    hour =  utils.getTime(lat,long)
    endDate = date.fromisoformat(endDate)
    if date.today() < endDate:
        return {"response":"Please select date lesser than todays date since we can't get the future environmental condition to predict solar output","mainpageUrl":"https://solaroutputprediction.herokuapp.com/"}
    if(utils.checkLimitExceeded()):
        return {"response":"Weatherbit API limit exceeded"}
    startDate = (endDate-timedelta(days=1)).isoformat() 
    solarOutputPerhours,times,solarOutputPerDay = getPerDayChart(lat,long,endDate,startDate)
    X,city_name = mainpage.getWeatherData(lat,long,hour)
    X = utils.getCorrectUnit(X)
    averageSolarEnergyPerHour = round(sum(solarOutputPerhours)/12,3)
    costsavings = round(5.73*averageSolarEnergyPerHour,3)
    co2 = round(0.185*averageSolarEnergyPerHour,3)
    if (hour>=0 and hour<=5) or (hour>=18 and hour<=24):
        return render_template('perday.html',currTimeprediction=0,solarOutputPerhours=solarOutputPerhours,time=times,solarOutputPerDay=solarOutputPerDay,costsavings = costsavings,averageSolarEnergyPerHour=averageSolarEnergyPerHour,co2 = co2,city_name=city_name,lat=lat,long=long,endDate=endDate)
    X = list([X])
    pred = round(model.predict(X)[0],3)
    return  render_template('perday.html',currTimeprediction = pred,solarOutputPerhours=solarOutputPerhours,time=times,solarOutputPerDay=solarOutputPerDay,costsavings = costsavings,averageSolarEnergyPerHour=averageSolarEnergyPerHour,co2 = co2,city_name=city_name,lat=lat,long=long,endDate=endDate)

@app.route('/monthly',methods=['POST','GET'])
def monthlyRoute():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    endDate = request.args.get('endDate')
    return monthly.monthlyData(lat,long,endDate)

if(__name__=="__main__"):
    app.run(debug=True)