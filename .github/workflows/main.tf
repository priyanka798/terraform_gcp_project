terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.5"
    }
  }

  required_version = ">= 0.12"
}

provider "google" {
  credentials = file("C:/Users/priya/terraform_gcp_project/polar-office-422517-t9-25b3de4ef764.json")
  project     = "polar-office-422517-t9"  # Replace with your actual project ID
  region      = "us-central1"
}

resource "google_storage_bucket" "my_bucket" {
  name     = "my-unique-bucket-name-251094"  # Replace with a valid bucket name
  location = "US"  # Or any other location you prefer

  lifecycle {
    prevent_destroy = true
  }
}
