class calc:
    def getDetail(self):
        self.total_computer=258
        self.total_hour=6
    def calculatesecondsperDay(self):
        Second_per_Day=self.total_hour*60*60
        print('Total Seconds per Day:',Second_per_Day)
    def calculateminutesperWeek(self):
        Minutes_per_Week=self.total_hour*60*7
        print("Total Minutes per Week:",Minutes_per_Week)
    def calculatehourperMonth(self):
        Hour_per_Month=self.total_hour*30
        print("Total Hour per Month:",Hour_per_Month)
    def calculatedayperyear(self):
        Day_per_Year=(self.total_hour*365)/24  
        print("Total Day per Year:",Day_per_Year)
to=calc()
to.getDetail()
to.calculatesecondsperDay()
to.calculateminutesperWeek()
to.calculatehourperMonth()
to.calculatedayperyear()
