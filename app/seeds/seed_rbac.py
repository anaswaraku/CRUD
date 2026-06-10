from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.permission import Permission
from app.models.role import Role


ROLES = [
    {
        "name": "Admin",
        "description": "System Administrator"
    },
    {
        "name": "Manager",
        "description": "Department Manager"
    },
    {
        "name": "user",
        "description": "Regular User"
    }
]


PERMISSIONS = [
    "user.create",
    "user.read",
    "user.delete",
    "user.update",
    "role.create",
    "role.read",
    "role.delete",
    "role.update"
]


def seed():
    db = SessionLocal()

    try:
        # ✅ Seed roles
        for role_data in ROLES:
            name = role_data["name"]
            description = role_data["description"]

            role = db.scalar(
                select(Role).where(Role.name == name)
            )

            if not role:
                db.add(
                    Role(
                        name=name,
                        description=description
                    )
                )

        # ✅ Seed permissions
        for code in PERMISSIONS:
            permission = db.scalar(
                select(Permission).where(
                    Permission.code == code
                )
            )

            if not permission:
                db.add(
                    Permission(
                        code=code,
                        description=code
                    )
                )

        db.commit()
        print("RBAC seed completed ✅")

    finally:
        db.close()


if __name__ == "__main__":
    seed()