# Oxam-proctoring
A Chrome extension that operates on HecakerEarth websites. Allow user to fill form before starting test and performs a camera and and initiates image proctoring, sending images to the server every one minute. Images are stored in AWS S3 buckets.



## Installation of Chrome extension
1. Clone the repository: git clone https://github.com/webgithuber/Oxam-proctoring.git
2. Open Chrome and navigate to chrome://extensions/
3. Enable Developer Mode by clicking the toggle switch on the top right corner of the page.
4. Click on the "Load unpacked" button and select the root directory of the cloned repository.
5. The extension should now be loaded and active in Chrome.

## Installation of API server
1. Navigate to the current directory using command prompt and create virtual enviornment:`py -m venv env`
2. Activate the virtual enviornment:`.\env\Scripts\activate`
3. Install the required packages: `pip install -r requirements.txt`
4. Set the AWS S3 bucket credentials in the settings.py:
   - `AWS_ACCESS_KEY_ID`: The access key ID for the AWS S3 bucket.
   - `AWS_SECRET_ACCESS_KEY`: The secret access key for the AWS S3 bucket.
   - `AWS_STORAGE_BUCKET_NAME`: The name of the AWS S3 bucket.
5. Navigate to the `exam` directory:`cd exam`
6. Flush the database:`python manage.py flush`
4. Run the database migrations: `py manage.py makemigrations`and `py manage.py migrate`
5. Create a superuser account: `py manage.py createsuperuser`
6. Start the development server: `py manage.py runserver 8000`

## Usage

- To start assesment, go to the `https://www.hackerearth.com/challenges/competitive/dsa-coding-contest-february-23/problems/` URL and fill in the form. You may visit other contest of Heackerearth.
- To make it work for Elitmus test.Make these changes.
   - "matches": ["https://www.elitmus.com/*"], in menifest file.
   - CSRF_TRUSTED_ORIGINS=['https://www.elitmus.com'], in settings.py
   - ["Access-Control-Allow-Origin"]="https://www.elitmus.com", in dashboard/view.py
- To view the dashboard, go to the `http://127.0.0.1:8000/admin-login` URL.

## Documentation
[Documentation](https://drive.google.com/file/d/1tMfOjytwzcMm68KKwY6Ro7SgfV1SMsoz/view?usp=share_link)


