from prefect import flow,task
from test import sum




def load():
   print("Loading data")
   print('Sum is: '+str(sum(2,4)))

@flow(name="Hello-world")
def my_flow():
   load()

if __name__ == "__main__":
   my_flow()
