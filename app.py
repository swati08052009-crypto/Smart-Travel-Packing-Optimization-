from flask import Flask, render_template, request, jsonify
from weather_api import get_weather_data
from packing_logic import generate_packing_checklist, calculate_luggage_weight
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/generate-checklist', methods=['POST'])
def generate_checklist():
    """
    Generate a smart packing checklist based on user input
    
    Expected JSON payload:
    {
        'destination': 'Paris',
        'start_date': '2024-07-15',
        'end_date': '2024-07-22',
        'travel_reason': 'vacation',  # vacation, business, adventure, family
        'transportation': 'flight',   # flight, car, train, etc.
        'itinerary': 'Beach and city exploration'  # optional
    }
    """
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['destination', 'start_date', 'end_date', 'travel_reason', 'transportation']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Get weather data
        weather_data = get_weather_data(
            destination=data['destination'],
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        
        if not weather_data:
            return jsonify({'error': 'Unable to fetch weather data'}), 500
        
        # Generate packing checklist
        checklist = generate_packing_checklist(
            destination=data['destination'],
            weather_data=weather_data,
            travel_reason=data['travel_reason'],
            transportation=data['transportation'],
            duration_days=(data.get('duration_days') or 7),
            itinerary=data.get('itinerary', '')
        )
        
        # Calculate luggage weight
        total_weight = calculate_luggage_weight(checklist)
        
        response = {
            'success': True,
            'weather': weather_data,
            'checklist': checklist,
            'total_weight_kg': total_weight,
            'total_weight_lbs': round(total_weight * 2.20462, 2),
            'recommendations': generate_recommendations(weather_data, data['travel_reason'])
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/calculate-weight', methods=['POST'])
def calculate_weight():
    """
    Calculate the weight of selected items
    
    Expected JSON payload:
    {
        'items': [
            {'name': 'T-shirt', 'quantity': 3, 'weight_per_item': 0.2},
            ...
        ]
    }
    """
    try:
        data = request.json
        items = data.get('items', [])
        
        total_weight = 0
        item_details = []
        
        for item in items:
            weight = item.get('quantity', 1) * item.get('weight_per_item', 0)
            total_weight += weight
            item_details.append({
                'name': item.get('name'),
                'quantity': item.get('quantity'),
                'weight_per_item_kg': item.get('weight_per_item'),
                'total_item_weight_kg': round(weight, 2)
            })
        
        return jsonify({
            'success': True,
            'items': item_details,
            'total_weight_kg': round(total_weight, 2),
            'total_weight_lbs': round(total_weight * 2.20462, 2)
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clothing-suggestions', methods=['POST'])
def get_clothing_suggestions():
    """
    Get clothing suggestions based on weather and travel reason
    
    Expected JSON payload:
    {
        'temperature': 25,
        'weather_condition': 'sunny',  # sunny, rainy, snowy, cloudy
        'travel_reason': 'vacation'
    }
    """
    try:
        data = request.json
        from packing_logic import get_clothing_by_weather
        
        suggestions = get_clothing_by_weather(
            temperature=data.get('temperature'),
            condition=data.get('weather_condition'),
            reason=data.get('travel_reason')
        )
        
        return jsonify({
            'success': True,
            'suggestions': suggestions
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_recommendations(weather_data, travel_reason):
    """
    Generate personalized recommendations based on weather and travel reason
    """
    recommendations = []
    
    avg_temp = weather_data.get('avg_temperature', 20)
    condition = weather_data.get('condition', 'sunny')
    
    if avg_temp > 30:
        recommendations.append('Pack light, breathable clothing for hot weather')
        recommendations.append('Don\'t forget sunscreen and sunglasses')
    elif avg_temp < 10:
        recommendations.append('Pack warm layers and a heavy jacket')
        recommendations.append('Include winter accessories like gloves and scarves')
    
    if 'rain' in condition.lower():
        recommendations.append('Bring a waterproof jacket and umbrella')
        recommendations.append('Consider water-resistant shoes')
    
    if travel_reason == 'business':
        recommendations.append('Pack formal wear and professional shoes')
        recommendations.append('Ensure you have business documents organized')
    elif travel_reason == 'adventure':
        recommendations.append('Pack sturdy, comfortable hiking shoes')
        recommendations.append('Include first aid kit and emergency supplies')
    elif travel_reason == 'family':
        recommendations.append('Remember essentials for all family members')
        recommendations.append('Pack entertainment and comfort items for children')
    
    return recommendations

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
