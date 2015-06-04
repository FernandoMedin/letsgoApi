from rest_framework.response import Response
from rest_framework.views import APIView

class FaceBook(APIView):

    # POST => /auth/facebook/
    def post(self, request):
        return Response({ "result": request.data })
