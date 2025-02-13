# Repository Documentation

## Project Structure Overview

The project is divided into two main folders: `frontend` and `backend`.

- **Frontend**: Built with React and Vite. The Node.js version used is 22.18.0.
- **Backend**: Built with Python. The Python version used is 3.10.9.

### Dependencies

- **Frontend**: Dependencies are listed in the `package.json` file inside the `frontend` folder.
- **Backend**: Dependencies are listed in the `requirements.txt` file inside the `backend` folder.

### Setup

#### Frontend

1. Navigate to the `frontend` folder:
    ```bash
    cd frontend
    ```
2. Install the dependencies:
    ```bash
    npm install
    ```
3. Start the project:
    ```bash
    npm run dev
    ```

#### Backend

1. Navigate to the `backend` folder:
    ```bash
    cd backend
    ```
2. Create a new virtual environment:
    ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On Ubuntu:
        ```bash
        source .venv/bin/activate
        ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the application:
    ```bash
    python run.py
    ```

After completing these steps, the project should be up and running.

## Issues

### WebSocket Connection
- **Frontend**: There are issues with the WebSocket connection in the frontend.
- **Backend**: The WebSocket connection in the backend is working correctly.

### Transcription
- The transcription functionality is not working as intended.
- There are no Valid results even when using the tiny model.

#### Troubleshooting Transcription Issues
1. Ensure your microphone is properly connected and working.
2. Verify that the audio input is clear and without significant background noise.
3. Check the backend logs for any errors related to the transcription service.
4. Try using a different model by updating the configuration in the backend.
5. If possible, test the transcription on a GPU-powered system for better performance.

### Testing Environment
- All tests have been conducted on a CPU.
- Testing or working on a GPU-powered system has not been possible.

