# Perfect Cycle

API to track the occurrence of a perfect cycle in a list.
The perfect cycle has two conditions needed to arise in a list, and they are as follows:

1. All elements of the list must be visited.
2. The last element to be visited takes you back to position zero.

Note: Each value points to the next index to visit in the list.
e.g., a = [3,0,1,2] is a perfect cycle => a[0] = 3, a[3] = 2, a[2] = 1, a[1] = 0, a[0] = 3

This is a perfect cycle since we visited all elements, and the last element took us back to the beginning of the list. 

# Prerequisite(s)
- Python 3.10
- PIP (python package manager)

# Setup
[Optional] 0. Setup your virtualenv
1. `pip install poetry`
2. `poetry install`

# How to Run
`make run`

# How to Test
`make test`

# Client - Swagger UI
1. After you run the server, go to http://127.0.0.1:8000/docs
