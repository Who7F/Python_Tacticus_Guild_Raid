import requests
from collections import Counter
from tabulate import tabulate

def getApi(url, API_key):
    headers = {
        "accept": "application/json",
        "X-API-KEY":API_key
        }

    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error {response.status_code}. GET DA MEK")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def getAttackCount(data, damageType):
    user_ids = []
    for e in data["entries"]:
        if e["damageType"] == damageType:
            user_ids.append(e["userId"])

    return Counter(user_ids)

def displayAttact(user_counts, guild_members):
    table = []
    for user_id, count in user_counts.items():
        if user_id in guild_members:
            table.append([guild_members[user_id], count, "BOYZ"])
        else:
            table.append([user_id, count, "WHO DA ONE"])
    print(tabulate(table, headers=["User Name", "Count", "_"], tablefmt="github"))

def displayMissing(user_counts, guild_members):
    table = []
    for g in guild_members:
        if g not in user_counts:
            table.append([guild_members[g], "GORT"])
    print(tabulate(table, headers=["User ID", "_"], tablefmt="github"))
    

def main():
    print("Sup")
    
    API_key = 
    url = "https://api.tacticusgame.com/api/v1/guildRaid"

    guild_members = {

        }

    data = getApi(url, API_key)

    boss_battle = getAttackCount(data, "Battle")
    displayAttact(boss_battle, guild_members)
    displayMissing(boss_battle, guild_members)

if __name__=="__main__":
    main()

'''
https://api.tacticusgame.com/
https://api.tacticusgame.com/swagger-ui/index.html#/
'''
