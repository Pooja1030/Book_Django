from google.cloud import aiplatform

# Initialize the AI Platform client
def initialize_client():
    aiplatform.init(project='', location='')  #add project and location

def predict_gemini_model(instance):
    model_id = ''  # add your model ID
    try:
        # Initializing the client
        client = aiplatform.gapic.PredictionServiceClient()

        # Preparing the input data
        endpoint = f"projects/model_id//location/endpoints/{model_id}"   #add model_id,location
        instances = [instance]

        # Perform the prediction
        response = client.predict(endpoint=endpoint, instances=instances)
        return response
    except Exception as e:
        raise RuntimeError(f"Error during prediction: {e}")
