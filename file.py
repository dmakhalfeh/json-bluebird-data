import os
import json


def find_cheapest_flight(calendar):
  cheapest_fare = float("inf")
  cheapest_day = None
  days=calendar["calendar"][0]["days"]
  for days in days:
    if days["fare"] < cheapest_fare and days["flight"]:
      cheapest_fare = days["fare"]
      cheapest_day = days["fullDate"]
  return cheapest_day,cheapest_fare
def list_files(directory):
  """Lists all the files in a directory."""
  files = os.listdir(directory)
  return files

def main():
  """Prints all the files in the current directory."""
  files = list_files('data/18')
  for date in files:
    data="data/18/"+date
    with open(data, "r") as f:
      calendar = json.load(f)
    cheapest_day, cheapest_fare = find_cheapest_flight(calendar)
    print(f"The cheapest flight is on {cheapest_day}, with a fare of ${cheapest_fare} found on {date}")


if __name__ == '__main__':
  main()
