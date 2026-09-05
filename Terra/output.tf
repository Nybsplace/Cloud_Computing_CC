output "public_url" {
  value       = "https://${var.linked_project}.supabase.co/storage/v1/object/public/${var.bucket_name}/${var.object_name}"
  description = "Public URL of the uploaded assignment PDF"
}