import requests
import threading
test = input("What's your url?\n") # if this url do over 1000 amount search and isn't in CF, Maybe Down.
def main():
  global test
  r = requests.get(test)
  print('Done' + str(r.status_code))
while True:
    threading.Thread(target=main).start()
