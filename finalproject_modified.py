import pandas as pd
import sys
#import csv file from the command line
df=pd.read_csv(sys.argv[1])

#drop weight, finbourgh_flick, double_eight_loop due to missing information

df.drop(["weight","finbourgh_flick", "double_eight_loop"], axis=1,inplace=True)

#handling missing values by creating another category

columns_replace=["house","player_code","move_specialty"]
for column in columns_replace:
	df[column].replace("?","U",inplace=True)
df["gender"].replace("Unknown/Invalid","U",inplace=True)
df = df[df.gender != 'U']
print (df.shape)

#sum num_games_satout, num_games_injured, num_games_notpartof and combine them in one feature named num_game_not_participate

df["num_game_not_participate"]=df.num_games_satout+df.num_games_injured+df.num_games_notpartof

#Reducing number of categories
#do encoding
def map_features(features,df,dict):
	for i in features:
		df = df.replace({i:dict})

	return df 
foul_dict={'None':'none','Norm':'norm','>7':'high','>8':'high','>200':'high','>300':'high'}
foul_columns=["snitchnip","stooging"]
df=map_features(foul_columns,df,foul_dict)

#convert move specialty
#1 stands for with specialty, 0 stands for without specialty
def convert_move_specialty(df):
	dict={}
	for i in df["move_specialty"]:
		if i=="U":
			dict.update({"U":0})
		else:
			dict.update({i:1})
	return dict

move_spec_dict=convert_move_specialty(df)
df=map_features(["move_specialty"],df,move_spec_dict)

#convert tactics
#Steady,Up,Down to 1, No to 0

tactics_dict={'Steady':1,'No':0,'Up':1,'Down':1}
tactics_columns=["body_blow","checking","dopplebeater_defence","hawkshead_attacking_formation","no_hands_tackle","power_play","sloth_grip_roll","spiral_dive","starfish_and_stick","twirl","wronski_feint","zig-zag","bludger_backbeat","chelmondiston_charge","dionysus_dive","reverse_pass","parkins_pincer","plumpton_pass","porskoff_ploy","transylvanian_tackle","woollongong_shimmy"]
df=map_features(tactics_columns,df,tactics_dict)

#sum up number of tactics used by each player
#create new column named num_total_tactics

df["num_total_tactics"]=0
def sum_tactics(df,columns):

	for i in columns:
		
		df["num_total_tactics"]+=df[i]

	return df

sum_tactics(df,tactics_columns)

#convert gender
#Female to 0, Male to 1

ordered_satisfaction = ["Female","Male"]
cat_dtype = pd.api.types.CategoricalDtype(ordered_satisfaction, ordered=True)
df["gender"]=df["gender"].astype(cat_dtype).cat.codes

#convert snitch_caught
#No to 0, Yes to 1

ordered_satisfaction = ["No","Yes"]
cat_dtype = pd.api.types.CategoricalDtype(ordered_satisfaction, ordered=True)
df["snitch_caught"]=df["snitch_caught"].astype(cat_dtype).cat.codes

#convert change
#No to 0,Ch to 1

ordered_satisfaction = ["No","Ch"]
cat_dtype = pd.api.types.CategoricalDtype(ordered_satisfaction, ordered=True)
df["change"]=df["change"].astype(cat_dtype).cat.codes

#one-hot encoding rest of columns

df=pd.get_dummies(df, columns=["house","foul_type_id","game_move_id","penalty_id","player_code","player_type","snitchnip","stooging"])

#move target to the last column

df_target=pd.DataFrame(data=df["quidditch_league_player"])
df.drop(["quidditch_league_player"], axis=1,inplace=True)
df.insert(len(df.columns),"quidditch_league_player", df_target)
df.to_csv("a.csv",index=False)

