landscaping = {"tool": 0, "money": 0}

tools = [
{"name": "Teeth", "profit": 1, "cost": 0},
{"name": "Rusty Scissors", "profit": 5, "cost": 5},
{"name": "Push Lawnmower", "profit": 50, "cost": 25},
{"name": "Battery Powered Lawnmower", "profit": 100, "cost": 250},
{"name": "Team of Students", "profit": 250, "cost": 500},

]

def cut_grass():
    tool = tools[landscaping["tool"]]
    print(f"You mow a lawn with your {tool['name']} and make {tool['profit']}. You have {landscaping['money']}")
    landscaping["money"] += tool["profit"]

def check_stats():
    tool = tools[landscaping["tool"]]
    print(f"You currently have {landscaping['money']} and are using a {tool['name']}")

def upgrade():
    if (landscaping["tool"] >= len(tools) -1):
        print("No more upgrades available.")
        return 0
    next_tool = tools[landscaping["tool"]+1]
    if (next_tool == None):
        print("There are no more tools to upgrade to.")
        return 0
    if (landscaping["money"] < next_tool["cost"]):
     print("Not enough money to upgrade tool.")
     return 0
    print("You are upgrading your tool.")
    landscaping["money"] -= next_tool["cost"]
    landscaping["tool"] += 1

def win_check():
    if(landscaping["tool"] == 4 and landscaping["money"] >= 1000):
        print("You Won!")
        return True
        return False

while (True):


    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit: ")

    i = int(i)

    if(i == 1):
        cut_grass()
    
    if (i == 2):
        check_stats()
        
    if (i == 3):
        upgrade()
        
    if (i == 4):
        print("You quit the game.")
        break

    if win_check():
        break