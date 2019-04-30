import csv
import pandas as pd 
#replace missing values with an unique category
data=pd.read_csv("qudditch_training.csv")
columns_replace=["house","player_code","move_specialty"]
for column in columns_replace:
	data[column].replace("?","U",inplace=True)

data["gender"].replace("Unknown/Invalid","U",inplace=True)
#seperate training and target
#drop id_num,player_id,weight,quidditch_league_player 
df=pd.DataFrame(data=data)
df_target=pd.DataFrame(data=data["quidditch_league_player"])
df.drop(["id_num","player_id","weight","quidditch_league_player"], axis=1,inplace=True)
#do one-hot encoding
df=pd.get_dummies(df, columns=["gender","house","foul_type_id","game_move_id","penalty_id","player_code","move_specialty","player_type"])
df.insert(len(df.columns),"quidditch_league_player", df_target) 
#do label encoding
#print(df)
df.to_csv("a.csv",index=False)
#df_target.to_csv("b.csv",index=False)

