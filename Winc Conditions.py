weather = {
        'rainy': 'take cows to cowshed',
        'sunny': 'take cows to cowshed\nmow grass',
        'windy': 'wait',
        'neutral': 'fertilize pasture'
    }

print(weather.get('rainy', "the cows are standing in the rain"))
print(weather.get('sunny', "The weather is sunny"))
print(weather.get('windy', "No other action"))
print(weather.get('neutral', "The weather is not sunny or windy"))

time_of_day = {
            'day': 'wait',
            'night': 'take cows to cowshed',
}

print(time_of_day.get('night', "The cows are on the pasture at night"))
print(time_of_day.get('day', "No other action"))

cow_milking_status = 'Need milking' if True else 'Don\'t need milking'
slurry_tank = 'Full' if True else 'Not full'
grass_status = 'Long' if True else 'Short'
    
location_of_the_cows = {
                     'pasture': 'take cows to cowshed',
                     'cowshed': 'milk cows',
}

print(location_of_the_cows.get('pasture', "the cows are on the pasture at night"))
print(location_of_the_cows.get('cowshed', "the cows are in the cowshed"))

season = {
        'winter': 'wait',
        'spring': 'mow grass',
        'summer': 'wait',
        'fall': 'wait',
}

print(season.get('winter', "No other action"))
print(season.get('spring', "The grass is long"))
print(season.get('summer', "No other action"))
print(season.get('fall', "No other action"))

weather = {
        'rainy': 'take cows to cowshed',
        'sunny': 'take cows to cowshed\nmow grass',
        'windy': 'wait',
        'neutral': 'fertilize pasture'
    }

time_of_day = {
            'day': 'wait',
            'night': 'take cows to cowshed',
}


location_of_the_cows = {
                     'pasture': 'take cows to cowshed',
                     'cowshed': 'milk cows',
}

cow_milking_status = 'Need milking' if True else 'Don\'t need milking'

season = {
        'winter': 'wait',
        'spring': 'mow grass',
        'summer': 'wait',
        'fall': 'wait',
}

slurry_tank = 'Full' if True else 'Not full'
grass_status = 'Long' if True else 'Short'

def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    if weather == "rainy" and time_of_day == "night" and location_of_the_cows == "pasture":
        print("take cows to cowshed")
    elif time_of_day == "day" and cow_milking_status == "Need milking" or location_of_the_cows == "pasture":
        print("take cows to cowshed\nmilk cows\ntake cows back to pasture")
    elif weather == "neutral" or location_of_the_cows == 'cowshed' and slurry_tank == "Full":
        print("fertilize pasture")
    elif weather == "sunny" or location_of_the_cows == 'cowshed' or season == "spring" and grass_status == 'long': 
        print("take cows to cowshed\nmow grass\n take cows back to pasture")
    else:
        print("wait")        
        
        
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

