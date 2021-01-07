from flask import Flask, render_template, request
import datetime
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html')

@app.route('/visualization')
def visualization():    
    return render_template('visualization.html')

@app.route('/visualization/reservation')
def vis_res():    
    return render_template('vis-reservation.html')

@app.route('/visualization/trends')
def vis_trends():    
    return render_template('vis-trends.html')

@app.route('/visualization/deposit')
def vis_dep():    
    return render_template('vis-deposit.html')

@app.route('/visualization/market')
def vis_mrt():    
    return render_template('vis-market.html')

@app.route('/visualization/other')
def vis_otr():    
    return render_template('vis-other.html')

@app.route('/prediction')
def prediction():    
    return render_template('prediction.html')

@app.route('/prediction/result', methods=['POST', 'GET'])
def result():

    if request.method == 'POST':
        input = request.form
        
        ## input from prediction.html
        hotel=str(input['hotel'])
        leadtime=int(input['leadtime'])
        tahun = int(input['arrival'][:4])
        bulan = int(input['arrival'][5:7])
        tanggal = int(input['arrival'][8:])
        arrival = datetime.datetime(tahun, bulan, tanggal)
        staysday=int(input['staysday'])
        staysend=int(input['staysend'])
        adults=int(input['adults'])
        children=int(input['children'])
        baby=int(input['baby'])
        meal=str(input['meal'])
        country=str(input['country'])
        market=str(input['market'])
        distribution=str(input['distribution'])
        customer=str(input['customer'])
        repeatedguest=str(input['repeatedguest'])
        prevcancel=str(input['prevcancel'])
        prevnotcancel=str(input['prevnotcancel'])
        room=str(input['room'])
        bookschange=int(input['bookschange'])
        deposit=str(input['deposit'])
        agent=str(input['agent'])
        company=str(input['company'])
        daywait=int(input['daywait'])
        adr=float(input['adr'])
        carparking=str(input['carparking'])
        specialrequest=str(input['specialrequest'])

        ## arrival date extraction
        arrival_year = int(arrival.strftime("%Y"))
        arrival_week = (int(arrival.strftime("%W")) + 1)
        arrival_day = int(arrival.strftime("%d"))
        arrival_month= str(arrival.strftime("%B"))

        stays = staysday + staysend

        ## replace value to digit
        aa = lambda x: 0 if x==0 else 1
        family = aa(baby + children)

        aa = lambda x: 0 if x=='Resort Hotel' else 1
        hotel_ = aa(hotel)

        aa = lambda x: 0 if x=='SC' else (1 if x=='BB' else(2 if x=='HB' else 3))
        meal_ = aa(meal)

        aa = lambda x: 0 if x=='Domestic' else 1
        country_ = aa(country)

        aa = lambda x: 0 if x=='No Deposit' else 1
        deposit_ = aa(deposit)

        aa = lambda x: 0 if x=='No' else 1
        rpt = aa(repeatedguest)
        prevc = aa(prevcancel)
        prevn = aa(prevnotcancel)
        agent_ = aa(agent)
        company_=aa(company)
        carp = aa(carparking)
        sper = aa(specialrequest)

        ## list of input to predict
        data = [hotel_, leadtime, arrival_year, arrival_week, arrival_day,
                    staysend, staysday, adults, children, baby, meal_, country_,
                    rpt, prevc, prevn, bookschange, deposit_, agent_, company_,
                    daywait, adr, carp, sper, family, stays]

        ## one hot encoding
        mrt = ['Corporate', 'Direct', 'Groups', 'Offline TA/TO', 'Online TA']
        mrt_ = [1 if x == market else 0 for x in mrt]
        am = ['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September']
        am_ = [1 if x == arrival_month else 0 for x in am]
        rm = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'P']
        rm_= [1 if x == room else 0 for x in rm]
        dc = ['Corporate', 'Direct', 'GDS', 'TA/TO']
        dc_= [1 if x == distribution else 0 for x in dc]
        ct = ['Other', 'Transient', 'Transient-Party']
        ct_= [1 if x == customer else 0 for x in ct]

        ## concat list input and one hot
        var = data + mrt_ + am_ + rm_ + dc_ + ct_
        var = scaler.transform([var])
        pred = model.predict_proba(var)[:,1]

        if pred > thresh:
            pred = 'Cancel'
        else:
            pred = 'Not Cancel'         


    return render_template (
        'result.html',
        hotel=hotel,
        leadtime=leadtime,
        arrival=(f'{arrival_day} {arrival_month} {arrival_year}'),
        staysday=staysday,
        staysend=staysend,
        adults=adults,
        children=children,
        baby=baby,
        meal=meal,
        country=country,
        market=market,
        distribution=distribution,
        customer=customer,
        repeatedguest=repeatedguest,
        prevcancel=prevcancel,
        prevnotcancel=prevnotcancel,
        room=room,
        bookschange=bookschange,
        deposit=deposit,
        agent=agent,
        company=company,
        daywait=daywait,
        adr=adr,
        carparking=carparking,
        specialrequest=specialrequest,
        pred=pred
    )
    


if __name__ == '__main__':
    ## load model ## model can get in file 4.1 Model.ipynb and run joblib dump
    model = joblib.load('model')
    scaler = joblib.load('scaler')
    thresh = joblib.load('thresh')
    app.run(debug=True)