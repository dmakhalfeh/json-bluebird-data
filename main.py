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

if __name__ == "__main__":
  with open("2.json", "r") as f:
    calendar = json.load(f)
  cheapest_day,cheapest_fare = find_cheapest_flight(calendar)
  print(f"The cheapest flight is on {cheapest_day}, with a fare of ${cheapest_fare}")
