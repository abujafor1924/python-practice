def find_unshot_cans(harry_shot, larry_shot):
    total_cans = 10
    harry_unshot = total_cans - harry_shot
    larry_unshot = total_cans - larry_shot
    return harry_unshot, larry_unshot


harry_shot, larry_shot = map(int, input("Enter your Two Number : ").split())

result = find_unshot_cans(harry_shot, larry_shot)
print(result[0], result[1])
