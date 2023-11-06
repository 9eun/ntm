#1. 포지션 GD 코딩
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
r=pd.read_csv('농구선수 스텟.csv',engine='python')  #csv 파일 불러오기
r1=r[r['POS']=='GD'].copy()     #포지션 설정
r1['공헌도']=r1['공헌도']=((r1['PTS']+r1['STL']+r1['BS']+r1['DEF'])*1.0+(r1['OFF']+r1['AST'])*1.5+r1['MIN']*0.4)-round(((r1['TO']*1.5)+(r1['2PA']-r1['2P'])*(100-r1['2P%'])*0.01*1.3+(r1['3PA']-r1['3P'])*(100-r1['3P%'])*0.01*1.5+(r1['FTA']-r1['FT'])*(100-r1['FT%'])*0.01*0.8),2)   #공헌도 설정
r2=r1.sort_values(by='공헌도',ascending=False)    #공헌도 내림차순 정렬
r3=r2.head(10)     #10개 만 보이게 
 
plt.figure(figsize=(15,8))       
plt.xticks(rotation=0)
sns.barplot(x='NAME',y='공헌도',data=r3)     
r3

#2. 포지션 C 코딩
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
r=pd.read_csv('농구선수 스텟.csv',engine='python')
r1=r[r['POS']=='C'].copy()
r1['공헌도']=r1['공헌도']=((r1['PTS']+r1['STL']+r1['BS']+r1['DEF'])*1.0+(r1['OFF']+r1['AST'])*1.5+r1['MIN']*0.4)-round(((r1['TO']*1.5)+(r1['2PA']-r1['2P'])*(100-r1['2P%'])*0.01*1.1+(r1['3PA']-r1['3P'])*(100-r1['3P%'])*0.01*0.9+(r1['FTA']-r1['FT'])*(100-r1['FT%'])*0.01*0.8),2)
r2=r1.sort_values(by=['공헌도'],ascending=False)
r3=r2.head(10)

plt.figure(figsize=(15,8))
plt.xticks(rotation=0)
sns.barplot(x='NAME',y='공헌도',data=r3)
r3






#3. 포지션 FD 코딩
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
r=pd.read_csv('농구선수 스텟.csv',engine='python')
r1=r[r['POS']=='FD'].copy()
r1['공헌도']=r1['공헌도']=((r1['PTS']+r1['STL']+r1['BS']+r1['DEF'])*1.0+(r1['OFF']+r1['AST'])*1.5+r1['MIN']*0.4)-round(((r1['TO']*1.5)+(r1['2PA']-r1['2P'])*(100-r1['2P%'])*0.01*1.2+(r1['3PA']-r1['3P'])*(100-r1['3P%'])*0.01*1.2+(r1['FTA']-r1['FT'])*(100-r1['FT%'])*0.01*0.8),2)
r2=r1.sort_values(by=['공헌도'],ascending=False)
r3=r2.head(10)

plt.figure(figsize=(15,8))
plt.xticks(rotation=0)
sns.barplot(x='NAME',y='공헌도',data=r3)
r3
