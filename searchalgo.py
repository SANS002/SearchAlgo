import math
from collections import deque


def linear_search(arr,target):
    for index,element in enumerate(arr):
        if element==target:
            return index 


def binary_search(arr,target):
    arr = sorted(arr)
    low = 0 #1st index value 
    high = len(arr)-1 #last index value 
    
    while low <= high : #booundries for searcch
        mid = (low + high)//2 #index value of the middle element calculting each time 
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid + 1

    return -1

def jump_search(arr,target):
    arr = sorted(arr)
    n =len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step,n)-1] < target :
        prev = step
        step +=int(math.sqrt(n)) 
        if prev >=n:
            return -1
    for i in range(prev,min(step,n)):
        if arr[i]==target:
            return i

def interpolation_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high and target>=arr[low] and target<=arr[high]:
        if arr[low]==arr[high]:
            if arr[low]==target:
                return low
            return -1
        pos = low+((target-arr[low])*(high-low)//
                   (arr[high]-arr[low])) #position calc formula for I.Pol search
        if arr[pos] == target:
            return pos
        elif arr[pos]<target:
            low = pos+1
        else :
            high = pos - 1
        return -1
    
def exponential_search(arr,target):
    n = len(arr)
    if arr[0] == target:
        return 0
    index = 1
    while index < n and arr[index] <= target:
        index *= 2
    return binary_search(arr,target)

def fibonacci_search(arr, target):
    n = len(arr)
    
    fibM_minus_2 = 0  # (m-2)'th Fibonacci number
    fibM_minus_1 = 1  # (m-1)'th Fibonacci number
    fibM = fibM_minus_1 + fibM_minus_2  # m'th Fibonacci number
    
    while fibM < n:
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    
    offset = -1
    
    while fibM > 1:
        i = min(offset + fibM_minus_2, n - 1)
        
        if arr[i] < target:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            offset = i
        
        elif arr[i] > target:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        
        else:
            return i
    
    if fibM_minus_1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

def bfs (graph,start,target):
    visited = set()
    queue = deque([start])
    parent = {start : None}

    while queue:
        node = queue.popleft()
        if node == target:
            return{
                "Trget":node,
                "Parent":parent[node],
                "Neighbors" : graph[node]
            }
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node 
                queue.append(neighbor)
    return "Not found"

def dfs(graph, node, target, visited=None, parent=None):
    if visited is None:
        visited = set()  
    if parent is None:
        parent = {}  

    visited.add(node)

    if node == target:
        return {
            "Target": node,
            "Parent": parent[node] if node in parent else None,
            "Neighbors": graph[node]
        }

    for neighbor in graph[node]:
        if neighbor not in visited:
            parent[neighbor] = node  
            result = dfs(graph, neighbor, target, visited, parent)
            if result:
                return result

    return None 
