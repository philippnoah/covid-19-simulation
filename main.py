import math 
import matplotlib.pyplot as plt

# assuming sigmoid
def transmission_rate(i_p: int, r: float) -> float:
  sig = (1+r) - r/(1+1/(math.exp(10*i_p-5)))
  return sig

# purely for asthetic purposes
def print_summary(input_data):
  print("summary:\n population: {}\n infected on day 0: {}\n dark figure scaling factor: {}\n transmission rate function: sigmoid-ish\n heard immunity (%): {}".format(input_data["N"], input_data["i_0"], input_data["dfs"], input_data["hi"]))

# N: population size
# i_0: infected on day 0
# dfs: dark figure scaling factor eg. 1.0
# ptr: peak transmission rate
# hi: heard immunity estimate as percentage

def infected_by_days(N: int, i_0: float, dfs: float, ptr: float, hi: float):
  i = dfs * i_0/N
  day = 0
  while (i < hi):
    print("day {}: {} infected ({:.1f} %)".format(day, int(i*N), i*100))
    i *= transmission_rate(i, ptr)
    day += 1
  output_data = {"days": day, "i": i}
  return output_data

def main():
  input_data_DE = {"N": 82790000, "i_0": 84800, "dfs": 10, "ptr": 0.1, "hi": 0.75}
  input_data_US = {"N": 327200000, "i_0": 5, "dfs": 1, "ptr": 0.15, "hi": 0.75}
  input_data_AT = {"N": 8000000, "i_0": 1, "dfs": 1, "ptr": 0.15, "hi": 0.75}

  input_data = input_data_DE

  print_summary(input_data)
  output_data = infected_by_days((input_data["N"]), input_data["i_0"], input_data["dfs"], input_data["ptr"], input_data["hi"])

  print("\n{} days until {} ({:.1f} %) have been infected".format(output_data["days"], int(output_data["i"] * input_data["N"]), output_data["i"] * 100))

main()