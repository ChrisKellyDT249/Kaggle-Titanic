__author__ = 'Chris'

'''
PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare,Cabin, Embarked
Step 1) Split data into Survived & Died
Step 2) Identify characteristics for each group
Step 3) Identify inter-relationships between characteristics for each group
Step 4) i) Set % chance for each characteristic
        ii) Set % for inter-related characteristics

Main Identifiers
    Pclass   - pclass_surv, pclass_decd
    Sex
    Embarked
    Fare(?)
All Identifiers
PassengerID
Survival        (0 = No; 1 = Yes)
pclass          Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton

this version - reducing identifiers to minimal
'''

def openfile():
    training_file = open("train.csv", "r")
    return training_file

def analysedata(training_file):
    #======================================================
    # Variables Declarations - Survivors
    #=====================================================
    passenger_count = 0
    age_surv = 0
    ave_age_surv = 0
    age_surv_null = 0
    tot_surv = 0 # calc % survival rate overall for info
    pclass_surv = {} # key is class number, value is % surv
    sex_surv = {} # ditto
    age_surv = {"14":0 , "30":0 , "50":0, "Null":0} # split into 3 groups
    count_ave_age_surv = 0
    embarked_surv = {"C":0 , "Q":0 , "S":0, "Null":0}
    # values for counting
    error_line = 0
    passenger_count = 0
    #===================================================
    # Variables Declarations - Deceased
    #===================================================
    tot_decd = 0
    age_decd = 0
    ave_age_decd = 0
    age_decd_null = 0
    pclass_decd = {} # key is class number, value is % decd
    sex_decd = {} # ditto
    age_decd = {"14":0 , "30":0 , "50":0, "Null":0} # split into 3 groups
    count_ave_age_decd = 0
    embarked_decd = {"C":0 , "Q":0 , "S":0, "Null":0}


    #===================================================
    # update stats based on survivor
    #===================================================
    for line in training_file:
        passenger_count += 1
        line = line.split(",")
        # survivor stats
        try:
            if line[1] == "1":
                tot_surv += 1
                try:
                    if int(line[5]) != 0:
                        age_surv += int(line[5])
                    else:
                        age_surv_null += 1
                except:
                    print("internal loop bad line")
                if line[2] in pclass_surv:
                        pclass_surv[line[2]] += 1
                else:
                    pclass_surv[line[2]] = 1
                if int(line[5]) == 0:
                    pclass_surv["Null"] += 1
                if int(line[5]) < 15:
                    pclass_surv["14"] += 1
                elif int(line[5]) < 31:
                    pclass_surv["30"] += 1
                elif int(line[5])> 50:
                    pclass_surv["50"] += 1
                if line[4] in sex_surv:
                    sex_surv[line[4]] += 1
                else:
                    sex_surv[line[4]] = 1
                if line[-1] in embarked_surv:
                    embarked_surv[line[-1]] += 1
                else:
                    embarked_surv[line[-1]] = 1
            else:
                if int(line[5]) != 0:
                    age_decd += int(line[5])
                else:
                    age_decd_null += 1
                if line[2] in pclass_decd:
                    pclass_decd[line[2]] += 1
                else:
                    pclass_decd[line[2]] = 1
                if int(lin[5])== 0:
                    pclass_decd["Null"] += 1
                if int(line[5]) < 15:
                    pclass_decd["14"] += 1
                elif int(line[5]) < 31:
                    pclass_decd["30"] += 1
                elif int(line[5])> 50:
                    pclass_decd["50"] += 1
                if line[4] in sex_surv:
                    sex_decd[line[4]] += 1
                else:
                    sex_decd[line[4]] = 1
                if line[-1] in embarked_decd:
                    embarked_decd[line[-1]] += 1
                else:
                    embarked_decd[line[-1]] = 1
        except:
            print("bad line", passenger_count)
#=================================================
    # Calculate survival rates & probabilities
#=================================================
    ave_age_surv = age_surv / tot_surv
    ave_age_decd = age_decd / tot_decd

    for cls in pclass_surv:
        try:
            cls_prop[cls] = pclass_surv / pclass_decd
        except:
            cls_prop[cls] = 0





    # -----------------
    # print stats
    # -----------------

    #ave_age_surv = age_surv/count_ave_age_surv
    print("The survivor Stats")
    print("count of survivors", tot_surv)
    print("Average age of survivors", ave_age_surv)
    print("sex surv", sex_surv)
    print("embarked surv", embarked_surv)
    print("class surv", pclass_surv)
    print("end")
    return
#
training_file = openfile()
results = analysedata(training_file)

print("end")