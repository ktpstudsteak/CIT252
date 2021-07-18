# Doctor Who needs help keeping track of who's next in line. He keeps losing his printout and would like to have it digitally. 
# Create a queue that will append new patients to the queue, remove old ones, and update (print out) the queue after each operation.

from collections import deque

patients = deque()


# Add patient function 
def addPatients(name):
    patients.append(name)
    print(patients)
    return patients

# Remove patient function
def removePatients():
    patients.pop()
    print(patients)


addPatients("Bob")
addPatients("Terisa")
addPatients("Julie")

removePatients()
removePatients()

