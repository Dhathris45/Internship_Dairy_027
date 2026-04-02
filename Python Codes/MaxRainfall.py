rainfall = {
    "Karnataka": 12,
    "Maharashtra": 20,
    "Kerala": 23
}

values = rainfall.values()

m = max(values)

for state in rainfall:
    if rainfall[state] == m:
        print(state, "has the maximum rainfall")