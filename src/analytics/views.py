# from asyncio.windows_events import NULL
from curses.ascii import HT
from django.shortcuts import HttpResponse, render
from .models import*
import pandas as pd
import json
#from django.views.generic import TemplateView # Import TemplateView

# Create your views here.
def index(request):
    #return render(request, 'home.html')
    return render(request, 'chooseForm.html')

def chooseForm(request):
    #print(request.POST)
    choice = request.POST.get('optradio')
    if choice=='option1':
        return render(request, 'home.html')
    else:
        return render(request, 'form2.html')

# for first form
def query(request):
    #declare all the form data
    if request.method == "POST":
        stat_choice = request.POST.get('optradio')
        # ppg = request.POST.get('PPG')
        # apg = request.POST.get('APG')
        # rpg = request.POST.get('RPG')
        # spg = request.POST.get('SPG')
        # bpg = request.POST.get('BPG')
        # _3pp = request.POST.get('3P%')
        # _2pp = request.POST.get('2P%')
        # fgp = request.POST.get('FG%') # not working
        # ofrtg = request.POST.get('OFRTG') #not working
        # dfrtg = request.POST.get('DFRTG') #not working
        team = request.POST.get('teamName')

    print(team)
    # array of all team names, used to check for valid team name
    teamNamess=["knicks", "lakers", "clippers", "sixers", "76ers", 
    "hawks", "raptors", "celtics", "bucks", "hornets", "pelicans", "spurs", "trailblazers", "trail blazers",
    "wolves", "timberwolves", "jazz", "bulls", "wizards", "rockets", "magic", "heat",
    "grizzlies", "pacers", "cavs", "cavaliers", "suns", "warriors", "thunder", "kings",
    "nuggets", "mavericks", "mavs", "pistons"]
    
    # check for valid team name
    team_checker2 = 0
    if team!="":
        team_checker = 0
        for i in range(len(teamNamess)):
            if(team==teamNamess[i]):
                team_checker=1
                team_checker2=1
        if team_checker==0:
            return HttpResponse("Invalid team name")
    
    #initialize the dataframe to be returned to page
    item = Player.objects.all().values()   
    df = pd.DataFrame(item)

    team_dest=""
    #handling teams
    if team_checker2==1:
        #match team
        if (team=="knicks"):
            team_dest="Nyk"
        if (team=="lakers"):
            team_dest="Lal"
        if (team=="clippers"):
            team_dest="Lac"
        if (team=="sixers" or team=="76ers"):
            team_dest="Phi"
        if (team=="hawks"):
            team_dest="Atl"
        if (team=="raptors"):
            team_dest="Tor"
        if (team=="celtics"):
            team_dest="Bos"
        if (team=="bucks"):
            team_dest="Mil"
        if (team=="hornets"):
            team_dest="Cha"
        if (team=="pelicans"):
            team_dest="Nor"
        if (team=="spurs"):
            team_dest="San"
        if (team=="trail blazers" or team=="trailblazers"):
            team_dest="Por"
        if (team=="wolves" or team=="timberwolves"):
            team_dest="Lac"
        if (team=="jazz"):
            team_dest="Uta"
        if (team=="bulls"):
            team_dest="Chi"
        if (team=="wizards"):
            team_dest="Was"
        if (team=="rockets"):
            team_dest="Hou"
        if (team=="magic"):
            team_dest="Orl"
        if (team=="heat"):
            team_dest="Mia"
        if (team=="grizzlies"):
            team_dest="Mem"
        if (team=="pacers"):
            team_dest="Ind"
        if (team=="cavs" or team=="cavaliers"):
            team_dest="Cle"
        if (team=="suns"):
            team_dest="Pho"
        if (team=="warriors"):
            team_dest="Gol"
        if (team=="thunder"):
            team_dest="Okc"
        if (team=="kings"):
            team_dest="Sac"
        if (team=="nuggets"):
            team_dest="Den"
        if (team=="mavericks" or team=="mavs"):
            team_dest="Dal"
        if (team=="pistons"):
            team_dest="Det"
    
        # print(2)
        # df1=df[df['team']==team_dest]
        # mydict = {
        #     "df": df1.to_html()
        # }
        # return render(request, 'home.html', context=mydict)
        

    _ppg=0
    _apg=0 
    _rpg=0 
    _spg=0 
    _bpg=0 
    __3pp=0 
    __2pp=0 
    _fgp=0 
    _ofrtg=0 
    _dfrtg=0
    print(stat_choice)
    if stat_choice=="option1":
        _ppg=1
    if stat_choice=="option2":
        _apg=1
    if stat_choice=="option3":
        _rpg=1
    if stat_choice=="option4":
        _spg=1
    if stat_choice=="option5":
        _bpg=1
    if stat_choice=="option6":
        __3pp=1
    if stat_choice=="option7":
        __2pp=1
    # if fgp:
    #     _fgp=1
    # if ofrtg:
    #     _ofrtg=1
    # if dfrtg:
    #     _dfrtg=1
    
    #if nothing is requested other than submit button
    if (_ppg+_apg+_rpg+_spg+_bpg+__3pp+__2pp+_fgp+_ofrtg+_dfrtg)==0 and team_checker2==0:
        return render(request, 'home.html')
    
    #ppg
    if _ppg==1:
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['pointsPerGame'])
            # mydict = {
            #     "df": df2.to_html()
            # }
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    ##apg
    if _apg==1:
        print(111)
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    #rpg
    if _rpg==1:
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)
    
    #spg
    if _spg==1:
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['stealPerGame'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    #bpg
    if _bpg==1:
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    #3pp
    if __3pp==1:
        df2 = df[df["threePointAttempts"]> 150]
        if team_checker2==1:
            df1=df2[df2['team']==team_dest]
            df3= df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df3.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df2.nlargest(n=10,columns=['threePointPercent'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    #2pp
    if __2pp==1:
        if team_checker2==1:
            df1=df[df['team']==team_dest]
            df2= df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        else:
            df1=df.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df1.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
        return render(request, 'home.html', context)

    #fgp
    # if _fgp==1:
    #     # df1=df.nlargest(n=10,columns=['fieldGoalPercent'])
    #     #df['fieldGoalPercent'] = df['fieldGoalPercent'].astype(float)
    #     df1=df.astype(str).astype(float).nlargest(n=10,columns=['fieldGoalPercent'])
    #     mydict = {
    #         "df": df1.to_html()
    #     }
    #     return render(request, 'home.html', context=mydict)

    # #off rtg
    # if _ofrtg==1:
    #     df1=df.nlargest(n=10,columns=['offrtg'])
    #     mydict = {
    #         "df": df1.to_html()
    #     }
    #     return render(request, 'home.html', context=mydict)

    # #def rtg
    # if _dfrtg==1:
    #     df1=df.nlargest(n=10,columns=['defrtg'])
    #     mydict = {
    #         "df": df1.to_html()
    #     }
    #     return render(request, 'home.html', context=mydict)

    #offrtg, defrtg, and fg% don't work bc dtype object ...
    # if team=="knicks":
    return render(request, 'home.html')


# second form
def query2(request):
    if request.method == "POST":
        print(request.POST.get("optradio"))
        stat_1 = request.POST.get("optradio")
        stat_2 = request.POST.get('optradio1')

        ppg1=False
        apg1=False
        rpg1=False
        spg1=False
        bpg1=False
        _3pp1=False
        _2pp1=False
        fgp1=False
        ofrtg1=False
        dfrtg1=False

        _ppg1=False
        _apg1=False
        _rpg1=False
        _spg1=False
        _bpg1=False
        __3pp1_=False
        __2pp1_=False
        notFilled=0
        #first stat to compare
        if stat_1=="option1":
            notFilled+=1
            ppg1=True
        if stat_1=="option2":
            notFilled+=1
            apg1=True
        if stat_1=="option3":
            notFilled+=1
            rpg1=True
        if stat_1=="option4":
            notFilled+=1
            spg1=True
        if stat_1=="option5":
            notFilled+=1
            bpg1=True
        if stat_1=="option6":
            notFilled+=1
            _3pp1=True
        if stat_1=="option7":
            notFilled+=1
            _2pp1=True
        if stat_1=="option8":
            notFilled+=1
            fgp1=True
        if stat_1=="option9":
            notFilled+=1
            ofrtg1=True
        if stat_1=="option10":
            notFilled+=1
            dfrtg1=True
        #number
        val = int(request.POST.get('value_'))
        print(val)
        #second stat (to find leaders in)
        if stat_2=="option11":
            notFilled+=1
            _ppg1=True
        if stat_2=="option22":
            notFilled+=1
            _apg1=True
        if stat_2=="option33":
            notFilled+=1
            _rpg1=True
        if stat_2=="option44":
            notFilled+=1
            _spg1=True
        if stat_2=="option55":
            notFilled+=1
            _bpg1=True
        if stat_2=="option66":
            notFilled+=1
            __3pp1_=True
        if stat_2=="option77":
            notFilled+=1
            __2pp1_=True
        
        print(request.POST.get('optradio1'))
    if(notFilled!=2):
        return render(request, 'form2.html')

        # fgp2 = request.POST.get('FG%1') # not working
        # ofrtg2 = request.POST.get('OFRTG1') #not working
        # dfrtg2 = request.POST.get('DFRTG1') #not working

    check1=0
    point1=0
    assists1=0 
    rebounds1=0 
    steal1=0 
    blocks1=0 
    threePoint1=0 
    twoPoint1=0 
    fieldGoal1=0 
    offRating1=0 
    defRating1=0
    #if stat1
    point2=0
    assists2=0 
    rebounds2=0 
    steal2=0 
    blocks2=0 
    threePoint2=0 
    twoPoint2=0 
    # fieldGoal2=0 
    # offRating2=0 
    # defRating2=0

    check5 = 0
    check6 = 0
    check7 = 0
    if val>=0:
        check5=1

    if check1==0:
        if ppg1:
            point1=1
            check6=1
        if apg1:
            assists1=1
            check6+=1
        if rpg1:
            rebounds1=1
            check6+=1
        if spg1:
            steal1=1
            check6+=1
        if bpg1:
            blocks1=1
            check6+=1
        if _3pp1:
            threePoint1=1
            check6+=1
        if _2pp1:
            twoPoint1=1
            check6+=1
        if fgp1:
            fieldGoal1=1
            check6+=1
        if ofrtg1:
            offRating1=1
            check6+=1
        if dfrtg1:
            defRating1=1
            check6+=1

    if check1==0:
        if _ppg1:
            point2=1
            check7=1
        if _apg1:
            assists2=1
            check7+=1
        if _rpg1:
            rebounds2=1
            check7+=1
        if _spg1:
            steal2=1
            check7+=1
        if _bpg1:
            blocks2=1
            check7+=1
        if __3pp1_:
            threePoint2=1
            check7+=1
        if __2pp1_:
            twoPoint2=1
            check7+=1
    
    item = Player.objects.all().values()   
    df = pd.DataFrame(item)

    if check5!=1 and check6!=1 and check7!=1:
        return HttpResponse("Must select a stat for the first stat option, enter a value, and select another stat for the third option")

    #point1 true
    if point1==1:
        if point2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["pointsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
    
    #assists1 true

    if assists1==1:
        if point2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["assistsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #rebounds1 true
    if rebounds1==1:
        if point2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["reboundsPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #steals1 true
    if steal1==1:
        if point2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["stealPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #blocks1 true
    if blocks1==1:
        if point2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["blocksPerGame"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["blocksPerGame"]>val]
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #2point percent true
    if twoPoint1==1:
        if point2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["twoPointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #3point percent true 
    if threePoint1==1:
        if point2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["threePointPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #offrtg1 true 
    if offRating1==1:
        if point2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            mydict = {
                "df": df2.to_html()
            }
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["offrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #defrtg1 true
    if defRating1==1:
        if point2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["defrtg"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)

    #fg1 true
    if fieldGoal1==1:
        if point2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['pointsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if assists2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['assistsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if rebounds2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['reboundsPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if steal2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['stealPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if blocks2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['blocksPerGame'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if threePoint2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['threePointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)
        if twoPoint2==1:
            df1= df[df["fieldGoalPercent"]>val]
            df2 = df1.nlargest(n=10,columns=['twoPointPercent'])
            json_records = df2.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            return render(request, 'form2.html', context)



    print(ppg1)
    return render(request, 'form2.html')


    #return HttpResponse("Invalid input: type either '1' or '2'")