import numpy as np
import pandas as pd

my_column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']

my_data = np.random.randint(low=0, high=101, size=(3, 4))

df = pd.DataFrame(data=my_data, columns=my_column_names)

print(df)

print(f"Second row of Eleanor column: {df['Eleanor'][1]}")

print("********* OUTRO *********")

df['Janet'] = df['Tahani'] + df['Jason']

print(df)

print("********* COPYING PREVIOUS DATASET *********")

# Cria uma referencia chamando my_dataframe para uma nova variável
print("Experiment with reference:")
reference_to_df = df

print(f" Starting value of df: {df['Jason'][1]}")
print(f" Starting value of reference_to_df: {reference_to_df['Jason'][1]}")

df.at[1, 'Jason'] = df['Jason'][1] + 5
print(f" Starting value of df: {df['Jason'][1]}")
print(f" Starting value of reference_to_df: {reference_to_df['Jason'][1]}")

print("**************************")

print('Experiment with a true copy:')
copy_of_dataframe = my_data.copy()
print(f" Starting value of df: {df['Activity'][1]}")
print(f" Starting value of reference_to_df: {reference_to_df['Activity'][1]}")

print("********* MODIFICANDO UMA ÚNICA CELULA NO DATAFRAME *********")
# my_data.at[1, 'Activity'] = my_data['Activity'][1] + 3
# print(f" Starting value of df: {my_data['Activity'][1]}")
# print(f" Starting value of reference_to_df: {copy_of_dataframe['Activity'][1]}")
df.at[1, 'Jason'] = df['Jason'][1] + 5
# print(f" Starting value of df: {df['Jason'][1]}")
# print(f" Starting value of copy_of_df: {copy_of_dataframe['Jason'][1]}")

print(df)
