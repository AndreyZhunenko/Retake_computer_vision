import numpy as np
import matplotlib.pyplot as plt

file = open("inp2.txt", "r")
lines = file.readlines()
file.close()

file = open("inp2.txt", "w")
for line in lines:
    if line[0] =='0':
        file.write(line)
file.close()

image = np.loadtxt("inp2.txt")

my_size = image.shape

first_i = 100
first_j = 100
left_i = 0
left_j = 0
right_i = 0
right_j = 0
    
for i in range(my_size[0]):
    for j in range(my_size[1]):
        if image[i][j] == 1:
           if i < first_i:
               first_i = i
               
left_i = first_i - 1
first_i = 0
for i  in range(my_size[0]):
    for j in range(my_size[1]):
        if image[i][j] == 1:
            if j < first_j:
                first_j = j
                
left_j = first_j - 1
first_j = 0
image[left_i][left_j] = 2

for i  in range(my_size[0]):
    for j in range(my_size[1]):
        if image[i][j] == 1:
            if i > first_i:
                first_i = i

right_i = first_i + 1
for i  in range(my_size[0]):
    for j in range(my_size[1]):
        if image[i][j] == 1:
            if j > first_j:
                first_j = j

right_j = first_j + 1
image[right_i][right_j] = 2

print(left_i, left_j)
print(right_i, right_j)

k = left_j + 1
while k < right_j:
    image[left_i][k] = 4
    k = k + 1
k = left_i
while k < right_i:
    image[k][right_j] = 4
    k = k + 1
k = right_j - 1
while k >= left_j:
    image[right_i][k] = 4
    k = k - 1
k = right_i - 1
while k > left_i:
    image[k][left_j] = 4
    k = k - 1


plt.imshow(image)
plt.show()