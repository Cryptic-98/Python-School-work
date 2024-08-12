initial_foods = ['pizza', 'sushi', 'tacos', 'pasta', 'burger']
favorite_foods = ['pizza', 'sushi', 'tacos', 'pasta', 'burger']
print(favorite_foods)
print(len(favorite_foods))
favorite_foods.append('falafel')
favorite_foods.remove('tacos')
print(favorite_foods)
sorted_foods = sorted(favorite_foods)
print(sorted_foods)
reversed_list = favorite_foods[::-1]
print(reversed_list) # reverse the sorted list
for food in favorite_foods:
    print(f'I love eating {food}')









