variable "linked_project" {
  type        = string
  description = "Supabase project reference ID"
}

variable "bucket_name" {
  type        = string
  description = "Name of the storage bucket"
}

variable "object_name" {
  type        = string
  description = "Name of the file in the bucket"
}

variable "local_file" {
  type        = string
  description = "Path to local file"
  default     = ""
}