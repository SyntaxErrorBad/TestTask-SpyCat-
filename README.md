# PROJECT: SpyCatAgency
## DESCRIPTION
The project aims to create an API for working with cats, missions, tasks within missions, and notes. This allows fetching specific data from the API through defined endpoints.

## REQUIREMENTS

- Python >= 3.8
- pip >= 21.0

**WARNING: MAKE SURE YOU FOLLOW ALL INSTALLATION STEPS BEFORE RUNNING THE APPLICATION.**

1. **CLONE THE REPOSITORY**:
    ```bash
    git clone https://github.com/SyntaxErrorBad/TestTask-SpyCat-
    ```
2. **CREATE A VIRTUAL ENVIRONMENT**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```
3. **INSTALL DEPENDENCIES**:
    ```bash
    pip install -r requirements.txt
    ```
4. **NAVIGATE TO THE WORKING DIRECTORY**:
    ```bash
    cd SpyCatAgency
    ```

**IMPORTANT**: MAKE SURE YOU HAVE INSTALLED ALL THE DEPENDENCIES BEFORE RUNNING THE APPLICATION.

**To run locally**

1. **CREATE A .env FILE**:
    `Or simply modify the .env.sample file and insert the required values`
2. **SET UP THE DATABASE**:
    `Set up the database if necessary`
3. **CONFIGURE THE settings.py FILE** 
    `Configure the settings.py file as per your requirements`
4. **TO START THE SERVER**:
    ```bash
    python manage.py runserver       
    ```

## ENDPOINT: Missions

1. **`/mission/all/`**  
   **Method**: GET  
   **Description**: Retrieve the list of all missions.  
   **Class**: `GetAllMissionsAPIView`  
   This endpoint returns a list of all missions in the system.

2. **`/mission/one/<int:id>/`**  
   **Method**: GET  
   **Description**: Retrieve a specific mission by its ID.  
   **Class**: `GetOneMissionAPIView`  
   This endpoint allows you to fetch details of a mission using the specified ID.

3. **`/mission/update/mission/<int:mission_id>/<int:target_id>/`**  
   **Method**: PATCH  
   **Description**: Update the status of a target for a specific mission.  
   **Class**: `UpdateTargetStatusAPIView`  
   This endpoint allows you to update the target status within a mission using the mission and target IDs.

4. **`/mission/update/note/<int:mission_id>/<int:target_id>/<int:note_id>/`**  
   **Method**: PATCH  
   **Description**: Update a note for a specific target in a mission.  
   **Class**: `UpdateNoteAPIView`  
   This endpoint allows you to update an existing note for a specific target in a mission using the mission, target, and note IDs.

5. **`/mission/assign/<int:mission_id>/`**  
   **Method**: POST  
   **Description**: Assign a cat to a mission.  
   **Class**: `AssignCatToMissionAPIView`  
   This endpoint allows you to assign a cat to a specific mission using the mission ID.

6. **`/mission/create/`**  
   **Method**: POST  
   **Description**: Create a new mission with targets.  
   **Class**: `CreateMissionWithTargetsAPIView`  
   This endpoint allows you to create a new mission along with its targets.

7. **`/mission/delete/<int:mission_id>/`**  
   **Method**: DELETE  
   **Description**: Delete a specific mission.  
   **Class**: `DeleteMissionAPIView`  
   This endpoint allows you to delete a mission using its ID.

## ENDPOINT: Cats

1. **`/cat/all/`**  
   **Method**: GET  
   **Description**: Retrieve the list of all cats.  
   **Class**: `GetAllCatsListAPIView`  
   This endpoint returns a list of all cats in the system.

2. **`/cat/one/<int:id>/`**  
   **Method**: GET  
   **Description**: Retrieve information about a specific cat by its ID.  
   **Class**: `GetOneCatAPIView`  
   This endpoint allows you to fetch the details of a cat using its ID.

3. **`/cat/one/<int:id>/update_salary/`**  
   **Method**: PATCH  
   **Description**: Update the salary of a cat.  
   **Class**: `CatUpdateSalaryAPIView`  
   This endpoint allows you to update a cat’s salary using the cat’s ID.

4. **`/cat/create/`**  
   **Method**: POST  
   **Description**: Create a new cat.  
   **Class**: `CreateNewCatAPIView`  
   This endpoint allows you to add a new cat to the system.

5. **`/cat/delete/<int:cat_id>/`**  
   **Method**: DELETE  
   **Description**: Delete a specific cat.  
   **Class**: `DeleteCatAPIView`  
   This endpoint allows you to delete a cat using its ID.

## How to use the API

1. First, set up the server as described in the **Installation** section.
2. Use tools like Postman or curl to make requests to the API.
3. Note: Authentication is not required as all endpoints are public. Don’t forget to add `host/api/` followed by the endpoints listed above.
