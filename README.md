# Eastern Cape Eatery Recommender

A web-based application to recommend eateries in the Eastern Cape, South Africa, based on cuisine, location, and budget. Built with [Streamlit](https://streamlit.io/) and deployed via [Streamlit Community Cloud](https://share.streamlit.io/), this app is perfect for foodies exploring East London, Gqeberha, and beyond.

## Features
- **Filter by Cuisine**: Choose from Seafood, African, Italian, and more.
- **Location-Based Search**: Find eateries in specific areas like East London or Gqeberha, or across the entire Eastern Cape.
- **Budget Options**: Select Budget-friendly, Mid-range, or Fine dining.
- **Random Recommendations**: Get up to 3 tailored suggestions with descriptions.
- **Mobile-Friendly**: Access the app via any browser, including on iOS devices.

## Live Demo
Try the app at: [Insert Streamlit URL here after deployment, e.g., `https://your-app-name.streamlit.app`]

## Getting Started

### Prerequisites
- A GitHub account to manage the repository.
- A Streamlit Community Cloud account (free, sign up with GitHub).

### Setup Instructions
1. **Set Up the Repository**:
   - Fork or clone this repository to your GitHub account.
   - Use the GitHub iOS app to create or manage the repository:
     - Open the GitHub iOS app (requires iOS 16+).
     - Tap the “+” icon to create a new repository named `eatery-recommender` (or use an existing one).
     - Initialize with a README if not already present.

2. **Verify or Add Files**:
   - Ensure the following files are in the repository root:
     ```
     ├── streamlit_app.py    # Main Streamlit app code
     ├── requirements.txt    # Dependencies (streamlit==1.38.0)
     └── README.md           # This file
     ```
   - In the GitHub iOS app:
     - Check for `streamlit_app.py` and `requirements.txt`.
     - If missing, tap “Add file” > “Create new file”, paste the contents (see below), and commit.
     - **requirements.txt** should contain:
       ```
       streamlit==1.38.0
       ```

3. **Deploy to Streamlit Community Cloud**:
   - Open Safari on your iOS device and go to [share.streamlit.io](https://share.streamlit.io/).
   - Sign in with your GitHub account.
   - Create a new app:
     - Click “New app” > “From GitHub”.
     - Select your `eatery-recommender` repository.
     - Set the “Main Python file” to `streamlit_app.py`.
     - Deploy (takes ~1-2 minutes).
   - For existing apps:
     - Go to “Manage app” > “Edit settings”.
     - Update “Main Python file” to `streamlit_app.py” if needed.
     - Save and redeploy.
   - Copy the app URL (e.g., `https://your-app-name.streamlit.app`) and update the “Live Demo” section above.

4. **Manage Updates via GitHub iOS App**:
   - Edit files (e.g., add eateries to `streamlit_app.py`) in the GitHub iOS app:
     - Navigate to the file, tap the pencil icon, make changes, and commit.
   - Streamlit auto-redeploys on new commits.
   - Example: Add a new eatery to the `eateries` list in `streamlit_app.py` and commit.

### Local Development (Optional)
To run locally:
1. Install Python 3.8+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt