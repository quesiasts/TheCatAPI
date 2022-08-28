def get_project_package(project_dir):
    if (project_dir / "project_name").exists():
        return "project_name"
    return "apps"
