from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """teste criando um novo usuario com um email bem sucedido """
        email = 'ernane@usp.br'
        password = '10anovele'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_emailo_normalized(self):
        """ testa se o email esta normalizado"""
        email = 'ernane@USP.BR'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ testa se o sistema cria um usuario sem email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """tea a cração de um super usuário """
        user = get_user_model().objects.create_superuser(
            'test@usp.br',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
