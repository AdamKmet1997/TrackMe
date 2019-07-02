# from matplotlib.ticker import FuncFormatter
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(16)
# money = [1.5e5, 2.5e6, 5.5e6, 2.0e7,12.5,12.8,1.5e5, 2.5e6, 5.5e6, 2.0e7,12.5,12.8,1.5e5, 2.5e6, 5.5e6, 2.0e7]


# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$%1.1fM' % (x * 1e-6)


# formatter = FuncFormatter(millions)

# fig, ax = plt.subplots()
# ax.yaxis.set_major_formatter(formatter)
# plt.bar(x, money)
# plt.xticks(x, ('q', 'w', 'e', 'r','t', 'y', 'u', 'i','o', 'p', 'a', 's','d', 'f', 'g', 'h'))
# plt.show()

mylines = []                                # Declare an empty list.
with open ('key_log1.txt', 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.

# Locate and print all occurences of letter "e"

index = 0                     # current index 
prev = 0                      # previous index
str = mylines[1]              # string to be searched (first element of mylines)
substr = "="                  # substring to search for
while index < len(str):       # While index has not exceeded string length,
  index = str.find(substr, index)  # set index to first occurrence of "e"
  if index == -1:             # If nothing was found,
    break                     # exit the while loop.
  print(" " * (index - prev) + "=", end='')  # print location of this "e"
  prev = index + len(substr)  # set previous to index + 1
  index += len(substr)        # increment the index by the length of substr. 
                              # (Repeat while loop until index >= len(str))
print('\n' + str);            # Print the original string under the e's