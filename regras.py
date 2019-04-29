import requests as rq
import unicodedata
def maiorAlt(jsonDict,jsonList):   
    maiorAltName = ""
    maiorAlt = 0
    jReturn = {}
    for jl in jsonList:
        auxAlt = jsonDict[jl+"Info"]["GeoPosition"]["Elevation"]["Metric"]["Value"]
        jReturn[jl] = auxAlt
        if(maiorAlt < auxAlt):
            maiorAltName = jl
            maiorAlt = auxAlt
            
        

    jReturn["Cidade"] = maiorAltName
    jReturn["Altitude"] = maiorAlt
    
    return jReturn
    

def getIbgeCode(jsonDict,jsonList,jsonState):
    menorPop = -1
    menorPopName = ""
    jReturn = {}
    for i in range(0,len(jsonState)):
        states = rq.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()
        for state in states:
            if state["sigla"] == jsonState[i]:
                stateCod = state["id"]
        cities = rq.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+str(stateCod)+"/municipios").json()
        for city in cities:
            if city["nome"] == jsonList[i]:
                cityCod = city["id"]
        getPop = rq.get("https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/"+str(cityCod)).json()["projecao"]["populacao"]
        
        jReturn[jsonList[i]] = cityCod
        
    return jReturn

def getPrecipitation(jsonDict,jsonList):
    jPrep = {}
    for jl in jsonList:
        print(jl)
        jPrep[jl] = {}
        jPrep[jl]["Date"] = jsonDict[jl+"Temp"]["LocalObservationDateTime"]
        if jsonDict[jl+"Temp"]["HasPrecipitation"] == True:
            if jsonDict[jl+"Temp"]["PrecipitationType"] == "Rain":
                jPrep[jl]["Precipitation"] = 10
            else:
                jPrep[jl]["Precipitation"] = 5
        else:
            jPrep[jl]["Precipitation"] = 0
        jPrep[jl]["weather_code"] = jsonDict[jl+"Info"]["Key"]
    return jPrep



    '''
        getIbgeCode = rq.get("https://viacep.com.br/ws/"+jsonState[i]+"/"+jsonList[i]+"/brasil/json/").json()[0]["ibge"]
 
        getPop = rq.get("https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/"+getIbgeCode).json()["projecao"]["populacao"]
        if menorPop == -1:
            menorPop = getPop
            menorPopName = jsonList[i]
        elif getPop < menorPop:
            menorPop = getPop
            menorPopName = jsonList[i]
    jReturn = {}
    jReturn["Cidade"] = menorPopName
    jReturn["Populacao"] = menorPop
    return jReturn'''
