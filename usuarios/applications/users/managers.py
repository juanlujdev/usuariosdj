from django.db import models

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    # _create_user creo el SUPERUSER con los campos que yo quiero
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):  # is staff, puede entrar
        # al admin,
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,  # lo trae internamente el baseUser
            is_superuser=is_superuser,  # lo trae internamente el baseUser
            **extra_fields
        )
        user.set_password(password)  # haseamos el password
        user.save(using=self.db)  # using es como hacer referencia con que bbdd vamos a trabajar
        return user

    # create user creo un USER con los campos quye yo quiero, llamnio a mi funcion creadora _create_user
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)  # los False hacen referencia
        # a los is_staff y is_superuser de la funcion de arriba create_user

    def create_superuser(self, username, email, password=None,
                         **extra_fields):  # los extra_fields es cualquier otro atributo
        # que se agrege
        return self._create_user(username, email, password, True, True, **extra_fields)  # el _ del principio es
        # para darle una funcio privada. los True hacen referencia a los is_staff y is_superuser de la funcion de arriba create_user
