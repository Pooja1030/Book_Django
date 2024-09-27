from rest_framework import generics, status
from rest_framework.response import Response
from google.cloud import aiplatform
import logging

# Initialize logging
logger = logging.getLogger(__name__)

# Initialize the AI Platform client
def initialize_client():
    aiplatform.init(project='geminiaiintegration', location='asia-south1')

def predict_gemini_model(instance):
    model_id = '5137103042922938368'  
    endpoint_id = '731381940657061888'  
    
    try:
        # Initializing  the client
        client = aiplatform.gapic.PredictionServiceClient()

        # Preparing the endpoint
        endpoint = f"projects/geminiaiintegration/locations/asia-south1/endpoints/{endpoint_id}"

        instances = [instance]

        logger.info(f"Sending the following instance for prediction: {instances}")

        # Performing the prediction
        response = client.predict(endpoint=endpoint, instances=instances)

        logger.info(f"Received prediction response: {response}")

        if response.predictions:
            return response.predictions[0]  
        else:
            raise RuntimeError("No predictions received.")

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise RuntimeError(f"Error during prediction: {e}")

# Example usage
if __name__ == "__main__":
    initialize_client()
    input_instance = {
        "id": "1",
        "title": "Kalki",
        "author": "Amish",
        "rating": 4.8,
        "stock": 150
    } 
    prediction_response = predict_gemini_model(input_instance)
    print(prediction_response)
