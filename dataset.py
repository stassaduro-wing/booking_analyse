import csv
import random
from datetime import datetime, timedelta

num_rows = 1050
cities = ['Warsaw', 'Krakow', 'Wroclaw', 'Gdansk', 'Prague', 'Berlin', 'Paris']


filters_data = {
    'rules': ['Free cancellation', 'Early check-in', 'Late check-out'],
    'meals': ['All inclusive', 'All meals', 'Breakfast', 'Dinner', 'Lunch'],
    'pets': [
        'All pets allowed', 'No pet deposit', 'Pet fee less than €20 per night', 'Muzzle not required', 
        'Dogs allowed', 'Allows 3+ pets', 'In-room pet station', 'Additional pet services', 'Cats allowed', 
        'Pets allowed in public areas', 'Pets welcome in the restaurant', 'Pet-welcome bonus', 'Allows 3 pets', 
        '20+ kg pet allowed', 'Pet walking area nearby', 'Up to 20kg pet allowed', 'No pet vaccination required', 
        'Allows 2 pets', 'Up to 15kg pet allowed', 'Towels for pets', 'Toys for pets', 'Unattended pets allowed', 
        'Up to 10kg pet allowed'
    ],
    'parking': ['parking'],
    'accessibility': [
        'Accessible property', 'Step-free access', 'Door width ≥ 80 cm', 'Spacious room layout', 
        'Accessible bed height', 'Accessible bathroom', 'Hard flooring', 'Wheelchair-accessible elevator', 
        'Accessible parking on-site', 'Accessible public areas', 'Accessible room'
    ],
    'facilities': [
        'Bathroom with rain shower', 'Private bathroom', 'Air conditioning', 'King/Queen-size 150+cm width', 
        'Wi-fi', 'Heating', 'Double (full) bed 131-150cm width', 'Coffee/Tea maker', 'Single (twin) bed 80-130cm width', 
        'Soundproof room', 'Elevator/lift access', 'Yoga area', 'Adults only', 'Naturist-friendly', 'Wake-up service', 
        'Allergy-free rooms', 'BBQ facilities', 'Beachfront', 'Private beach area', 'Beach/pool towels', 'Beauty salon/services', 
        'Bike rental/services', 'Blackout curtains', 'Business center', 'Meeting/Conference facilities', 'On-site restaurant', 
        'Bars and lounges (including poolside bar)', 'Grab-and-go snacks (snack bar or vending machines)', 'Casino', 
        'Express check-in/check-out', 'Contactless check-in/out', 'Self check-in', 'Concierge services', 'Connecting rooms', 
        'Currency exchange', 'Work desk', 'Indoor fireplace', 'Children’s pool', 'Game room/arcade', 'Table tennis', 
        'Garden', 'Terrace/Patio', 'Golf course (on-site or nearby)', 'Hair salon', 'On-site medical assistance', 
        'In-room safe', 'Daily housekeeping', 'Minibar', 'Luggage storage', 'EV charging', 'Pillow menu', '24-hour front desk', 
        'Room service', '24-hour security', 'On-site shops', 'Ski access & services', 'Smoke-free property', 
        'Water sports facilities', 'Tennis court', 'Mini golf', 'Tour/ticket assistance', 'Sea view', 'Mountain view', 
        'City view', 'VIP room amenities', 'Water park access', 'Picnic area', 'Crib/Cot available', 'Extra bed available', 
        'Laundry facilities/services', 'Porter/Bellboy service', 'Library', 'Hiking', 'Fishing', 'Sun loungers', 
        'Private entrance', '24/7 kitchen access', 'Bathroom with buthtub', 'Bedside reading lights', 'Fridge', 
        'Microwave', 'Real double bed (not 2 twins pushed together)', 'Room size 30m2 +', 'Safe for toddlers and kids', 'Kitchen'
    ],
    'search_settings': ['Hide no reacted offers', 'Hide liked offers', 'Hide disliked rooms'],
    'kids': [
        'Kids-friendly bathroom', 'Babysitting', 'Child-friendly menu', 'Family-friendly', 
        'Safe balcony', 'TV for kids', 'Playground or Playroom', 'Entertainment for kids'
    ],
    'pool_n_beach': ['Rooftop pool', 'Heated pool', 'Any pool', 'Outdoor pool', 'Indoor pool'],
    'sport': ['Spa', 'Gym', 'Sauna'],
    'transfer': ['Shuttle service'],
    'business': ['Coworking lounge'],
    'other': ['Boutique hotel', 'Design hotel', 'Dutch-speaking staff', 'English-speaking staff', 'Historical building', 'Multilingual staff']
}


ai_scenarios = [
    {"prompt": "quiet hotel with parking and breakfast near center", "city": "Krakow", "parking": "parking", "meals": "Breakfast", "facilities": "Soundproof room"},
    {"prompt": "pet-friendly room with big bed and wifi for work", "city": "Warsaw", "pets": "All pets allowed", "meals": "", "facilities": "Wi-fi,Work desk,King/Queen-size 150+cm width"},
    {"prompt": "cheap hostel for weekend trip with friends", "city": "Wroclaw", "cnt_persons": (3, 5), "max_price": 150, "facilities": "Kitchen"},
    {"prompt": "luxury apartment with pool and gym", "city": "Warsaw", "min_price": 500, "max_price": 2000, "pool_n_beach": "Any pool", "sport": "Gym,Spa", "rating": 5, "score": 9},
    {"prompt": "family room close to beach with kids area", "city": "Gdansk", "kids": "Family-friendly,Playground or Playroom", "facilities": "Beachfront"}
]

headers = [
    'id', 'user_id', 'status', 'created_at', 'closed_at', 'city_of_booking', 'start_date', 'end_date', 
    'cnt_of_person', 'min_price', 'max_price', 'booking_id', 'rules', 'meals', 'pets', 'parking', 
    'accessibility', 'facilities', 'search_settings', 'room_size', 'kids', 'pool_n_beach', 'sport', 
    'transfer', 'business', 'rating', 'score', 'other', 'search_mode', 'ai_chat_id'
]

base_date = datetime(2026, 1, 1, 10, 0, 0)

def get_random_filters(filter_list, max_items=3):
    if random.random() < 0.4:  
        return ""
    num_elements = random.randint(1, min(max_items, len(filter_list)))
    return ", ".join(random.sample(filter_list, num_elements))


with open('booking_activity_dataset.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(num_rows):
        row_id = 100000 + i
        user_id = random.randint(1000, 1500)
        
        search_mode = 'ai' if random.random() < 0.6 else 'manual'
        
        session_duration = random.randint(1, 5) if search_mode == 'ai' else random.randint(5, 25)
        created_at = base_date + timedelta(days=random.randint(0, 140), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        closed_at = created_at + timedelta(minutes=session_duration)
        
        if search_mode == 'ai':
            status = random.choice(['closed', 'booked', 'booked', 'in_progress'])
        else:
            status = random.choice(['closed', 'closed', 'in_progress', 'booked'])
            
        booking_id = random.randint(75000, 100000) if status == 'booked' else ""

        days_ahead = random.randint(2, 30)
        duration_stay = random.randint(1, 7)
        start_date = (created_at + timedelta(days=days_ahead)).date()
        end_date = start_date + timedelta(days=duration_stay)

        city_of_booking = random.choice(cities)
        cnt_persons = random.randint(1, 4)
        min_price = random.choice([0, 50, 100, 150])
        max_price = min_price + random.randint(150, 800)
        
        ai_chat_id = random.randint(5000, 9000) if search_mode == 'ai' else ""
        
        filters = {}
        filters['room_size'] = random.randint(10, 100) if random.random() > 0.3 else 0
        filters['rating'] = random.randint(1, 5) if random.random() > 0.3 else 1
        filters['score'] = random.randint(1, 10) if random.random() > 0.3 else 1

        if search_mode == 'manual':
            for key in filters_data:
                filters[key] = get_random_filters(filters_data[key])
        else:
            scenario = random.choice(ai_scenarios)
            city_of_booking = scenario['city']
            
            if 'cnt_persons' in scenario:
                cnt_persons = random.randint(*scenario['cnt_persons'])
            if 'max_price' in scenario:
                max_price = scenario['max_price']
                min_price = max(0, max_price - random.randint(50, 100))
                
            if 'rating' in scenario:
                filters['rating'] = scenario['rating']
            if 'score' in scenario:
                filters['score'] = scenario['score']

            for key in filters_data:
                if key in scenario:
                    filters[key] = scenario[key]
                else:
                    filters[key] = get_random_filters(filters_data[key], max_items=1) if random.random() < 0.15 else ""

        writer.writerow([
            row_id, user_id, status, created_at.strftime('%Y-%m-%d %H:%M:%S'), closed_at.strftime('%Y-%m-%d %H:%M:%S'),
            city_of_booking, start_date, end_date, cnt_persons, min_price, max_price, booking_id,
            filters.get('rules', ''), filters.get('meals', ''), filters.get('pets', ''), filters.get('parking', ''),
            filters.get('accessibility', ''), filters.get('facilities', ''), filters.get('search_settings', ''), filters['room_size'],
            filters.get('kids', ''), filters.get('pool_n_beach', ''), filters.get('sport', ''), filters.get('transfer', ''),
            filters.get('business', ''), filters['rating'], filters['score'], filters.get('other', ''),
            search_mode, ai_chat_id
        ])
