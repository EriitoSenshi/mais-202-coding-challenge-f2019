import pandas

home = pandas.read_csv('home_ownership_data.csv')
loan = pandas.read_csv('loan_data.csv')

home_member_ids = []
loan_member_ids = []
loan_amount = []
types = []


for i in range(home['member_id'].__len__()):
    home_member_ids.append(home['member_id'][i])
    types.append(home['home_ownership'][i])

for i in range(loan['member_id'].__len__()):
    loan_member_ids.append(loan['member_id'][i])
    loan_amount.append(loan['loan_amnt'][i])



