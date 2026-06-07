# drop_duplicates(series + dataframe) -> works like and -> duplicated()

# ye ye batata hai ki apke data me kitne rows duplicated hai 
import pandas as pd
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

print(marks)
ans =  marks.duplicated()
# ye bata deta hai ki kitne duplicated row hai 
print(ans)

ans =  marks.duplicated().sum()
# ye method ye bataa deta hai ki kitne duplicates ka count ya sum kya hia 
print(ans)


# hamne yaha anya deta banaya usem dekha 
temp = pd.Series([1,1,1,2,3,3,4,4,])
a = temp.drop_duplicates(keep='last')
print(a)

# find the last match played by virat kohli in Delhi
# step 1:
# ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']
# ipl.head()

# yethoda trik q hai 
# step 2:
# def did_kohli_play(players_list):
#   return 'V Kohli' in players_list

# step 3: 
# ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)
# ipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play'] == True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first')

