# python3
import sys
import threading
import numpy


def compute_height(n, parents):
  # Write this function
    heights=[0]*n
    vaiEsTurBiju=[0]*n
    max_height = 0

    for i in range(0, n):
        #print("i = ", i)
        if(vaiEsTurBiju[i] == 1):
            continue
        j = i
        previousHeights = []
        while(True):
            #print("j = ", j)
            if(vaiEsTurBiju[j] == 1):
                for x in previousHeights:
                  heights[x]+=heights[j]
                break
            vaiEsTurBiju[j]=1
            previousHeights.append(j)
            for x in previousHeights:
                heights[x]+=1
            if(parents[j] == -1):
                break
            j = parents[j]
  # Your code here 
    for height in heights:
        if height > max_height:
            max_height = height

    return max_height


def main():
  # implement input form keyboard and from files
  # input number of elements
  text=input()
  text=text.upper()
  if text.startswith("I"):
    number_of_nodes = int(input)

  # input values in one variable, separate with space, split these values in an array
    nodes = input()
    splited_nodes= nodes.split()
    list_of_ints =numpy.array((list(map(int, splited_nodes))))
  
  
  
  if text.startswith("F"):
     file_name = input()
     if file_name.find("a") != -1:
        return
     
     file_name = open(file_name)
     number_of_nodes = int(file_name.readline())
     nodes = file_name.readline()
     splited_nodes= nodes.split()
     list_of_ints =numpy.array((list(map(int, splited_nodes))))
            


  # call the function and output it's result
  print("calling compute heioght ")
  print(compute_height(number_of_nodes, list_of_ints))
  print("viss")
  pass


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(107)  # max depth of recursion
threading.stack_size(227)  # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))