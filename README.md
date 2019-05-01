# ml_final_project
machine learning project
Because I have doubts on label encoding, I created different version for trying. Snitchnip and stooging are both foul type but the maximum # of Snitchnip in our data is >300 and the maximum # of stooging in our data is >8. Should they be encoded as the same integer? So >300 # of Snitchnip means the same as >8 # of stooging? This problem only affects the model with weights instead of random forests. 
 

Version 1: do label encoding for snitchnip and stooging on the same scale.
For example: 
There are 4 categories in snitchnip: None, Norm, >200, >300
There are 4 categories in stooging: None, Norm, >7, >8
The order hierarchy is [None,Norm,>7,>8,>200,>300]
So after label encoding:
There are 4 values in snitchnip: 0,1,4,5 corresponds to None, Norm, >200, >300
There are 4 values in stooging: 0,1,2,3 corresponds to None, Norm, >7, >8

Version 2: do label encoding for snitchnip and stooging on the different scale.
The order hierarchy for snitchnip is [None,Norm,>200,>300]
The order hierarchy for stooging is [None,Norm,>7,>8]
So after label encoding:
There are 4 values in snitchnip: 0,1,2,2 corresponds to None, Norm, >200, >300
There are 4 values in stooging: 0,1,2,3 corresponds to None, Norm, >7, >8

I encoded other features using one hot encoding.
I left some comlumns with numerical values. 
I converted the target to 0 or 1.
0 stands for NO, 1 stands for YES.








