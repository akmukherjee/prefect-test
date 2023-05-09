from prefect import flow,task
import subprocess
from test import sum




def load():
   print("Loading data")
   print('Sum is: '+str(sum(2,4)))

@flow(name="Hello-world")
def my_flow():
   #subprocess.call('git submodule update --init --recursive', timeout=60, shell=True)
   subprocess.call('ls -l',shell=True)
   from bento.common.utils import APP_NAME
   load()

if __name__ == "__main__":
   my_flow()
