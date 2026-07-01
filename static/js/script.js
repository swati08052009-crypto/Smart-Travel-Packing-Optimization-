// Smart Travel Packing Optimizer - Frontend JavaScript

// Global variables
let currentChecklist = [];
let currentWeatherData = {};
let currentRecommendations = [];

// Form submission
document.getElementById('packingForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    await generateChecklist();
});

// Generate packing checklist
async function generateChecklist() {
    const destination = document.getElementById('destination').value;
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const durationDays = parseInt(document.getElementById('durationDays').value) || 7;
    const travelReason = document.getElementById('travelReason').value;
    const transportation = document.getElementById('transportation').value;
    const itinerary = document.getElementById('itinerary').value;

    // Validation
    if (!destination || !startDate || !endDate || !travelReason || !transportation) {
        alert('Please fill in all required fields');
        return;
    }

    // Show loading spinner
    showLoadingSpinner(true);
    hideResultsSection();

    try {
        const payload = {
            destination,
            start_date: startDate,
            end_date: endDate,
            duration_days: durationDays,
            travel_reason: travelReason,
            transportation,
            itinerary
        };

        const response = await fetch('/api/generate-checklist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to generate checklist');
        }

        const data = await response.json();

        if (data.success) {
            currentChecklist = data.checklist;
            currentWeatherData = data.weather;
            currentRecommendations = data.recommendations;

            displayWeatherInfo(data.weather);
            displayRecommendations(data.recommendations);
            displayChecklist(data.checklist);
            displayWeightSummary(data.total_weight_kg, data.total_weight_lbs);

            showLoadingSpinner(false);
            showResultsSection();
            scrollToResults();
        } else {
            throw new Error('Failed to generate checklist');
        }
    } catch (error) {
        console.error('Error:', error);
        showLoadingSpinner(false);
        alert('Error: ' + error.message);
    }
}

// Display weather information
function displayWeatherInfo(weatherData) {
    const weatherInfo = document.getElementById('weatherInfo');
    weatherInfo.innerHTML = '';

    const items = [
        { label: 'Location', value: weatherData.destination || 'Unknown' },
        { label: 'Avg Temperature', value: `${weatherData.avg_temperature}°C` },
        { label: 'Min Temperature', value: `${weatherData.min_temperature}°C` },
        { label: 'Max Temperature', value: `${weatherData.max_temperature}°C` },
        { label: 'Condition', value: weatherData.condition || 'Unknown' },
        { label: 'Humidity', value: `${weatherData.humidity}%` },
        { label: 'Wind Speed', value: `${weatherData.wind_speed} km/h` },
        { label: 'Precipitation Chance', value: `${weatherData.precipitation_chance}%` }
    ];

    items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'info-item';
        div.innerHTML = `
            <div class="info-item-label">${item.label}</div>
            <div class="info-item-value">${item.value}</div>
        `;
        weatherInfo.appendChild(div);
    });
}

// Display recommendations
function displayRecommendations(recommendations) {
    const recommendationsList = document.getElementById('recommendationsList');
    recommendationsList.innerHTML = '';

    recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.textContent = rec;
        recommendationsList.appendChild(li);
    });
}

// Display packing checklist
function displayChecklist(checklist) {
    const tableBody = document.getElementById('checklistTableBody');
    tableBody.innerHTML = '';

    checklist.forEach((item, index) => {
        const totalWeight = (item.weight_kg * item.quantity).toFixed(2);
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td><span class="category-badge">${item.category}</span></td>
            <td>${item.quantity}</td>
            <td>${item.weight_kg}</td>
            <td>${totalWeight}</td>
            <td><input type="checkbox" id="item-${index}"></td>
        `;
        tableBody.appendChild(row);
    });
}

// Display weight summary
function displayWeightSummary(totalKg, totalLbs) {
    const weightSummary = document.getElementById('weightSummary');
    weightSummary.innerHTML = `
        <div class="weight-item">
            <div class="weight-item-label">Total Weight</div>
            <div class="weight-item-value">${totalKg} kg</div>
        </div>
        <div class="weight-item" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
            <div class="weight-item-label">Weight in Pounds</div>
            <div class="weight-item-value">${totalLbs} lbs</div>
        </div>
        <div class="weight-item" style="background: linear-gradient(135deg, #10b981, #059669);">
            <div class="weight-item-label">Status</div>
            <div class="weight-item-value">${getWeightStatus(totalKg)}</div>
        </div>
    `;
}

// Get weight status
function getWeightStatus(weightKg) {
    if (weightKg <= 7) return '✓ Light';
    if (weightKg <= 15) return '⚠ Moderate';
    if (weightKg <= 23) return '⚠ Heavy';
    return '✗ Very Heavy';
}

// Filter functionality
document.getElementById('filterInput').addEventListener('input', (e) => {
    const filter = e.target.value.toLowerCase();
    filterChecklist(filter, '');
});

document.getElementById('categoryFilter').addEventListener('change', (e) => {
    const category = e.target.value;
    const filter = document.getElementById('filterInput').value.toLowerCase();
    filterChecklist(filter, category);
});

function filterChecklist(filter, category) {
    const rows = document.querySelectorAll('#checklistTableBody tr');
    rows.forEach(row => {
        const itemName = row.querySelector('td').textContent.toLowerCase();
        const itemCategory = row.querySelector('.category-badge').textContent;
        
        let show = true;
        if (filter && !itemName.includes(filter)) show = false;
        if (category && itemCategory !== category) show = false;
        
        row.style.display = show ? '' : 'none';
    });
}

// Print checklist
function printChecklist() {
    window.print();
}

// Download checklist as CSV
function downloadChecklist() {
    let csv = 'Item,Category,Quantity,Weight (kg),Total Weight (kg)\n';
    
    currentChecklist.forEach(item => {
        const totalWeight = (item.weight_kg * item.quantity).toFixed(2);
        csv += `"${item.name}","${item.category}",${item.quantity},${item.weight_kg},${totalWeight}\n`;
    });

    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `packing-checklist-${new Date().toISOString().split('T')[0]}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Reset form
function resetForm() {
    document.getElementById('packingForm').reset();
    hideResultsSection();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// UI Helper Functions
function showLoadingSpinner(show) {
    const spinner = document.getElementById('loadingSpinner');
    if (show) {
        spinner.classList.remove('hidden');
    } else {
        spinner.classList.add('hidden');
    }
}

function showResultsSection() {
    document.getElementById('resultsSection').classList.remove('hidden');
}

function hideResultsSection() {
    document.getElementById('resultsSection').classList.add('hidden');
}

function scrollToResults() {
    const resultsSection = document.getElementById('resultsSection');
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Set minimum date to today
window.addEventListener('DOMContentLoaded', () => {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('startDate').setAttribute('min', today);
    document.getElementById('endDate').setAttribute('min', today);

    // Set default duration
    document.getElementById('durationDays').addEventListener('change', (e) => {
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;
        
        if (startDate && endDate) {
            const start = new Date(startDate);
            const end = new Date(endDate);
            const diffTime = Math.abs(end - start);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            document.getElementById('durationDays').value = diffDays;
        }
    });
});

// Add category badge styling
const style = document.createElement('style');
style.textContent = `
    .category-badge {
        display: inline-block;
        padding: 4px 8px;
        background: #e0e7ff;
        color: #3730a3;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 500;
    }
`;
document.head.appendChild(style);
