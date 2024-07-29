from google.cloud import storage
import os


def create_bucket(bucket_name, project_id):
    """Creates a new Google Cloud Storage bucket."""

    # Initialize a storage client
    client = storage.Client(project=project_id)

    # Create a bucket object
    bucket = client.bucket(bucket_name)

    # Create the bucket
    try:
        bucket.create(location='US')  # Specify the location, e.g., 'US', 'EU', etc.
        print(f"Bucket {bucket_name} created.")
    except Exception as e:
        print(f"Error creating bucket: {e}")


if __name__ == "__main__":
    # Define bucket name and project ID
    BUCKET_NAME = "my-unique-bucket-name-251094"  # Replace with your bucket name
    PROJECT_ID = "polar-office-422517-t9"  # Replace with your Google Cloud project ID

    # Set the environment variable for the service account
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/priya/terraform_gcp_project/polar-office-422517-t9-25b3de4ef764.json"  # Update the path to your service account key

    # Call the function to create the bucket
    create_bucket(BUCKET_NAME, PROJECT_ID)
