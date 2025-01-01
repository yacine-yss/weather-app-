
from flask import Flask , render_template 
from flask import request
import requests

weather=Flask(__name__)

api_key="f6708564fa93a30704b801d0790ba675"
api_url="https://api.openweathermap.org/data/2.5/weather"

@weather.route('/',methods=['POST','GET'])
def add():

    if request.method=='POST':
        city=request.form.get('city')
        if city:
            response= requests.get(
            url=api_url,
            params={
                "q":city,
                "appid":str(api_key),
                "units":"metric"
            }
        )
        if response.status_code==200:
            weather_data=response.json()
            temp=f"the weather on "+city+" is "+str(weather_data['main']['temp'])+" °C"
            icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png"
            return render_template('home.html', temp=temp,icon_url=icon_url)

        else:
            error='error api not found'
            return render_template('home.html', error=error)
    else:
        error='please enter a city'
        return render_template('home.html', error=error)

    


    return render_template('home.html') 


if __name__=='__main__':
    weather.run(debug=True)

