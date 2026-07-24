from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
# from .models import HealthRecord
# from .serializers import HealthRecordSerializer

class HealthRecordLogView(APIView):
    """
    API endpoint to save a health record for the logged-in user.
    """
    # permission_classes = [IsAuthenticated]  # Protects the endpoint
    permission_classes = [AllowAny]

    # def post(self, request):
    #     serializer = HealthRecordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # Inject the logged-in user context
    #         serializer.save(user=request.user)
    #         return Response(
    #             {"message": "Health data logged", "data": serializer.data}, 
    #             status=status.HTTP_201_CREATED
    #         )
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        API endpoint to retrieve health records for the logged-in user.
        """
        # records = HealthRecord.objects.filter(user=request.user)
        # serializer = HealthRecordSerializer(records, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Health data retrieval endpoint"}, status=status.HTTP_200_OK)