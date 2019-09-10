import pandas
import matplotlib.pyplot as plt

home = pandas.read_csv('home_ownership_data.csv')
loan = pandas.read_csv('loan_data.csv')
length = home['member_id'].__len__()

home_member_ids = []
loan_member_ids = []
loan_amount = []
types = []

mortgage_loan = 0
mortgage_counter = 0
own_loan = 0
own_counter = 0
rent_loan = 0
rent_counter = 0


def init_array(arr, csv_file, obj):
    """Function used to initialize the arrays
    """
    for k in range(length):
        arr.append(csv_file[obj][k])


init_array(home_member_ids, home, 'member_id')
init_array(loan_member_ids, loan, 'member_id')
init_array(loan_amount, loan, 'loan_amnt')
init_array(types, home, 'home_ownership')

# This determines which type of loan amount to increment depending on the type of the member id's home ownership
for i in range(length):
    if types[i] == 'MORTGAGE':
        mortgage_counter += 1
        for j in range(length):
            if home_member_ids[i] == loan_member_ids[j]:
                mortgage_loan += int(loan_amount[j])
    elif types[i] == 'RENT':
        rent_counter += 1
        for j in range(length):
            if home_member_ids[i] == loan_member_ids[j]:
                rent_loan += int(loan_amount[j])
    elif types[i] == 'OWN':
        own_counter += 1
        for j in range(length):
            if home_member_ids[i] == loan_member_ids[j]:
                own_loan += int(loan_amount[j])

mortgage_average = mortgage_loan / mortgage_counter
rent_average = rent_loan / rent_counter
own_average = own_loan / own_counter

x_values = ['MORTGAGE', 'OWN', 'RENT']
y_values = [mortgage_average, own_average, rent_average]


def plot_graph():
    plt.bar(x_values, y_values)
    plt.xlabel('Home ownership', fontsize=10)
    plt.ylabel('Average loan amount', fontsize=10)
    plt.title('Average loan amount per home ownership')
    plt.show()


plot_graph()
