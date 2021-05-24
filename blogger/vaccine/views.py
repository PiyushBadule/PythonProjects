from django.shortcuts import render
import json
import datetime
import requests

def index(request):
    if request.method == 'GET':
        return render(request, "index.html")

    else:
        date = request.POST['date']
        date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
        age = int(request.POST['age'])
        pincode = request.POST['pincode']
        response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode"
           "={}&date={}".format(pincode, date), headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})
        if response.ok:
            data = response.json()
            center1 = []
            sesssion1 = []
            signal = 0

            for center in data['centers']:
                for session in center['sessions']:
                    if (session["min_age_limit"] <= age and session["available_capacity"] > 0):
                        sesssion1.append(session)
                        center1.append(center)
                        signal += 1
            #
            #         else:
            #             context = {'Availibility':"Sorry Vaccine is Not availabel at current Date and Location"
            #                                       "Please Search for Another PinCode"}

            context = {'signal': signal, "data_list": zip(center1, sesssion1)}
            return render(request, "index.html", context)

def test(request):
    return render(request, "vaccineform.html")
# 110054