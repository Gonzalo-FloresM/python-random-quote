import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print(quotes[rnd] ,end = '')
  print(quotes[rnd2])

  print("Hello there!", end = '')
  print("It is a great day.")

  quotes.append("Explore Python on your own")
  print(quotes[len(quotes)-1])

if __name__== "__main__":
  primary()
