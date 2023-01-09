# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
# factors
weather = 'rainy','sunny','windy','neutral'
time_of_day = 'day','night'
cow_milking_status = 'Need milking' if True else 'Don\'t need milking'
location_of_the_cows = 'pasture', 'cowshed'
season = 'winter','spring','summer','fall'
slurry_tank = 'Full' if True else 'Not full'
grass_status = 'Long' if True else 'Short'

# actions
actions = ''

def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status):

    if ((location_of_the_cows == 'pasture' and time_of_day == 'night') or  (location_of_the_cows == 'pasture' and weather == 'rainy')):
        return (actions + 'take cows to cowshed') 
    elif ((location_of_the_cows == 'cowshed' and cow_milking_status == True)):
     return (actions + 'milk cows')
    elif ((slurry_tank == True and location_of_the_cows == 'cowshed') and (weather != 'sunny' and weather != 'windy')):
     return (actions + 'fertilize pasture')
    elif ((location_of_the_cows == 'pasture' and grass_status == True) and (weather == 'sunny' and season == 'spring' and grass_status == True)):
     return (actions + '"take cows to cowshed\nmow grass\n take cows back to pasture"')
    else:
         return('wait')

action = farm_action('sunny', 'day', False, 'pasture', 'spring', False, False)

print(action)
      