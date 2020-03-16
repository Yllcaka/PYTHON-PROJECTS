import threading
import random
import os
import time
mutex = threading.Lock()
tree = '''
          .     .  .      +     .      .          .
     .       .      .     #       .           .
        .      .         ###            .      .      .
      .      .   "#:. .:#R"##:. .:B"  .      .
          .      . "####"W##"##Y#"  .
       .     "#:.    .:#"#W#"#:.    .:#"  .        .       .
  .             "####Y####"####R####"        .        .
        .    "#:.  "##W#"#B#"Y###"  .:#"   .       .
     .     .  "###Y###""##"##""#R#W###"                  .
                ."##"#####"#R###"##"           .      .
    .   "#:. ...  .:##"#B#"###"##:.  ... .:#"     .
      .     "##R####"##"B####"##"#Y#####"      .     .
    .    .     "#####""#####B#""##R##"    .      .
            .     "      000      "    .     .
       .         .   .   000     .        .       .
.. .. ..................O000O........................ ......
'''
tree = "\u001b[32m" + tree + "\033[0m"
tree = list(tree.rstrip())
for i,c in enumerate(tree):
    if c ==".":
        tree[i] = f"\u001b[37m{c}\033[32m"
    if c =="0" or c == "O":
        tree[i] = f"\u001b[36m{c}\033[32m"
    if c == "+":
        tree[i] = f"\u001b[33m{c}\033[32m"

yellow = []
blue = []
red = []
bblue = []
def colored_dot(color):
    if color == "yellow":
        return f"\u001b[33m●\033[32m"
    if color == "blue":
        return f"\u001b[34m●\033[32m"
    if color == "red":
        return f"\u001b[31m●\033[32m"
    if color == "bblue":
        return f"\u001b[37m●\033[32m"

def lights(color,indexes):
    off = True
    while True:
        for idx in indexes:
            tree[idx] = colored_dot(color) if off else "\u001b[37m●\033[32m"

        mutex.acquire()
        os.system("cls" if os.name == 'nt' else "clear")
        print("".join(tree))
        mutex.release()
        off = not off
        time.sleep(random.uniform(0.5,1.5))
for i,c in enumerate(tree):
    if c == "Y":
        yellow.append(i)
        tree[i] = "●"
    if c == "B":
        blue.append(i)
        tree[i] = "●"
    if c == "R":
        red.append(i)
        tree[i] = "●"
    if c == "W":
        bblue.append(i)
        tree[i] = "●"


ty = threading.Thread(target=lights, args=("yellow",yellow))
tb = threading.Thread(target=lights, args=("blue",blue))
tr = threading.Thread(target=lights, args=("red",red))
tw = threading.Thread(target=lights, args=("bblue",bblue))


for t in [ty,tb,tr,tw]:
    t.start()
for t in [ty,tb,tr,tw]:
    t.join()