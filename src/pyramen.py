#Developer: Andrew Park
#Last Modified: 09-29-2020

import traceback
import pandas as pd
import sys
import getopt

def main(argv):
    try:
        (opts,args)=getopt.getopt(argv,"hm:s:o:")
  
        f_menu=""
        f_sales=""
        f_out=""

        for opt,arg in opts:
            if opt=="-m":
                f_menu=str(arg)
            elif opt=="-s":
                f_sales=str(arg)
            elif opt=="-o":
                f_out=str(arg)
            else:
                usage()
                sys.exit(0)
        
        if (f_sales=="" or f_sales==None):
            raise Exception("sales file invalid, filename:"+str(f_sales))
        else:
            print("main|sales file: "+str(f_sales))

        if (f_menu=="" or f_menu==None):
            raise Exception("menu file invalid, filename:"+str(f_menu))
        else:
            print("main|menu file: "+str(f_menu))

        if (f_out=="" or f_out==None):
            raise Exception("output file invalid, filename:"+str(f_out))
        else:
            print("main|output file: "+str(f_out))

        menu=pd.read_csv(f_menu,header=0)
        sales=pd.read_csv(f_sales,header=0) 

        print("main|out:")

        #reports={}
        fd=open(f_out,"w")
        distinct_items=sales['Menu_Item'].unique()
        for sale_item in distinct_items:
            if (sale_item!="" or sale_item!=None):
            
                menu_row=menu.loc[menu["item"]==sale_item]
                sales_rows=sales[sales.Menu_Item==sale_item]
                
                count=sales_rows['Quantity'].sum()
                price=menu_row['price'].values[0]
                revenue=price*count
                cost=menu_row['cost'].values[0]*count
                profit=revenue-cost
               
                ''' 
                print("count:"+str(count))
                print("revenue:"+str(revenue))
                print("cost:"+str(cost))
                print("profit:"+str(profit))
                '''

                # DEBUG - This structure was discontinued due to bad design
                # reports[sale_item]={"count":count,"revenue":revenue,"cogs":cost,"profit":profit}

                print(sale_item+" "+str({"count":count,"revenue":revenue,"cogs":cost,"profit":profit}))
                fd.write(sale_item+" "+str({"count":count,"revenue":revenue,"cogs":cost,"profit":profit})+"\n")
        fd.close() 
        print("main|completed")   
    except:
        traceback.print_exc()
        pass

def usage():
    print("Usage: python pyramen.py -s sales -m menu -o output") 

if __name__=="__main__":
    main(sys.argv[1:])

