resource "supabase_settings" "assignment" {
  project_ref = var.linked_project

  api = jsonencode({
    db_extra_search_path = "public, extensions"
    db_schema           = "public, storage, graphql_public"
    max_rows            = 1000
  })
}