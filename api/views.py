from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
import numpy as np
from django.shortcuts import render

model = joblib.load("linear_regression_model_hhe.pkl")

def index(request):
    return render(request, 'index.html')


class PredictView(APIView):
    def post(self, request):
        print("hehe")
        print(request.data)
        features = request.data.get('features', [])
        print(features)
        if not features or len(features) == 0:
            return Response({'error': 'Dữ liệu đầu vào không hợp lệ'}, status=400)

        features_array = np.array([features])

        prediction = model.predict(features_array)
        print(prediction)
        return Response({'prediction': prediction[0]})
