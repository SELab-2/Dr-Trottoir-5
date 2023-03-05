from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
        Custom User Manager to create users. Email is the unique identifier
    """

    def create_user(self, email, password, name, phone_nr, location, access_rights, **other_fields):
        """
            Creates a user with giving parameters.
        :param email: String
        :param password: String
        :param name: String
        :param phone_nr: String
        :param location: ForeignKey
        :param access_rights: SmallInteger
        :param other_fields:
        :return: User
        """
        if email == "":
            raise ValueError(_("Er moet een email adres aanwezig zijn"))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_nr=phone_nr, location=location, access_rights=access_rights,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, phone_nr, location, **other_fields):
        other_fields.setdefault('access_rights', 3)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault("is_superuser", True)

        """
            Error handling when creating a super user
        """
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Bij superuser moet de variable is_staff gelijk zijn aan True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Bij superuser moet de variable is_superuser gelijk zijn aan True."))

        return self.create_user(email, password, name, phone_nr, location, 3, **extra_fields)
