# Question: https://www.codewars.com/kata/566b490c8b164e03f8000002/train/python
# Name: 80's Kids #6: Rock 'Em, Sock 'Em Robots
# Level: 5kyu

# Description: 
''' You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, but things have gotten a little boring. You've each decided to add some amazing new features to your robot and automate them to battle to the death.
Each robot will be represented by an object. You will be given two robot objects, and an object of battle tactics and how much damage they produce. Each robot will have a name, hit points, speed, and then a list of battle tacitcs they are to perform in order. Whichever robot has the best speed, will attack first with one battle tactic.
Your job is to decide who wins.
Example:
 robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
 fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."
robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35. Now robot1 uses a punch, and so on.
Rules
- A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
- Robots alternate turns attacking. Tactics are used in order.
- A fight is over when a robot has 0 or less health or both robots have run out of tactics.
- A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
- If both robots run out of tactics, whoever has the most health wins. Return the message "{Name} has won the fight."
- If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw." '''

# Code:
def fight(robot_1, robot_2, tactics):
    fightIndex, robo1tactic, robo2tactic, robo1health, robo2health = 1, 0, 0, robot_1["health"], robot_2["health"]
    battle = True
    if robot_1["speed"] < robot_2["speed"]:
        fightIndex = 2
    while battle:
        if fightIndex % 2 == 0 and robo2tactic < len(robot_2["tactics"]):
            curr_tactic = robot_2["tactics"][robo2tactic]
            robo1health -= tactics[curr_tactic]
            robo2tactic += 1
        elif robo1tactic < len(robot_1["tactics"]):
            curr_tactic = robot_1["tactics"][robo1tactic]
            robo2health -= tactics[curr_tactic]
            robo1tactic += 1
        if robo1tactic >= len(robot_1["tactics"]) and robo2tactic >= len(robot_2["tactics"]) or robo1health <= 0 or robo2health <= 0:
            battle = False
        fightIndex += 1
    if robo1health < robo2health:
        return robot_2["name"] + " has won the fight."
    elif robo1health > robo2health:
        return robot_1["name"] + " has won the fight."
    else:
        return "The fight was a draw."
      
      
# Sample Tests
''' robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
test.assert_equals(fight(robot_1, robot_2, tactics), "Missile Bob has won the fight.")
robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
test.assert_equals(fight(robot_1, robot_2, tactics), "Rocky has won the fight.") '''
