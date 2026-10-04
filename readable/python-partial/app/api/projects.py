# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/projects.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _out


# NOT DECOMPILED: list_projects


# Original qualified name: create_project
def create_project(body, db):
    p = svc.create_project(db, body.name, body.output_folder, body.
        default_config, body.kind)
    return _out(db, p)



# Original qualified name: get_project
def get_project(project_id, db):
    return _out(db, svc.get_project(db, project_id))



# Original qualified name: update_project
def update_project(project_id, body, db):
    p = svc.update_project(db, project_id, name=body.name, default_config=body.
        default_config)
    return _out(db, p)



# Original qualified name: delete_project
def delete_project(project_id, delete_files, db):
    svc.delete_project(db, project_id, delete_files)
    return {'deleted': project_id}



# NOT DECOMPILED: copy_asset


# NOT DECOMPILED: get_project_asset
