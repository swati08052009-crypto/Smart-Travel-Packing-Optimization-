# Smart Travel Packing Optimization System

An AI-powered application that helps users pack smartly for their trips by predicting weather, suggesting appropriate items, and calculating luggage weight.

## Features

- 🌤️ **Weather prediction** based on destination and travel dates
- 📦 **Smart packing checklist** generation
- 👕 **Clothing recommendations** by travel reason and season
- ⚖️ **Luggage weight estimation** in kg and lbs
- 🚗 **Transportation mode** suggestions
- 🗺️ **Itinerary-based** packing suggestions
- 📊 **Interactive filtering** and search functionality
- 📥 **Export options** - Print or download as CSV

## Project Structure

```
├── app.py                 # Main Flask application
├── weather_api.py         # Weather prediction module
├── packing_logic.py       # Smart packing checklist logic
├── requirements.txt       # Python dependencies
├── .env.example           # Environment configuration template
├── README.md              # Project documentation
├── templates/
│   └── index.html         # Main HTML frontend
└── static/
    ├── css/
    │   └── style.css      # CSS styling
    └── js/
        └── script.js      # JavaScript functionality
```

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/swati08052009-crypto/Smart-Travel-Packing-Optimizer.git
   cd Smart-Travel-Packing-Optimizer
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
   
   Get a free API key from: https://openweathermap.org/api

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to `http://localhost:5000`

## Usage

1. **Enter Trip Details**:
   - Destination (city name)
   - Start and end dates
   - Trip duration (auto-calculated)
   - Reason for travel (vacation, business, adventure, family)
   - Transportation mode (flight, car, train, etc.)
   - Optional itinerary (beach, hiking, skiing, diving, etc.)

2. **Get Smart Recommendations**:
   - Weather forecast for your destination
   - Personalized packing suggestions
   - Detailed checklist with quantities
   - Total luggage weight in kg and lbs
   - Weight status indicator

3. **Manage Your Checklist**:
   - Filter by category or search by item name
   - Check items off as you pack
   - Print the checklist
   - Download as CSV file

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **APIs**: OpenWeatherMap, Nominatim (OpenStreetMap)
- **Libraries**: 
  - Flask (Web framework)
  - Requests (HTTP library)
  - python-dotenv (Environment variables)
  - Pandas (Data processing)
  - NumPy (Numerical computing)

## API Endpoints

### POST `/api/generate-checklist`
Generates a smart packing checklist based on user input.

**Request Body**:
```json
{
  "destination": "Paris",
  "start_date": "2024-07-15",
  "end_date": "2024-07-22",
  "duration_days": 7,
  "travel_reason": "vacation",
  "transportation": "flight",
  "itinerary": "Beach and city exploration"
}
```

**Response**:
```json
{
  "success": true,
  "weather": { /* weather data */ },
  "checklist": [ /* packing items */ ],
  "total_weight_kg": 18.5,
  "total_weight_lbs": 40.79,
  "recommendations": [ /* personalized tips */ ]
}
```

### POST `/api/calculate-weight`
Calculates total weight of selected items.

### POST `/api/clothing-suggestions`
Gets clothing suggestions based on weather and travel reason.

## Packing Algorithm

The system considers:

1. **Base Essentials** (always included)
   - Passport, documents, medications, toiletries, phone charger, etc.

2. **Travel Reason**
   - Vacation: casual clothes, swimsuits, beach items
   - Business: formal wear, laptop, briefcase
   - Adventure: hiking gear, first aid kit, water bottle
   - Family: varied clothing, entertainment, baby supplies

3. **Weather Conditions**
   - Hot weather (>28°C): light clothes, sunscreen, hats
   - Cold weather (<10°C): heavy jacket, thermal layers, winter accessories
   - Rainy weather: waterproof jacket, umbrella, water-resistant shoes

4. **Transportation Mode**
   - Flight: travel pillow, eye mask, compression socks
   - Car: snacks, sunglasses
   - Train: entertainment, snacks

5. **Duration-based Adjustments**
   - Quantities scale with trip length
   - Toiletries and clothing adjusted accordingly

6. **Itinerary Activities**
   - Beach: additional swimwear, snorkel gear
   - Hiking: boots, backpack, water bottle
   - Skiing: ski jacket, thermal underwear
   - Diving: diving suit, certification documents

## Weight Estimation

- Base luggage weight: 2.5 kg
- Each item has a predefined weight
- Total calculated automatically
- Status indicator:
  - ✓ Light: ≤7 kg
  - ⚠ Moderate: 7-15 kg
  - ⚠ Heavy: 15-23 kg
  - ✗ Very Heavy: >23 kg

## Features in Detail

### Weather Integration
- Real-time weather data from OpenWeatherMap
- 5-day forecast processing
- Temperature, humidity, wind speed, precipitation chance
- Automatic mock data fallback for demonstration

### Smart Recommendations
- Personalized tips based on weather and travel type
- Context-aware suggestions
- Safety and comfort considerations

### User Interface
- Responsive design (mobile, tablet, desktop)
- Smooth animations and transitions
- Intuitive form layout
- Real-time filtering and search
- Print-friendly styling

## Configuration

### Environment Variables

```env
# Weather API
OPENWEATHER_API_KEY=your_api_key_here

# Flask
FLASK_ENV=development
FLASK_DEBUG=True
```

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "API key not found"
**Solution**: Check your `.env` file has the correct OpenWeatherMap API key

### Issue: "Connection refused" on localhost:5000
**Solution**: Make sure Flask is running and port 5000 is not in use

## Future Enhancements

- [ ] User accounts and saved packing lists
- [ ] Integration with online retailers for purchasing
- [ ] Mobile app version
- [ ] Social sharing of packing lists
- [ ] AI-powered item suggestions based on past trips
- [ ] Integration with calendar for event-based packing
- [ ] Multi-language support
- [ ] Real-time collaboration on packing lists

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

## Author

Created with ❤️ for smart travelers

---

**Happy Packing! ✈️🧳**
