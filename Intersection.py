road = {"ns":"green","ew":"red"}


def lightSwitch(intersection):
    for k in intersection.keys():
        if intersection[k] =="green":
            intersection[k] ="yellow"
        elif intersection[k] == "yellow":
            intersection[k] = "red"
        elif intersection[k] == "red":
            intersection[k] = 'green'
    assert "red" in intersection.values(), "neither light is red" +str(intersection)
print(road)
lightSwitch(road)
print(road)