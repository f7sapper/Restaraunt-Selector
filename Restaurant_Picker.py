import random
from datetime import datetime, timedelta

# List of cuisine types
cuisine_types = ['Italian', 'Chinese', 'Mexican', 'Japanese', 'Wings', 'American', 'BBQ']

# Dictionary of restaurants for each cuisine type
restaurants_dict = {
    'Italian': ['Olive Garden', 'Fazoli\'s', 'Carrabba\'s', 'PennePazze Murfreesboro', 'La Tavola Ristorante Italiano', 
                'Sorelles Italian Restaurant and Pizza', 'Maria\'s on the Square'],
    'Chinese': ['Panda Express', 'Fu Sing', 'Teriyaki Madness'],
    'Mexican': ['Camino Real', 'Taco Bell', 'Cinco De Mayo', 'West 22 Tacos'],
    'Japanese': ['Toki House', 'Wasabi Japanese Steak house', 'Koji Express Japanese Grill', 'Poke Fun', 'Sushin', 'Hokkaido Ramen House',
                 'Wako japanese Cusine'],
    'Wings': ['Toots', 'Buffalo Wild Wings', 'MJ\'s', 'Jefferson\'s'],
    'American': ['Texas Roadhouse', 'Triple B\'s', 'Jonathan\'s Grille', 'Firebirds', 'Bar Louie\'s', 'Cajun Steamer', 'Longhorn Steakhouse',
                  'Miller\'s Ale House', 'The Alley on Main'],
    'BBQ': ['Single Tree', 'Puckett\'s', 'Slick Pig BBQ', 'Martin\'s BBQ', 'Edely\'s', 'Peg Leg Porker']
    }

# Log to store past 14 days of cuisine and restaurant choices
selection_log = []

def clean_log(log, days=14):
    """Remove entries older than a specified number of days."""
    cutoff_date = datetime.now() - timedelta(days=days)
    return [entry for entry in log if entry['date'] >= cutoff_date]

def random_restaurant_generator(log, restaurants_dict):
    # Clean up the log to remove entries older than 14 days
    log = clean_log(log)
    
    # Get available cuisines and restaurants that are not in the log
    available_cuisines = []
    available_restaurants = {}
    for cuisine in cuisine_types:
        # Find restaurants not in the log for this cuisine
        available_restaurants[cuisine] = [r for r in restaurants_dict[cuisine] if r not in [entry['restaurant'] for entry in log]]
        # Only add cuisine to available_cuisines if it has restaurants left
        if available_restaurants[cuisine]:
            available_cuisines.append(cuisine)
    
    # Check if there are available cuisines and restaurants
    if not available_cuisines:
        print("All cuisines or restaurants have been used in the last 14 days. Resetting selection log.")
        log.clear()
        available_cuisines = cuisine_types
        available_restaurants = {cuisine: list(restaurants_dict[cuisine]) for cuisine in cuisine_types}
    
    # Pick a random cuisine type
    cuisine = random.choice(available_cuisines)
    
    # Pick a random restaurant based on the cuisine type
    restaurant = random.choice(available_restaurants[cuisine])
    
    # Add the selection to the log with the current date
    log.append({'cuisine': cuisine, 'restaurant': restaurant, 'date': datetime.now()})
    
    return f"How about some {cuisine} food? Try {restaurant}!", log

# Example usage
result, selection_log = random_restaurant_generator(selection_log, restaurants_dict)
print(result)
