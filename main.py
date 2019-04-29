import requests as rq
from flask import Flask, request
import json
import regras as Rules
from pprint import pprint
from sqlRules import DataBase


app = Flask(__name__) 


@app.route("/", methods=['POST']) 
def hello():
    
    apikey = "VcG4or5T7rPynectLEGYyUQRoMySGjrl"
    jsonList = ["São Paulo", "Santos", "Ribeirão Preto", "Sorocaba"]
    jsonState = ["SP", "SP", "SP", "SP"]
    jsonDict = {}
    with open('jsonTest.json', encoding='utf-8') as f:
       jsonDict = json.load(f)

    db = DataBase()
    #jsonList = []
    #jsonDict = {}
    '''
    for junit in request.json["cidades"]:
        
        state = junit["estado"]
        city = junit["cidade"]
        cityInfo = rq.get("http://dataservice.accuweather.com/locations/v1/cities/BR/"+state+
        "/search?apikey="+apikey+"&q="+city).json()[0]
        print(cityInfo)
        finalJson = rq.get("http://dataservice.accuweather.com/currentconditions/v1/"+cityInfo["Key"]+
        "/historical/24?apikey="+apikey)
        jsonDict[cityInfo["LocalizedName"]+"Temp"] = finalJson.json()[0]
        jsonDict[cityInfo["LocalizedName"]+"Info"] = cityInfo
        jsonList.append(cityInfo["LocalizedName"])
    #return json.dumps(jsonDict)
    '''
    
    getAlt = Rules.maiorAlt(jsonDict,jsonList)
    getIBGEs = Rules.getIbgeCode(jsonDict,jsonList,jsonState)
    cityInfo = {}
    for jl in jsonList:
        auxCity = db.findCity(jsonDict[jl+"Info"]["Key"]).fetchone()
        print(auxCity   )
        if(auxCity == None):
            cityInfo["name"] = jl
            cityInfo["altitude"] = getAlt[jl]
            cityInfo["weather_code"] = jsonDict[jl+"Info"]["Key"]
            cityInfo["ibge_code"] = getIBGEs[jl]
            db.insertCity(cityInfo)
        else:
            cityInfo = auxCity
    getPrecipitation = Rules.getPrecipitation(jsonDict,jsonList)
    print(getPrecipitation)
    for jl in jsonList:
        db.insertPrecipitation(getPrecipitation[jl])

    
   
    
    
    return json.dumps(jsonDict)
 
if __name__ == "__main__": 
    app.run()