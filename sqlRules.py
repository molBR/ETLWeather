import pyodbc 
class DataBase:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-MF6GBN4R;'
                        'Database=StoneDatabase;'
                        'Trusted_Connection=yes;')

    def insertCity(self,cityInfo):
        SQLCommand = ("INSERT INTO StoneDatabase.dbo.CITY "
                 "(weather_code, ibge_code, altitude, name) "
                 "VALUES (?,?,?,?)")
        cursor = self.conn.cursor()
        arrayInfo = [cityInfo["weather_code"],cityInfo["ibge_code"],cityInfo["altitude"],cityInfo["name"]]
        cursor.execute(SQLCommand,arrayInfo) 
        self.conn.commit()

    def findCity(self,weather_code):
        SQLCommand = ("SELECT * FROM StoneDatabase.dbo.CITY WHERE weather_code = "+str(weather_code)) 
        cursor = self.conn.cursor()
        cursor.execute(SQLCommand)
        return cursor
    
    def insertPrecipitation(self, precipitation):
        print(precipitation)
        SQLCommand = ("INSERT INTO StoneDatabase.dbo.PRECIPITATION2 "
            "(date, precipitation, weather_code) "
            "VALUES (?,?,?)")
        cursor = self.conn.cursor() 
        arrayInfo = [precipitation["Date"],precipitation["Precipitation"],precipitation ["weather_code"]]
        cursor.execute(SQLCommand,arrayInfo)
        print(cursor.fetchone())
        return cursor
