import numpy as np

one_dimensional_array = np.array([1.2,  2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print("*****THIS IS A ONE DIMENSIONAL ARRAY*****")
print(one_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print("*****THIS IS A TWO DIMENSIONAL ARRAY")
print(two_dimensional_array)

sequence_of_integers = np.arange(5, 12)
print("*****THIS IS A SEQUENCE OF INTEGERS*****")
print(sequence_of_integers)

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=6)
print("*****THIS IS MULTIPLE INTEGERS BETWEEN 50 AND 100*****")
print(random_integers_between_50_and_100)

random_floats_between_0_and_1 = np.random.random(size=([6]))
print("*****THIS IS FLOATS*****")
print(random_floats_between_0_and_1)

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print("*****FLOATS PLUS 2.0*****")
print(random_floats_between_2_and_3)

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print("*****FLOATS BETWEEN 150 AND 300*****")
print(random_integers_between_150_and_300)
