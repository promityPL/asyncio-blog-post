import asyncio
from random import random
 
# funkcja symulująca długie obliczenia
async def long_computation(task_id: int) -> str:
   for i in range(3):
       await asyncio.sleep(random())
       print(f"Task {task_id}: {i}")
   return "DONE"
 
# uruchamia n współbieżnych funkcji _long_computation_
async def launch_tasks(n_tasks: int):
   coros = [long_computation(i) for i in range(n_tasks)]
   await asyncio.gather(*coros)

# wywołując python example.py możemy zobaczyć, że zadania są
# rzeczywiście wykonywane współbieżnie
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(launch_tasks(3))