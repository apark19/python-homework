#Developer: Andrew Park
#Last Modified: 9-28-2020

import pandas as pd
import getopt
import traceback
import sys

def main(argv):
    try:
        (opts,args)=getopt.getopt(argv,"hi:f:")

        input=""
        output=""

        for opt,arg in opts:
            if opt=="-i":
               input=str(arg)
            elif opt=="-f":
               output=str(arg)
            else:
               usage()
               sys.exit(1)

        if (input=="" or input==None):
            print("main|Input file is invalid, input:"+str(input))
        else:
            print("main|input:"+str(input))

        if (output=="" or output==None):
            print("Output file is invalid, output:"+str(output)) 
        else:
            print("main|output:"+str(output))

        # assume input file is .csv
        budgets=pd.read_csv(input,header=0)

        #print(budgets) 
        months=budgets.Date.unique().size

        # assume no NaN values
        sum=budgets['Profit/Losses'].sum() 

        gain=""
        loss=""
        avg_sum=0
        for index in range(len(budgets)):
            #print(budgets.loc[index,'Date'])
            #print(budgets.loc[index,'Profit/Losses'])  
 
            if index==0:
                prev=budgets.loc[index,'Profit/Losses']
                tmp_gain=0
                tmp_loss=0
            else:
                cur=budgets.loc[index,'Profit/Losses']

                if (cur-prev>tmp_gain):
                    tmp_gain=cur-prev
                    gain="Greatest Increase in Profits: "+str(budgets.loc[index,'Date'])+" ($"+str(tmp_gain)+")"
                elif (cur-prev<tmp_loss):
                    tmp_loss=cur-prev
                    loss="Greatest Decrease in Profits: "+str(budgets.loc[index,'Date'])+" ($"+str(tmp_loss)+")"

                # append to avg_sum
                avg_sum+=cur-prev

                #print(cur-prev)
                #print(avg_sum)

                prev=cur

        #print(gain)
        #print(loss)          

        #print(len(budgets))
        #print(avg_sum/len(budgets)) 
        write_log(months,sum,avg_sum/len(budgets),gain,loss)
        
        rc=write_output(output,months,sum,avg_sum/len(budgets),gain,loss)
        if rc!=0:
            print("main|write_output failed...")
            raise Exception("rc:"+str(rc))
    except:
        traceback.print_exc()


def write_log(total_months,net_total,avg_change,profit,loss):
    print('''\nFinancial Analysis
-------------------------
Total Months: '''+str(total_months)+'''
Total: $'''+str(net_total)+'''
Average Change: $'''+str(avg_change)+
'''\n'''+str(profit)+
'''\n'''+str(loss))

def write_output(fname,total_months,net_total,avg_change,profit,loss):
    try:
        fd=open(fname,"w")
        fd.write('''Financial Analysis
---------------------------
Total Months: '''+str(total_months)+'''
Total: $'''+str(net_total)+'''
Average Change: $'''+str(avg_change)+
'''\n'''+str(profit)+
'''\n'''+str(loss))

        fd.close()
        print("main|completed")
        return 0
    except:
        traceback.print_exc()
        return 1

def usage():
    print('''Usage: python pybank.py -i input -f output''')

if __name__ == "__main__":
    main(sys.argv[1:])
    exit()
