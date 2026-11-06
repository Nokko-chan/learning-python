alien_0 = {"color": "green", "speed": "slow"}
# alien_0["points"] = 5

# print(alien_0["points"])
points_value = alien_0.get("points", "No point value assigned.")
print(points_value)