from typing import List, Dict, Tuple

# Packing data based on travel reason, weather, and duration
PACKING_DATABASE = {
    'essentials': [
        {'name': 'Passport', 'quantity': 1, 'weight_kg': 0.05, 'category': 'documents'},
        {'name': 'Travel Documents', 'quantity': 1, 'weight_kg': 0.1, 'category': 'documents'},
        {'name': 'Medications', 'quantity': 1, 'weight_kg': 0.2, 'category': 'health'},
        {'name': 'Toiletries Bag', 'quantity': 1, 'weight_kg': 1.0, 'category': 'toiletries'},
        {'name': 'Underwear', 'quantity': 1, 'weight_kg': 0.3, 'category': 'clothing'},
        {'name': 'Socks', 'quantity': 1, 'weight_kg': 0.2, 'category': 'clothing'},
        {'name': 'Phone Charger', 'quantity': 1, 'weight_kg': 0.15, 'category': 'electronics'},
        {'name': 'Wallet/Money', 'quantity': 1, 'weight_kg': 0.1, 'category': 'valuables'},
    ],
    'vacation': [
        {'name': 'T-Shirt', 'quantity': 4, 'weight_kg': 0.2, 'category': 'clothing'},
        {'name': 'Shorts', 'quantity': 2, 'weight_kg': 0.3, 'category': 'clothing'},
        {'name': 'Casual Pants', 'quantity': 2, 'weight_kg': 0.4, 'category': 'clothing'},
        {'name': 'Casual Shoes', 'quantity': 2, 'weight_kg': 0.5, 'category': 'footwear'},
        {'name': 'Swimsuit', 'quantity': 2, 'weight_kg': 0.2, 'category': 'clothing'},
        {'name': 'Sunglasses', 'quantity': 1, 'weight_kg': 0.05, 'category': 'accessories'},
        {'name': 'Hat/Cap', 'quantity': 1, 'weight_kg': 0.1, 'category': 'accessories'},
        {'name': 'Beach Towel', 'quantity': 1, 'weight_kg': 0.5, 'category': 'accessories'},
        {'name': 'Light Jacket', 'quantity': 1, 'weight_kg': 0.4, 'category': 'clothing'},
    ],
    'business': [
        {'name': 'Formal Shirts', 'quantity': 3, 'weight_kg': 0.25, 'category': 'clothing'},
        {'name': 'Business Pants', 'quantity': 2, 'weight_kg': 0.5, 'category': 'clothing'},
        {'name': 'Blazer', 'quantity': 1, 'weight_kg': 0.8, 'category': 'clothing'},
        {'name': 'Formal Shoes', 'quantity': 1, 'weight_kg': 0.6, 'category': 'footwear'},
        {'name': 'Tie', 'quantity': 2, 'weight_kg': 0.05, 'category': 'accessories'},
        {'name': 'Laptop/Tablet', 'quantity': 1, 'weight_kg': 1.5, 'category': 'electronics'},
        {'name': 'Business Cards', 'quantity': 1, 'weight_kg': 0.02, 'category': 'documents'},
        {'name': 'Portfolio/Briefcase', 'quantity': 1, 'weight_kg': 0.5, 'category': 'luggage'},
    ],
    'adventure': [
        {'name': 'Hiking Boots', 'quantity': 1, 'weight_kg': 0.8, 'category': 'footwear'},
        {'name': 'Sports T-Shirt', 'quantity': 3, 'weight_kg': 0.2, 'category': 'clothing'},
        {'name': 'Hiking Pants', 'quantity': 2, 'weight_kg': 0.4, 'category': 'clothing'},
        {'name': 'Rain Jacket', 'quantity': 1, 'weight_kg': 0.5, 'category': 'clothing'},
        {'name': 'First Aid Kit', 'quantity': 1, 'weight_kg': 0.5, 'category': 'health'},
        {'name': 'Water Bottle', 'quantity': 1, 'weight_kg': 0.5, 'category': 'accessories'},
        {'name': 'Backpack (60L)', 'quantity': 1, 'weight_kg': 2.0, 'category': 'luggage'},
        {'name': 'Torch/Flashlight', 'quantity': 1, 'weight_kg': 0.3, 'category': 'electronics'},
        {'name': 'Energy Bars', 'quantity': 10, 'weight_kg': 0.04, 'category': 'food'},
    ],
    'family': [
        {'name': 'Casual Clothes', 'quantity': 5, 'weight_kg': 0.25, 'category': 'clothing'},
        {'name': 'Kids Clothes', 'quantity': 7, 'weight_kg': 0.15, 'category': 'clothing'},
        {'name': 'Shoes', 'quantity': 2, 'weight_kg': 0.5, 'category': 'footwear'},
        {'name': 'Entertainment Items', 'quantity': 3, 'weight_kg': 0.5, 'category': 'entertainment'},
        {'name': 'Portable Charger', 'quantity': 2, 'weight_kg': 0.3, 'category': 'electronics'},
        {'name': 'Wet Wipes', 'quantity': 1, 'weight_kg': 0.3, 'category': 'toiletries'},
        {'name': 'Baby Supplies', 'quantity': 1, 'weight_kg': 1.5, 'category': 'health'},
    ],
    'hot_weather': [
        {'name': 'Light T-Shirts', 'quantity': 5, 'weight_kg': 0.15, 'category': 'clothing'},
        {'name': 'Shorts', 'quantity': 4, 'weight_kg': 0.2, 'category': 'clothing'},
        {'name': 'Sunscreen', 'quantity': 2, 'weight_kg': 0.5, 'category': 'toiletries'},
        {'name': 'Hat', 'quantity': 2, 'weight_kg': 0.1, 'category': 'accessories'},
        {'name': 'Sunglasses', 'quantity': 1, 'weight_kg': 0.05, 'category': 'accessories'},
        {'name': 'Light Scarf', 'quantity': 1, 'weight_kg': 0.1, 'category': 'clothing'},
    ],
    'cold_weather': [
        {'name': 'Heavy Jacket', 'quantity': 1, 'weight_kg': 1.2, 'category': 'clothing'},
        {'name': 'Thermal Layers', 'quantity': 3, 'weight_kg': 0.3, 'category': 'clothing'},
        {'name': 'Winter Pants', 'quantity': 2, 'weight_kg': 0.5, 'category': 'clothing'},
        {'name': 'Winter Boots', 'quantity': 1, 'weight_kg': 0.8, 'category': 'footwear'},
        {'name': 'Gloves', 'quantity': 2, 'weight_kg': 0.1, 'category': 'accessories'},
        {'name': 'Scarf', 'quantity': 1, 'weight_kg': 0.15, 'category': 'accessories'},
        {'name': 'Beanie', 'quantity': 1, 'weight_kg': 0.1, 'category': 'accessories'},
    ],
    'rainy_weather': [
        {'name': 'Waterproof Jacket', 'quantity': 1, 'weight_kg': 0.6, 'category': 'clothing'},
        {'name': 'Umbrella', 'quantity': 1, 'weight_kg': 0.4, 'category': 'accessories'},
        {'name': 'Waterproof Shoes', 'quantity': 1, 'weight_kg': 0.6, 'category': 'footwear'},
        {'name': 'Quick Dry Clothes', 'quantity': 3, 'weight_kg': 0.2, 'category': 'clothing'},
    ],
}

def generate_packing_checklist(
    destination: str,
    weather_data: Dict,
    travel_reason: str,
    transportation: str,
    duration_days: int = 7,
    itinerary: str = ''
) -> List[Dict]:
    """
    Generate a smart packing checklist based on various parameters
    
    Args:
        destination: Travel destination
        weather_data: Weather information from API
        travel_reason: Type of travel (vacation, business, adventure, family)
        transportation: Mode of transport (flight, car, train, etc.)
        duration_days: Number of days traveling
        itinerary: Optional itinerary details
    
    Returns:
        List of items to pack with quantities and weights
    """
    checklist = []
    
    # Add essentials (always included)
    checklist.extend(PACKING_DATABASE['essentials'])
    
    # Add items based on travel reason
    if travel_reason.lower() in PACKING_DATABASE:
        checklist.extend(PACKING_DATABASE[travel_reason.lower()])
    
    # Add weather-specific items
    temp = weather_data.get('avg_temperature', 20)
    condition = weather_data.get('condition', 'Sunny').lower()
    
    if temp > 28:
        checklist.extend(PACKING_DATABASE['hot_weather'])
    elif temp < 10:
        checklist.extend(PACKING_DATABASE['cold_weather'])
    
    if 'rain' in condition or weather_data.get('precipitation_chance', 0) > 30:
        checklist.extend(PACKING_DATABASE['rainy_weather'])
    
    # Adjust quantities based on duration
    checklist = adjust_quantities_by_duration(checklist, duration_days)
    
    # Add transportation-specific items
    checklist = add_transportation_items(checklist, transportation)
    
    # Add itinerary-specific items
    if itinerary:
        checklist = add_itinerary_items(checklist, itinerary)
    
    # Remove duplicates and merge quantities
    checklist = merge_duplicate_items(checklist)
    
    return checklist

def adjust_quantities_by_duration(checklist: List[Dict], duration_days: int) -> List[Dict]:
    """
    Adjust quantities based on trip duration
    """
    adjusted = []
    
    for item in checklist:
        if item['category'] in ['clothing', 'toiletries']:
            # Adjust based on duration
            multiplier = max(1, duration_days / 7)
            item['quantity'] = max(int(item['quantity'] * multiplier), item['quantity'])
        
        adjusted.append(item)
    
    return adjusted

def add_transportation_items(checklist: List[Dict], transportation: str) -> List[Dict]:
    """
    Add transportation-specific items
    """
    transportation_items = {
        'flight': [
            {'name': 'Travel Pillow', 'quantity': 1, 'weight_kg': 0.3, 'category': 'accessories'},
            {'name': 'Eye Mask', 'quantity': 1, 'weight_kg': 0.05, 'category': 'accessories'},
            {'name': 'Compression Socks', 'quantity': 1, 'weight_kg': 0.1, 'category': 'clothing'},
        ],
        'car': [
            {'name': 'Sunglasses', 'quantity': 1, 'weight_kg': 0.05, 'category': 'accessories'},
            {'name': 'Snacks', 'quantity': 1, 'weight_kg': 0.5, 'category': 'food'},
        ],
        'train': [
            {'name': 'Entertainment', 'quantity': 1, 'weight_kg': 0.3, 'category': 'entertainment'},
            {'name': 'Snacks', 'quantity': 1, 'weight_kg': 0.3, 'category': 'food'},
        ],
    }
    
    if transportation.lower() in transportation_items:
        checklist.extend(transportation_items[transportation.lower()])
    
    return checklist

def add_itinerary_items(checklist: List[Dict], itinerary: str) -> List[Dict]:
    """
    Add items based on itinerary activities
    """
    itinerary_lower = itinerary.lower()
    
    itinerary_items = {
        'beach': [
            {'name': 'Swimsuit', 'quantity': 2, 'weight_kg': 0.2, 'category': 'clothing'},
            {'name': 'Snorkel Gear', 'quantity': 1, 'weight_kg': 0.5, 'category': 'accessories'},
            {'name': 'Beach Towel', 'quantity': 2, 'weight_kg': 0.6, 'category': 'accessories'},
        ],
        'hiking': [
            {'name': 'Hiking Boots', 'quantity': 1, 'weight_kg': 0.8, 'category': 'footwear'},
            {'name': 'Backpack', 'quantity': 1, 'weight_kg': 1.5, 'category': 'luggage'},
            {'name': 'Water Bottle', 'quantity': 1, 'weight_kg': 0.5, 'category': 'accessories'},
        ],
        'mountain': [
            {'name': 'Mountain Climbing Gear', 'quantity': 1, 'weight_kg': 3.0, 'category': 'equipment'},
        ],
        'skiing': [
            {'name': 'Ski Jacket', 'quantity': 1, 'weight_kg': 1.0, 'category': 'clothing'},
            {'name': 'Ski Pants', 'quantity': 1, 'weight_kg': 0.8, 'category': 'clothing'},
            {'name': 'Thermal Underwear', 'quantity': 2, 'weight_kg': 0.3, 'category': 'clothing'},
        ],
        'diving': [
            {'name': 'Diving Suit', 'quantity': 1, 'weight_kg': 2.0, 'category': 'equipment'},
            {'name': 'Diving Certification', 'quantity': 1, 'weight_kg': 0.05, 'category': 'documents'},
        ],
    }
    
    for activity, items in itinerary_items.items():
        if activity in itinerary_lower:
            checklist.extend(items)
    
    return checklist

def merge_duplicate_items(checklist: List[Dict]) -> List[Dict]:
    """
    Merge duplicate items and sum quantities
    """
    items_dict = {}
    
    for item in checklist:
        key = item['name'].lower()
        
        if key in items_dict:
            items_dict[key]['quantity'] += item['quantity']
        else:
            items_dict[key] = item.copy()
    
    return list(items_dict.values())

def calculate_luggage_weight(checklist: List[Dict]) -> float:
    """
    Calculate total weight of all items in the checklist
    
    Args:
        checklist: List of items to pack
    
    Returns:
        Total weight in kilograms
    """
    total_weight = 0.0
    
    for item in checklist:
        weight_per_item = item.get('weight_kg', 0)
        quantity = item.get('quantity', 1)
        total_weight += weight_per_item * quantity
    
    # Add luggage weight (typical luggage weighs 2-3 kg)
    luggage_weight = 2.5
    total_weight += luggage_weight
    
    return round(total_weight, 2)

def get_clothing_by_weather(
    temperature: float,
    condition: str,
    reason: str = 'vacation'
) -> List[Dict]:
    """
    Get clothing suggestions based on weather conditions
    
    Args:
        temperature: Temperature in Celsius
        condition: Weather condition (sunny, rainy, snowy, cloudy)
        reason: Travel reason for context
    
    Returns:
        List of suggested clothing items
    """
    suggestions = []
    
    # Temperature-based suggestions
    if temperature > 30:
        suggestions.extend(PACKING_DATABASE['hot_weather'])
    elif temperature > 20:
        suggestions.append({'name': 'Light Jacket', 'quantity': 1, 'weight_kg': 0.4, 'category': 'clothing'})
    elif temperature > 10:
        suggestions.append({'name': 'Sweater', 'quantity': 1, 'weight_kg': 0.5, 'category': 'clothing'})
    else:
        suggestions.extend(PACKING_DATABASE['cold_weather'])
    
    # Condition-based suggestions
    if 'rain' in condition.lower():
        suggestions.extend(PACKING_DATABASE['rainy_weather'])
    
    return suggestions
