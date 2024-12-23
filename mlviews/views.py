from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Load the pre-trained model
with open('ml_models/iris_model.pkl', 'rb') as f:
    model = pickle.load(f)


def validate_input_view(request):
    if request.method == 'POST':
        # Get the features from the input
        input_data = request.POST.get('features')
        try:
            # Try to convert input to a numpy array
            features = np.array([float(x) for x in input_data.split(',')])
            
            # Check if the correct number of features (4) is provided
            if len(features) != 4:
                return HttpResponse('<p style="color: red;">Please provide exactly 4 numerical values.</p>')
            
            # If valid
            return HttpResponse('<p style="color: green;">Input is valid!</p>')
        except ValueError:
            # If conversion to float fails
            return HttpResponse('<p style="color: red;">Please enter valid numerical values separated by commas.</p>')
    
    return HttpResponse(status=400)

def predict_view(request):
    if request.method == 'POST':

        input_data = request.POST.get('features')
        input_array = np.array([float(x) for x in input_data.split(',')]).reshape(1, -1)
        
        # Make a prediction
        prediction = model.predict(input_array)[0]
        flower_types = ["Setosa", "Versicolor", "Virginica"]  # Example class names
        prediction_text = flower_types[prediction]
        
        # Return a plain HTML response for the result
        return HttpResponse(f'<p>Prediction Result: <strong>{prediction_text}</strong></p>')
    
    # Render the main page
    return render(request, 'home.html')
