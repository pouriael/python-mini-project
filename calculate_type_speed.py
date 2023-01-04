from time import *
import random as r


def mistake(partest,usertest): 
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except :
            error +=1
    return error
    
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput) / time_R
    return round(speed)

test = ["test",'test','test']

test1 = r.choice(test)
print("**** typing speed ****")
print()
print(test1)
print()
time_1 = time()
testinput = input("enter: ")
time_2 = time()

print("speed: ",speed_time(time_1,time_2,testinput),"w/sec")
print("error: ",mistake(test1,testinput))