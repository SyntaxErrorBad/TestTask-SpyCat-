from .serializers.cat import CatSerializer
from .serializers.mission import MissionSerializer
from .serializers.target import TargetSerializer
from .serializers.note import NoteSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import Cat, Mission, Target, Note

"""
Cat
"""


class GetAllCatsListAPIView(generics.ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class GetOneCatAPIView(generics.RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'id'


class CatUpdateSalaryAPIView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, id):
        try:
            cat = Cat.objects.get(id = id)

            salary = request.data.get("salary")
            if salary:
                cat.salary = salary

                cat.save()

                serializer = CatSerializer(cat)
                return Response(serializer.data)

            return Response({"detail": "Salary field is required."}, status = status.HTTP_400_BAD_REQUEST)

        except Cat.DoesNotExist:
            return Response({"detail": "Cat not found"}, status = status.HTTP_404_NOT_FOUND)


class CreateNewCatAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cat created successfully', 'data': serializer.data})
        else:
            return Response({'message': 'Invalid data', 'errors': serializer.errors})


class DeleteCatAPIView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, cat_id):
        try:
            cat = Cat.objects.get(id=cat_id)
            cat.delete()
            return Response({"message": "Cat deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Cat.DoesNotExist:
            return Response({"message": "Cat not found"}, status=status.HTTP_404_NOT_FOUND)


"""
Mission
"""


class GetAllMissionsAPIView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class GetOneMissionAPIView(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'id'


class CreateMissionWithTargetsAPIView(APIView):
    def post(self, request):
        serializer = MissionSerializer(data=request.data)

        if serializer.is_valid():
            mission = serializer.save()
            return Response(MissionSerializer(mission).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTargetStatusAPIView(APIView):
    def patch(self, request, mission_id, target_id):
        try:
            mission = Mission.objects.get(id=mission_id)

            target = Target.objects.get(id=target_id, mission=mission)

            target.status = 'completed'
            target.save()

            serializer = TargetSerializer(target)

            return Response({
                "message": "Target status updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Mission.DoesNotExist:
            return Response({"message": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)
        except Target.DoesNotExist:
            return Response({"message": "Target not found for this mission"}, status=status.HTTP_404_NOT_FOUND)


class UpdateNoteAPIView(APIView):
    def patch(self, request, mission_id, target_id, note_id):
        try:
            mission = Mission.objects.get(id=mission_id)

            target = Target.objects.get(id=target_id, mission=mission)

            if mission.status == 'completed' or target.status == 'completed':
                return Response({
                    "message": "Cannot update note. Mission or target is completed."
                }, status=status.HTTP_400_BAD_REQUEST)

            note = Note.objects.get(id=note_id, target=target)

            note_text = request.data.get('note', None)

            if not note_text:
                return Response({"message": "Note text is required to update."},
                                status=status.HTTP_400_BAD_REQUEST)

            note.note = note_text
            note.save()

            serializer = NoteSerializer(note)

            return Response({
                "message": "Note updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Mission.DoesNotExist:
            return Response({"message": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)
        except Target.DoesNotExist:
            return Response({"message": "Target not found for this mission"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"message": "Note not found for this target"}, status=status.HTTP_404_NOT_FOUND)


class AssignCatToMissionAPIView(APIView):
    def patch(self, request, mission_id):
        try:
            mission = Mission.objects.get(id=mission_id)

            if mission.status == 'completed':
                return Response({
                    "message": "Cannot assign cat. Mission is completed."
                }, status=status.HTTP_400_BAD_REQUEST)

            cat_id = request.data.get('cat_id', None)
            if not cat_id:
                return Response({"message": "Cat ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            cat = Cat.objects.get(id=cat_id)

            mission.cat = cat
            mission.save()

            serializer = MissionSerializer(mission)

            return Response({
                "message": "Cat assigned to mission successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Mission.DoesNotExist:
            return Response({"message": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)
        except Cat.DoesNotExist:
            return Response({"message": "Cat not found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteMissionAPIView(APIView):
    def delete(self, request, mission_id):
        try:
            mission = Mission.objects.get(id = mission_id)

            if mission.cat:
                return Response({"message": "Cannot delete mission, it is assigned to a cat."},
                                status = status.HTTP_400_BAD_REQUEST)
            mission.delete()
            return Response({"message": "Mission deleted successfully"}, status = status.HTTP_204_NO_CONTENT)

        except Mission.DoesNotExist:
            return Response({"message": "Mission not found"}, status = status.HTTP_404_NOT_FOUND)