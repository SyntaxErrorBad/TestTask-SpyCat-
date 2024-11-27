from django.urls import path
from django.urls import include
from .views import GetAllCatsListAPIView, GetOneCatAPIView, CatUpdateSalaryAPIView,  \
    CreateNewCatAPIView, DeleteCatAPIView
from .views import GetAllMissionsAPIView, GetOneMissionAPIView, UpdateTargetStatusAPIView, \
    UpdateNoteAPIView, AssignCatToMissionAPIView, CreateMissionWithTargetsAPIView, DeleteMissionAPIView


app_name = 'api'

mission = [
    path('all/', GetAllMissionsAPIView.as_view(), name='all-missions'),
    path('one/<int:id>', GetOneMissionAPIView.as_view(), name='all-missions'),
    path('update/mission/<int:mission_id>/<int:target_id>/', UpdateTargetStatusAPIView.as_view(),
         name='update-mission-target'),
    path('update/note/<int:mission_id>/<int:target_id>/<int:note_id>/', UpdateNoteAPIView.as_view(),
         name='update-mission-target-note'),
    path('assign/<int:mission_id>/', AssignCatToMissionAPIView.as_view(), name='assign-cat'),
    path('create/', CreateMissionWithTargetsAPIView.as_view(), name='mission-with-target'),
    path('delete/<int:mission_id>/', DeleteMissionAPIView.as_view(), name='delete-mission'),
]

cat = [
    path('all/', GetAllCatsListAPIView.as_view(), name='all-cats'),
    path('one/<int:id>/', GetOneCatAPIView.as_view(), name='one-cat'),
    path('one/<int:id>/update_salary/', CatUpdateSalaryAPIView.as_view(), name='one-cat-update-salary'),
    path('create/', CreateNewCatAPIView.as_view(), name='create-cat'),
    path('delete/<int:cat_id>/', DeleteCatAPIView.as_view(), name='delete-cat'),
]

urlpatterns = [
    path('cat/', include(cat)),
    path('mission/', include(mission))
]
