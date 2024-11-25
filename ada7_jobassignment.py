# -*- coding: utf-8 -*-
"""ADA7_JobAssignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X08GhHx1fVTkw6zO891kA4_TssPwv1yn
"""

import heapq
import copy

class Node:

    def __init__(self, x, y, assigned, parent):

        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.workerID = x
        self.jobID = y
        self.assigned = copy.deepcopy(assigned)

        if y != -1:
            self.assigned[y] = True

    def __lt__(self, other):

        return self.cost < other.cost  # Compare nodes based on their cost

class CustomHeap:

    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):

        if self.heap:
            return heapq.heappop(self.heap)
        return None

def new_node(x, y, assigned, parent):
    return Node(x, y, assigned, parent)

def calc_cost(cost_mat, x, y, assigned, N):

    cost = 0
    avail = [True] * N

    for i in range(x + 1, N):
        min_val, min_index = float('inf'), -1

        for j in range(N):
            if not assigned[j] and avail[j] and cost_mat[i][j] < min_val:
                min_index = j
                min_val = cost_mat[i][j]
        cost += min_val
        avail[min_index] = False

    return cost

def print_assig(min_node):

    if min_node.parent is None:
        return

    print_assig(min_node.parent)
    print(f"Assign Worker {chr(min_node.workerID + ord('A'))} to Job {min_node.jobID + 1}")

def find_min_cost(cost_mat, N):

    pq = CustomHeap()
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.workerID = -1
    pq.push(root)

    while True:
        min_node = pq.pop()
        i = min_node.workerID + 1

        if i == N:
            print_assig(min_node)
            return min_node.cost

        for j in range(N):

            if not min_node.assigned[j]:
                child = new_node(i, j, min_node.assigned, min_node)
                child.pathCost = min_node.pathCost + cost_mat[i][j]
                child.cost = child.pathCost + calc_cost(cost_mat, i, j, child.assigned, N)
                pq.push(child)

if __name__ == "__main__":

    print("Job Assignment Problem")
    num_workers = int(input("Enter num of workers: "))
    num_jobs = int(input("Enter num of jobs: "))

    if num_workers != num_jobs:
        print("Num of workers and jobs must be equal.")

    else:
        print("Enter cost mat row by row (space-separated values):")
        cost_mat = []

        for i in range(num_workers):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            cost_mat.append(row)

        print("\nCalculating Optimal Assignment...")
        optimal_cost = find_min_cost(cost_mat, num_workers)

        if optimal_cost is not None:
            print(f"\nOptimal Cost is: {optimal_cost}")
        else:
            print("\nNo optimal solution found.")

"""
Time and Space Complexity : O(N^2 log N)
"""