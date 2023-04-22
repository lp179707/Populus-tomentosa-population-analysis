import pandas as pd
import sys
#The first parameter is the input file, which contains three columns named chr,bp, and p；
#The second parameter is the location of the starting site;
#The third parameter is the output file prefix。

f=pd.read_csv(sys.argv[1], sep='\t',header=None)
f.columns=['chr','bp','p']
#Classification by chromosome
g=f.groupby('chr')
begin=sys.argv[2]
begin=int(begin)
hete=pd.DataFrame()
for i in dict(list(g)).keys():
    index=dict(list(g)).get(i)
    ran=list(range(begin,index['bp'].max()+5000,5000))
    index['bin']=pd.cut(x=index['bp'],bins=ran)
    index = index.groupby('bin').agg({'p':'sum'})
    index['chr']=i
    hete = hete.append(index)
hete.to_csv(sys.argv[3]+'.csv')
