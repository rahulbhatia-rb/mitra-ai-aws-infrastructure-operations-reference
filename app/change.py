def change_ready(change):
 required={"owner","rollback","validation","window"}
 return required <= set(change) and all(change[k] for k in required)
