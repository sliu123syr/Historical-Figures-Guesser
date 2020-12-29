
from graphics import*

class Record:
    def __init__(self,numberofguesses,numberofpeople):
        self.numberofguesses=numberofguesses
        self.numberofpeople=numberofpeople
    def plusoneguess(self):
        self.numberofguesses=self.numberofguesses+1
    def plusoneperson(self):
        self.numberofpeople=self.numberofpeople+1
    def display(self):
        return str("Number of Guesses:"+str(self.numberofguesses)+"\nNumber of People Discovered:"+str(self.numberofpeople))

player=Record(0,0)

def main():
    win=GraphWin("GuessTheFigure",600,800)  #(GW)
    win.setCoords(-300,-400,300,400)
    win.setBackground("white")
    outfile=open("historicalfigureslist.txt","r")
    listofsolutions=[]
    for line in outfile:
        line=line.replace("\n","")
        listofsolutions.append(str(line))
        player.plusoneguess()
        player.plusoneperson()
    game(win,listofsolutions)   #(FNC)

def game(win,listofsolutions):
    option=startmenu(win,listofsolutions)
    if option=="playgame":
        import random 
        numbers=[1,2,3,4,5,6,7]
        newnumbers = sorted(numbers,key=lambda x: random.random())  #(RND)
        for i in newnumbers:
            if i==1:
                first=profession(win)
            elif i==2:
                second=country(win)
            elif i==3:
                third=deathage(win)
            elif i==4:
                fourth=century(win)
            elif i==5:
                fifth=gender(win)
            elif i==6:
                sixth=death(win)
            elif i==7:
                seventh=ethnicity(win)
    infile=open("historicalfiguresinformation.txt","r") #(IFL)
    nameofperson="None"
    for line in infile:
        line=line.replace("-","")
        person=line.split("\t")
        if first==person[1] and second==person[2] and third==person[3] and fourth==person[4] and fifth==person[5] and sixth==person[6] and seventh==person[7]:
            nameofperson=person[0]
    infile.close()
    if nameofperson=="None":
        nosolution(win,listofsolutions)
    else:
        alreadylisted=False
        for i in listofsolutions:
            if i==nameofperson:
                alreadylisted=True
        if alreadylisted==False:
            listofsolutions.append(nameofperson)
        printoutfile(listofsolutions)
        solution(win,nameofperson,listofsolutions)

def printoutfile(listofsolutions):
        outfile=open("historicalfigureslist.txt","w")   #(OFL)
        for i in listofsolutions:
            print(i,file=outfile)
        outfile.close()
        
def startmenu(win,listofsolutions):
    introduction1=Text(Point(0,250),"Welcome!") #(OTXT)
    introduction2=Text(Point(0,225),"Think of a Historical figure or celebrity")
    introduction3=Text(Point(0,200),"Then click the button to begin")
    introduction1.draw(win)
    introduction2.draw(win)
    introduction3.draw(win)
    beginbutton=Rectangle(Point(-100,10),Point(100,110))
    resultsbutton=Rectangle(Point(-100,-110),Point(100,-10))
    beginbutton.draw(win)
    resultsbutton.draw(win)
    begintext=Text(Point(0,60),"Begin")
    resultstext=Text(Point(0,-60),"Show Results")
    begintext.draw(win)
    resultstext.draw(win)
    while True:
        clickpoint=win.getMouse()   #(IMS)
        if checkpoint(clickpoint,beginbutton)==True or checkpoint(clickpoint,resultsbutton):
            introduction1.undraw()
            introduction2.undraw()
            introduction3.undraw()
            beginbutton.undraw()
            begintext.undraw()
            resultsbutton.undraw()
            resultstext.undraw()
        if checkpoint(clickpoint,beginbutton)==True:
            return "playgame"
        elif checkpoint(clickpoint,resultsbutton)==True:
            showresults(win,listofsolutions)

def solution(win,nameofperson,listofsolutions):
    sentencetext=Text(Point(0,200),"The person that I'm thinking of is...")
    sentencetext.draw(win)
    nametext=Text(Point(0,150),nameofperson)
    nametext.setSize(36)
    nametext.draw(win)
    plagaintext=Text(Point(0,0),"Main Menu")
    plagaintext.draw(win)
    playagainbutton=Rectangle(Point(-100,-50),Point(100,50))
    playagainbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,playagainbutton)==True:
            sentencetext.undraw()
            nametext.undraw()
            plagaintext.undraw()
            playagainbutton.undraw()
            player.plusoneguess()
            player.plusoneperson()
            game(win,listofsolutions)

def nosolution(win,listofsolutions):
    sentencetext=Text(Point(0,200),"We were unable to find a solution.")
    sentencetext.setSize(20)
    sentencetext.draw(win)
    tryagaintext=Text(Point(0,0),"Main Menu")
    tryagaintext.draw(win)
    tryagainbutton=Rectangle(Point(-100,-50),Point(100,50))
    tryagainbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,tryagainbutton)==True:
            sentencetext.undraw()
            tryagaintext.undraw()
            tryagainbutton.undraw()
            player.plusoneguess()
            game(win,listofsolutions)

def showresults(win,listofsolutions):
    text=Text(Point(0,350),"Here are the figures that you have found:")
    text.draw(win)
    returntomenutext=Text(Point(0,-350),"Return to Main Menu")
    returntomenutext.draw(win)
    returntomenubutton=Rectangle(Point(-100,-375),Point(100,-325))
    returntomenubutton.draw(win)
    yvalue=300
    textofnames=Text(Point(0,0),"")
    recordtext=Text(Point(0,300),player.display())
    recordtext.draw(win)
    for i in listofsolutions:
        textsofar=textofnames.getText()
        textofnames.setText(textsofar+"\n"+i)
    textofnames.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,returntomenubutton)==True:
            text.undraw()
            returntomenutext.undraw()
            returntomenubutton.undraw()
            textofnames.undraw()
            recordtext.undraw()
            game(win,listofsolutions)
        
#-------------------------------------------------------------------------------
def profession(win):
    question=Text(Point(0,250),"What is your person's profession?")
    question.draw(win)
    leadertext=Text(Point(0,175),"Leader")
    soldiertext=Text(Point(0,115),"Soldier")
    scientisttext=Text(Point(0,55),"Scientist or Philosopher")
    humanitariantext=Text(Point(0,-5),"Humanitarian")
    explorertext=Text(Point(0,-65),"Explorer")
    athletetext=Text(Point(0,-125),"Athlete")
    businessmantext=Text(Point(0,-185),"Businessman")
    artisttext=Text(Point(0,-245),"Art and Literature (Click for more options)")
    leadertext.draw(win)
    soldiertext.draw(win)
    scientisttext.draw(win)
    humanitariantext.draw(win)
    explorertext.draw(win)
    athletetext.draw(win)
    businessmantext.draw(win)
    artisttext.draw(win)
    leaderbutton=Rectangle(Point(-200,150),Point(200,200))
    soldierbutton=Rectangle(Point(-200,90),Point(200,140))
    scientistbutton=Rectangle(Point(-200,30),Point(200,80))
    humanitarianbutton=Rectangle(Point(-200,-30),Point(200,20))
    explorerbutton=Rectangle(Point(-200,-90),Point(200,-40))
    athletebutton=Rectangle(Point(-200,-150),Point(200,-100))
    businessmanbutton=Rectangle(Point(-200,-210),Point(200,-160))
    artistbutton=Rectangle(Point(-200,-270),Point(200,-220))
    leaderbutton.draw(win)
    soldierbutton.draw(win)
    scientistbutton.draw(win)
    humanitarianbutton.draw(win)
    explorerbutton.draw(win)
    athletebutton.draw(win)
    businessmanbutton.draw(win)
    artistbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,leaderbutton)==True or checkpoint(clickpoint,soldierbutton)==True or checkpoint(clickpoint,scientistbutton)==True or checkpoint(clickpoint,humanitarianbutton) or checkpoint(clickpoint,explorerbutton) or checkpoint(clickpoint,athletebutton)==True or checkpoint(clickpoint,businessmanbutton)==True or checkpoint(clickpoint,artistbutton)==True:
            question.undraw()
            leadertext.undraw()
            soldiertext.undraw()
            scientisttext.undraw()
            humanitariantext.undraw()
            explorertext.undraw()
            athletetext.undraw()
            businessmantext.undraw()
            artisttext.undraw()
            leaderbutton.undraw()
            soldierbutton.undraw()
            scientistbutton.undraw()
            humanitarianbutton.undraw()
            explorerbutton.undraw()
            athletebutton.undraw()
            businessmanbutton.undraw()
            artistbutton.undraw()
        if checkpoint(clickpoint,leaderbutton)==True:
            job="Leader"
            return job
        elif checkpoint(clickpoint,soldierbutton)==True:
            job="Soldier"
            return job
        elif checkpoint(clickpoint,scientistbutton)==True:
            job="Scientist"
            return job
        elif checkpoint(clickpoint,humanitarianbutton)==True:
            job="Humanitarian"
            return job
        elif checkpoint(clickpoint,explorerbutton)==True:
            job="Explorer"
            return job
        elif checkpoint(clickpoint,athletebutton)==True:
            job="Athlete"
            return job
        elif checkpoint(clickpoint,businessmanbutton)==True:
            job="Businessman"
            return job
        elif checkpoint(clickpoint,artistbutton)==True:
            job=artprofession(win)
            return job

def artprofession(win):
    question=Text(Point(0,250),"What is your person's Art profession?")
    question.draw(win)
    paintertext=Text(Point(0,175),"Painter")
    writertext=Text(Point(0,115),"Writer")
    musiciantext=Text(Point(0,55),"Musician")
    actortext=Text(Point(0,-5),"Actor")
    paintertext.draw(win)
    writertext.draw(win)
    musiciantext.draw(win)
    actortext.draw(win)
    painterbutton=Rectangle(Point(-200,150),Point(200,200))
    writerbutton=Rectangle(Point(-200,90),Point(200,140))
    musicianbutton=Rectangle(Point(-200,30),Point(200,80))
    actorbutton=Rectangle(Point(-200,-30),Point(200,20))
    painterbutton.draw(win)
    writerbutton.draw(win)
    musicianbutton.draw(win)
    actorbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,painterbutton)==True or checkpoint(clickpoint,writerbutton)==True or checkpoint(clickpoint,musicianbutton)==True or checkpoint(clickpoint,actorbutton)==True:
            question.undraw()
            paintertext.undraw()
            writertext.undraw()
            musiciantext.undraw()
            actortext.undraw()
            painterbutton.undraw()
            writerbutton.undraw()
            musicianbutton.undraw()
            actorbutton.undraw()
        if checkpoint(clickpoint,painterbutton)==True:
            job="Painter"
            return job
        elif checkpoint(clickpoint,writerbutton)==True:
            job="Writer"
            return job
        elif checkpoint(clickpoint,musicianbutton)==True:
            job="Musician"
            return job
        elif checkpoint(clickpoint,actorbutton)==True:
            job="Actor"
            return job

#-------------------------------------------------------------------------------
def country(win):
    question=Text(Point(0,250),"What continent did your person's country exist in?")
    question.draw(win)
    northamericatext=Text(Point(0,175),"North America")
    southamericatext=Text(Point(0,115),"South America")
    europetext=Text(Point(0,55),"Europe")
    africatext=Text(Point(0,-5),"Africa")
    asiatext=Text(Point(0,-65),"Asia")
    australiatext=Text(Point(0,-125),"Australia")
    northamericatext.draw(win)
    southamericatext.draw(win)
    europetext.draw(win)
    africatext.draw(win)
    asiatext.draw(win)
    australiatext.draw(win)
    northamericabutton=Rectangle(Point(-200,150),Point(200,200))
    southamericabutton=Rectangle(Point(-200,90),Point(200,140))
    europebutton=Rectangle(Point(-200,30),Point(200,80))
    africabutton=Rectangle(Point(-200,-30),Point(200,20))
    asiabutton=Rectangle(Point(-200,-90),Point(200,-40))
    australiabutton=Rectangle(Point(-200,-150),Point(200,-100))
    northamericabutton.draw(win)
    southamericabutton.draw(win)
    europebutton.draw(win)
    africabutton.draw(win)
    asiabutton.draw(win)
    australiabutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,northamericabutton)==True or checkpoint(clickpoint,southamericabutton)==True or checkpoint(clickpoint,europebutton)==True or checkpoint(clickpoint,africabutton)==True or checkpoint(clickpoint,asiabutton)==True or checkpoint(clickpoint,australiabutton)==True:
            question.undraw()
            northamericatext.undraw()
            southamericatext.undraw()
            europetext.undraw()
            africatext.undraw()
            asiatext.undraw()
            australiatext.undraw()
            northamericabutton.undraw()
            southamericabutton.undraw()
            europebutton.undraw()
            africabutton.undraw()
            asiabutton.undraw()
            australiabutton.undraw()
        if checkpoint(clickpoint,northamericabutton)==True:
            nation=northamerica(win)
            return nation
        if checkpoint(clickpoint,southamericabutton)==True:
            nation=southamerica(win)
            return nation
        if checkpoint(clickpoint,europebutton)==True:
            nation=europe(win)
            return nation
        if checkpoint(clickpoint,africabutton)==True:
            nation=africa(win)
            return nation
        if checkpoint(clickpoint,asiabutton)==True:
            nation=asia(win)
            return nation
        if checkpoint(clickpoint,australiabutton)==True:
            nation="Australia"
            return nation

def northamerica(win):
    question=Text(Point(0,250),"What country in North America did your person live in?")
    question.draw(win)
    canadatext=Text(Point(0,175),"Canada")
    usatext=Text(Point(0,115),"United States of America")
    carribeantext=Text(Point(0,55),"Carribean Islands")
    mexicotext=Text(Point(0,-5),"Mexico")
    canadatext.draw(win)
    usatext.draw(win)
    carribeantext.draw(win)
    mexicotext.draw(win)
    canadabutton=Rectangle(Point(-200,150),Point(200,200))
    usabutton=Rectangle(Point(-200,90),Point(200,140))
    carribeanbutton=Rectangle(Point(-200,30),Point(200,80))
    mexicobutton=Rectangle(Point(-200,-30),Point(200,20))
    canadabutton.draw(win)
    usabutton.draw(win)
    carribeanbutton.draw(win)
    mexicobutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,canadabutton)==True or checkpoint(clickpoint,usabutton)==True or checkpoint(clickpoint,carribeanbutton)==True or checkpoint(clickpoint,mexicobutton)==True:
            question.undraw()
            canadatext.undraw()
            usatext.undraw()
            carribeantext.undraw()
            mexicotext.undraw()
            canadabutton.undraw()
            usabutton.undraw()
            carribeanbutton.undraw()
            mexicobutton.undraw()
        if checkpoint(clickpoint,canadabutton)==True:
            country="Canada"
            return country
        if checkpoint(clickpoint,usabutton)==True:
            country="USA"
            return country
        if checkpoint(clickpoint,carribeanbutton)==True:
            country="Carribean"
            return country
        if checkpoint(clickpoint,mexicobutton)==True:
            country="Mexico"
            return country

def southamerica(win):
    question=Text(Point(0,250),"What country in South America did your person live in?")
    question.draw(win)
    venezuelatext=Text(Point(0,175),"Venezula")
    braziltext=Text(Point(0,115),"Brazil")
    argentinatext=Text(Point(0,55),"Argentina")
    venezuelatext.draw(win)
    braziltext.draw(win)
    argentinatext.draw(win)
    venezuelabutton=Rectangle(Point(-200,150),Point(200,200))
    brazilbutton=Rectangle(Point(-200,90),Point(200,140))
    argentinabutton=Rectangle(Point(-200,30),Point(200,80))
    venezuelabutton.draw(win)
    brazilbutton.draw(win)
    argentinabutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,venezuelabutton)==True or checkpoint(clickpoint,brazilbutton)==True or checkpoint(clickpoint,argentinabutton)==True:
            question.undraw()
            venezuelatext.undraw()
            braziltext.undraw()
            argentinatext.undraw()
            venezuelabutton.undraw()
            brazilbutton.undraw()
            argentinabutton.undraw()
        if checkpoint(clickpoint,venezuelabutton)==True:
            country="Venezuela"
            return country
        if checkpoint(clickpoint,brazilbutton)==True:
            country="Brazil"
            return country
        if checkpoint(clickpoint,argentinabutton)==True:
            country="Argentina"
            return country

def europe(win):
    question=Text(Point(0,250),"What country in Europe did your person live in?")
    question.draw(win)
    germanytext=Text(Point(-102.5,175),"Germany")
    italytext=Text(Point(102.5,175),"Italy")
    greecetext=Text(Point(-102.5,115),"Greece")
    dutchtext=Text(Point(102.5,115),"Netherlands")
    swisstext=Text(Point(-102.5,55),"Switzerland")
    polandtext=Text(Point(102.5,55),"Poland")
    irelandtext=Text(Point(-102.5,-5),"Ireland")
    scandinaviatext=Text(Point(102.5,-5),"Scandinavia")
    francetext=Text(Point(-102.5,-65),"France")
    austriatext=Text(Point(102.5,-65),"Austria")
    scotlandtext=Text(Point(-102.5,-125),"Scotland")
    spaintext=Text(Point(102.5,-125),"Spain")
    portugaltext=Text(Point(-102.5,-185),"Portugal")
    englandtext=Text(Point(102.5,-185),"England")
    germanytext.draw(win)
    italytext.draw(win)
    greecetext.draw(win)
    dutchtext.draw(win)
    swisstext.draw(win)
    polandtext.draw(win)
    irelandtext.draw(win)
    scandinaviatext.draw(win)
    francetext.draw(win)
    austriatext.draw(win)
    scotlandtext.draw(win)
    spaintext.draw(win)
    portugaltext.draw(win)
    englandtext.draw(win)
    germanybutton=Rectangle(Point(-200,150),Point(-5,200))
    italybutton=Rectangle(Point(5,150),Point(200,200))
    greecebutton=Rectangle(Point(-200,90),Point(-5,140))
    dutchbutton=Rectangle(Point(5,90),Point(200,140))
    swissbutton=Rectangle(Point(-200,30),Point(-5,80))
    polandbutton=Rectangle(Point(5,30),Point(200,80))
    irelandbutton=Rectangle(Point(-200,-30),Point(-5,20))
    scandinaviabutton=Rectangle(Point(5,-30),Point(200,20))
    francebutton=Rectangle(Point(-200,-90),Point(-5,-40))
    austriabutton=Rectangle(Point(5,-90),Point(200,-40))
    scotlandbutton=Rectangle(Point(-200,-150),Point(-5,-100))
    spainbutton=Rectangle(Point(5,-150),Point(200,-100))
    portugalbutton=Rectangle(Point(-200,-210),Point(-5,-160))
    englandbutton=Rectangle(Point(5,-210),Point(200,-160))
    germanybutton.draw(win)
    italybutton.draw(win)
    greecebutton.draw(win)
    dutchbutton.draw(win)
    swissbutton.draw(win)
    polandbutton.draw(win)
    irelandbutton.draw(win)
    scandinaviabutton.draw(win)
    francebutton.draw(win)
    austriabutton.draw(win)
    scotlandbutton.draw(win)
    spainbutton.draw(win)
    portugalbutton.draw(win)
    englandbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,germanybutton)==True or checkpoint(clickpoint,italybutton)==True or checkpoint(clickpoint,greecebutton)==True or checkpoint(clickpoint,dutchbutton)==True or checkpoint(clickpoint,swissbutton)==True or checkpoint(clickpoint,polandbutton)==True or checkpoint(clickpoint,irelandbutton)==True or checkpoint(clickpoint,scandinaviabutton)==True or checkpoint(clickpoint,francebutton)==True or checkpoint(clickpoint,austriabutton)==True or checkpoint(clickpoint,scotlandbutton)==True or checkpoint(clickpoint,spainbutton)==True or checkpoint(clickpoint,portugalbutton)==True or checkpoint(clickpoint,englandbutton)==True:
            question.undraw()
            germanytext.undraw()
            italytext.undraw()
            greecetext.undraw()
            dutchtext.undraw()
            swisstext.undraw()
            polandtext.undraw()
            irelandtext.undraw()
            scandinaviatext.undraw()
            francetext.undraw()
            austriatext.undraw()
            scotlandtext.undraw()
            spaintext.undraw()
            portugaltext.undraw()
            englandtext.undraw()
            germanybutton.undraw()
            italybutton.undraw()
            greecebutton.undraw()
            dutchbutton.undraw()
            swissbutton.undraw()
            polandbutton.undraw()
            irelandbutton.undraw()
            scandinaviabutton.undraw()
            francebutton.undraw()
            austriabutton.undraw()
            scotlandbutton.undraw()
            spainbutton.undraw()
            portugalbutton.undraw()
            englandbutton.undraw()
        if checkpoint(clickpoint,germanybutton)==True:
            country="Germany"
            return country
        if checkpoint(clickpoint,italybutton)==True:
            country="Italy"
            return country
        if checkpoint(clickpoint,greecebutton)==True:
            country="Greece"
            return country
        if checkpoint(clickpoint,dutchbutton)==True:
            country="Dutch"
            return country
        if checkpoint(clickpoint,swissbutton)==True:
            country="Swiss"
            return country
        if checkpoint(clickpoint,polandbutton)==True:
            country="Poland"
            return country
        if checkpoint(clickpoint,irelandbutton)==True:
            country="Ireland"
            return country
        if checkpoint(clickpoint,scandinaviabutton)==True:
            country="Scandinavia"
            return country
        if checkpoint(clickpoint,francebutton)==True:
            country="France"
            return country
        if checkpoint(clickpoint,austriabutton)==True:
            country="Austria"
            return country
        if checkpoint(clickpoint,scotlandbutton)==True:
            country="Scotland"
            return country
        if checkpoint(clickpoint,spainbutton)==True:
            country="Spain"
            return country
        if checkpoint(clickpoint,portugalbutton)==True:
            country="Portugal"
            return country
        if checkpoint(clickpoint,englandbutton)==True:
            country="England"
            return country

def africa(win):
    question=Text(Point(0,250),"What country in Africa did your person live in?")
    question.draw(win)
    northafricatext=Text(Point(0,175),"North Africa")
    midafricatext=Text(Point(0,115),"Mid Africa")
    southafricatext=Text(Point(0,55),"South Africa")
    northafricatext.draw(win)
    midafricatext.draw(win)
    southafricatext.draw(win)
    northafricabutton=Rectangle(Point(-200,150),Point(200,200))
    midafricabutton=Rectangle(Point(-200,90),Point(200,140))
    southafricabutton=Rectangle(Point(-200,30),Point(200,80))
    northafricabutton.draw(win)
    midafricabutton.draw(win)
    southafricabutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,northafricabutton)==True or checkpoint(clickpoint,midafricabutton)==True or checkpoint(clickpoint,southafricabutton)==True:
            question.undraw()
            northafricatext.undraw()
            midafricatext.undraw()
            southafricatext.undraw()
            northafricabutton.undraw()
            midafricabutton.undraw()
            southafricabutton.undraw()
        if checkpoint(clickpoint,northafricabutton)==True:
            country="NorthAfrica"
            return country
        if checkpoint(clickpoint,midafricabutton)==True:
            country="MidAfrica"
            return country
        if checkpoint(clickpoint,southafricabutton)==True:
            country="SouthAfrica"
            return country

def asia(win):
    question=Text(Point(0,250),"What country in Asia did your person live in?")
    question.draw(win)
    russiatext=Text(Point(0,175),"Russia")
    japantext=Text(Point(0,115),"Japan")
    indiatext=Text(Point(0,55),"India")
    chinatext=Text(Point(0,-5),"China")
    tibettext=Text(Point(0,-65),"Tibet")
    pakistantext=Text(Point(0,-125),"Pakistan")
    koreatext=Text(Point(0,-185),"Korea")
    russiatext.draw(win)
    japantext.draw(win)
    indiatext.draw(win)
    chinatext.draw(win)
    tibettext.draw(win)
    pakistantext.draw(win)
    koreatext.draw(win)
    russiabutton=Rectangle(Point(-200,150),Point(200,200))
    japanbutton=Rectangle(Point(-200,90),Point(200,140))
    indiabutton=Rectangle(Point(-200,30),Point(200,80))
    chinabutton=Rectangle(Point(-200,-30),Point(200,20))
    tibetbutton=Rectangle(Point(-200,-90),Point(200,-40))
    pakistanbutton=Rectangle(Point(-200,-150),Point(200,-100))
    koreabutton=Rectangle(Point(-200,-210),Point(200,-160))
    russiabutton.draw(win)
    japanbutton.draw(win)
    indiabutton.draw(win)
    chinabutton.draw(win)
    tibetbutton.draw(win)
    pakistanbutton.draw(win)
    koreabutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,russiabutton)==True or checkpoint(clickpoint,japanbutton)==True or checkpoint(clickpoint,indiabutton)==True or checkpoint(clickpoint,chinabutton) or checkpoint(clickpoint,tibetbutton) or checkpoint(clickpoint,pakistanbutton)==True or checkpoint(clickpoint,koreabutton)==True:
            question.undraw()
            russiatext.undraw()
            japantext.undraw()
            indiatext.undraw()
            chinatext.undraw()
            tibettext.undraw()
            pakistantext.undraw()
            koreatext.undraw()
            russiabutton.undraw()
            japanbutton.undraw()
            indiabutton.undraw()
            chinabutton.undraw()
            tibetbutton.undraw()
            pakistanbutton.undraw()
            koreabutton.undraw()
        if checkpoint(clickpoint,russiabutton)==True:
            country="Russia"
            return country
        elif checkpoint(clickpoint,japanbutton)==True:
            country="Japan"
            return country
        elif checkpoint(clickpoint,indiabutton)==True:
            country="India"
            return country
        elif checkpoint(clickpoint,chinabutton)==True:
            country="China"
            return country
        elif checkpoint(clickpoint,tibetbutton)==True:
            country="Tibet"
            return country
        elif checkpoint(clickpoint,pakistanbutton)==True:
            country="Pakistan"
            return country
        elif checkpoint(clickpoint,koreabutton)==True:
            country="Korea"
            return country

#-------------------------------------------------------------------------------
def deathage(win):
    question1=Text(Point(0,250),"How old is your person as of Dec. 2019?")
    question2=Text(Point(0,225),"If your person is dead, enter their age when they died")
    question3=Text(Point(0,200),"Enter the age in the box in integers, then hit CONTINUE")
    question1.draw(win)
    question2.draw(win)
    question3.draw(win)
    deathageentry=Entry(Point(0,150),5)
    deathageentry.draw(win)
    deathageentry.setFill("white")
    continuetext=Text(Point(0,75),"Continue")
    continuetext.draw(win)
    continuebutton=Rectangle(Point(-100,50),Point(100,100))
    continuebutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,continuebutton)==True:
            ageatdeath=deathageentry.getText()  #(IEB)
            question1.undraw()
            question2.undraw()
            question3.undraw()
            deathageentry.undraw()
            continuetext.undraw()
            continuebutton.undraw()
            return ageatdeath

#-------------------------------------------------------------------------------
def century(win):
    question1=Text(Point(0,250),"In what century did your person live in? (Enter BC for any century before the first)")
    question2=Text(Point(0,225),"If your person lived in multiple centuries, choose the one he/she was born in")
    question3=Text(Point(0,200),"Enter the century in the box in integers, then hit CONTINUE")
    question1.draw(win)
    question2.draw(win)
    question3.draw(win)
    centuryentry=Entry(Point(0,150),5)
    centuryentry.draw(win)
    centuryentry.setFill("white")
    continuetext=Text(Point(0,75),"Continue")
    continuetext.draw(win)
    continuebutton=Rectangle(Point(-100,50),Point(100,100))
    continuebutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,continuebutton)==True:
            century=centuryentry.getText()
            question1.undraw()
            question2.undraw()
            question3.undraw()
            centuryentry.undraw()
            continuetext.undraw()
            continuebutton.undraw()
            return century

#-------------------------------------------------------------------------------
def gender(win):
    question=Text(Point(0,250),"Is your person a male or a female?")
    question.draw(win)
    maletext=Text(Point(0,175),"Male")
    femaletext=Text(Point(0,115),"Female")
    maletext.draw(win)
    femaletext.draw(win)
    malebutton=Rectangle(Point(-200,150),Point(200,200))
    femalebutton=Rectangle(Point(-200,90),Point(200,140))
    malebutton.draw(win)
    femalebutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,malebutton)==True or checkpoint(clickpoint,femalebutton)==True:
            question.undraw()
            maletext.undraw()
            femaletext.undraw()
            malebutton.undraw()
            femalebutton.undraw()
        if checkpoint(clickpoint,malebutton)==True:
            gender="Male"
            return gender
        elif checkpoint(clickpoint,femalebutton)==True:
            gender="Female"
            return gender

#-------------------------------------------------------------------------------
def death(win):
    question=Text(Point(0,250),"Is your person still alive?")
    question.draw(win)
    alivetext=Text(Point(0,175),"Yes")
    deadtext=Text(Point(0,115),"No")
    alivetext.draw(win)
    deadtext.draw(win)
    alivebutton=Rectangle(Point(-200,150),Point(200,200))
    deadbutton=Rectangle(Point(-200,90),Point(200,140))
    alivebutton.draw(win)
    deadbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,alivebutton)==True or checkpoint(clickpoint,deadbutton)==True:
            question.undraw()
            alivetext.undraw()
            deadtext.undraw()
            alivebutton.undraw()
            deadbutton.undraw()
        if checkpoint(clickpoint,alivebutton)==True:
            death="Alive"
            return death
        elif checkpoint(clickpoint,deadbutton)==True:
            death=deathcondition(win)
            return death

def deathcondition(win):
    question=Text(Point(0,250),"How did your person die?")
    question.draw(win)
    wartext=Text(Point(0,175),"War")
    assasinationtext=Text(Point(0,115),"Assasination")
    suicidetext=Text(Point(0,55),"Suicide")
    diseasetext=Text(Point(0,-5),"Disease")
    executiontext=Text(Point(0,-65),"Execution")
    accidenttext=Text(Point(0,-125),"Accident")
    unknowntext=Text(Point(0,-185),"Unknown")
    wartext.draw(win)
    assasinationtext.draw(win)
    suicidetext.draw(win)
    diseasetext.draw(win)
    executiontext.draw(win)
    accidenttext.draw(win)
    unknowntext.draw(win)
    warbutton=Rectangle(Point(-200,150),Point(200,200))
    assasinationbutton=Rectangle(Point(-200,90),Point(200,140))
    suicidebutton=Rectangle(Point(-200,30),Point(200,80))
    diseasebutton=Rectangle(Point(-200,-30),Point(200,20))
    executionbutton=Rectangle(Point(-200,-90),Point(200,-40))
    accidentbutton=Rectangle(Point(-200,-150),Point(200,-100))
    unknownbutton=Rectangle(Point(-200,-210),Point(200,-160))
    warbutton.draw(win)
    assasinationbutton.draw(win)
    suicidebutton.draw(win)
    diseasebutton.draw(win)
    executionbutton.draw(win)
    accidentbutton.draw(win)
    unknownbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,warbutton)==True or checkpoint(clickpoint,assasinationbutton)==True or checkpoint(clickpoint,suicidebutton)==True or checkpoint(clickpoint,diseasebutton) or checkpoint(clickpoint,executionbutton)==True or checkpoint(clickpoint,accidentbutton)==True or checkpoint(clickpoint,unknownbutton)==True:
            question.undraw()
            wartext.undraw()
            assasinationtext.undraw()
            suicidetext.undraw()
            diseasetext.undraw()
            executiontext.undraw()
            accidenttext.undraw()
            unknowntext.undraw()
            warbutton.undraw()
            assasinationbutton.undraw()
            suicidebutton.undraw()
            diseasebutton.undraw()
            executionbutton.undraw()
            accidentbutton.undraw()
            unknownbutton.undraw()
        if checkpoint(clickpoint,warbutton)==True:
            deathcondition="War"
            return deathcondition
        elif checkpoint(clickpoint,assasinationbutton)==True:
            deathcondition="Assasination"
            return deathcondition
        elif checkpoint(clickpoint,suicidebutton)==True:
            deathcondition="Suicide"
            return deathcondition
        elif checkpoint(clickpoint,diseasebutton)==True:
            deathcondition="Disease"
            return deathcondition
        elif checkpoint(clickpoint,executionbutton)==True:
            deathcondition="Execution"
            return deathcondition
        elif checkpoint(clickpoint,accidentbutton)==True:
            deathcondition="Accident"
            return deathcondition
        elif checkpoint(clickpoint,unknownbutton)==True:
            deathcondition="Unknown"
            return deathcondition

#-------------------------------------------------------------------------------
def ethnicity(win):
    question=Text(Point(0,250),"What is your person's ethnicity?")
    question.draw(win)
    whitetext=Text(Point(0,175),"White")
    latinotext=Text(Point(0,115),"Latino")
    asiantext=Text(Point(0,55),"Asian")
    jewishtext=Text(Point(0,-5),"Jewish")
    blacktext=Text(Point(0,-65),"Black")
    whitetext.draw(win)
    latinotext.draw(win)
    asiantext.draw(win)
    jewishtext.draw(win)
    blacktext.draw(win)
    whitebutton=Rectangle(Point(-200,150),Point(200,200))
    latinobutton=Rectangle(Point(-200,90),Point(200,140))
    asianbutton=Rectangle(Point(-200,30),Point(200,80))
    jewishbutton=Rectangle(Point(-200,-30),Point(200,20))
    blackbutton=Rectangle(Point(-200,-90),Point(200,-40))
    whitebutton.draw(win)
    latinobutton.draw(win)
    asianbutton.draw(win)
    jewishbutton.draw(win)
    blackbutton.draw(win)
    while True:
        clickpoint=win.getMouse()
        if checkpoint(clickpoint,whitebutton)==True or checkpoint(clickpoint,latinobutton)==True or checkpoint(clickpoint,asianbutton)==True or checkpoint(clickpoint,jewishbutton) or checkpoint(clickpoint,blackbutton)==True:
            question.undraw()
            whitetext.undraw()
            latinotext.undraw()
            asiantext.undraw()
            jewishtext.undraw()
            blacktext.undraw()
            whitebutton.undraw()
            latinobutton.undraw()
            asianbutton.undraw()
            jewishbutton.undraw()
            blackbutton.undraw()
        if checkpoint(clickpoint,whitebutton)==True:
            ethnicity="White"
            return ethnicity
        elif checkpoint(clickpoint,latinobutton)==True:
            ethnicity="Latino"
            return ethnicity
        elif checkpoint(clickpoint,asianbutton)==True:
            ethnicity="Asian"
            return ethnicity
        elif checkpoint(clickpoint,jewishbutton)==True:
            ethnicity="Jewish"
            return ethnicity
        elif checkpoint(clickpoint,blackbutton)==True:
            ethnicity="Black"
            return ethnicity
        
#-------------------------------------------------------------------------------
def checkpoint(point,button):
    ll=button.getP1()
    ur=button.getP2()
    if ll.getX()<point.getX()<ur.getX() and ll.getY()<point.getY()<ur.getY():
        result=True
    else:
        result=False
    return result



main()
