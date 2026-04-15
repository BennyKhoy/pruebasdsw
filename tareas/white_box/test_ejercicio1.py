import unittest
from unittest.mock import mock_open, patch

from ejercicio1 import (
    generate_password_hash,
    generate_salt,
    load_user_data,
    login,
    main,
    register,
    save_user_data,
)


class TestGenerateSalt(unittest.TestCase):

    def test_generate_salt_returns_string(self):
        """
        Verifica que devuelve un string
        """
        salt = generate_salt()
        self.assertIsInstance(salt, str)

    def test_generate_salt_length(self):
        """
        Verifica que el salt tenga la longitud correcta
        """
        salt = generate_salt()
        self.assertEqual(len(salt), 32)

    def test_generate_salt_unique(self):
        """
        Verifica que 2 salt generadas sean diferentes
        """
        salt1 = generate_salt()
        salt2 = generate_salt()
        self.assertNotEqual(salt1, salt2)


class TestGeneratePasswordHash(unittest.TestCase):

    def test_generate_password_hash_returns_string(self):
        """
        Verifica que el hash sea un string.
        """
        result = generate_password_hash("contraseña1221", "somesalt")
        self.assertIsInstance(result, str)

    def test_generate_password_same_hash(self):
        """
        Verifica que la misma contraseña y salt generen el mismo hash
        """
        hash1 = generate_password_hash("contraseña1221", "somesalt")
        hash2 = generate_password_hash("contraseña1221", "somesalt")
        self.assertEqual(hash1, hash2)

    def test_generate_password_hash_different_passwords(self):
        """
        Verifica que diferentes contraseñas generen diferente hash
        """
        hash1 = generate_password_hash("contraseña1221", "somesalt")
        hash2 = generate_password_hash("contraseña2121", "somesalt")
        self.assertNotEqual(hash1, hash2)

    def test_generate_password_hash_different_salts(self):
        """
        Verifica que la misma contraseña con salt diferente genere diferente hash
        """
        hash1 = generate_password_hash("contraseña1221", "salt1")
        hash2 = generate_password_hash("contraseña1221", "salt2")
        self.assertNotEqual(hash1, hash2)


class TestLoadUserData(unittest.TestCase):

    @patch("os.path.exists", return_value=True)
    @patch(
        "builtins.open",
        mock_open(read_data='{"alex": {"password_hash": "ghkcu", "salt": "abcd"}}'),
    )
    def test_load_user_data_file_exists(self, mock_exists):
        """
        Verifica que se carga el archivo correctamente si existe
        """
        result = load_user_data()
        self.assertEqual(result, {"alex": {"password_hash": "ghkcu", "salt": "abcd"}})

    @patch("os.path.exists", return_value=False)
    def test_load_user_data_file_not_exists(self, mock_exists):
        """
        Verifica que se devuelve un diccionario vacio si no existe el archivo
        """
        result = load_user_data()
        self.assertEqual(result, {})


class TestSaveUserData(unittest.TestCase):
    @patch("builtins.open", mock_open())
    def test_save_user_data_writes_file(
        self,
    ):
        """
        verifica que se escribe el archivo correctamente
        """
        with patch("builtins.open", mock_open()) as mock_file:
            save_user_data({"alex": {"password_hash": "ghkcu", "salt": "abcd"}})
            mock_file.assert_called_once_with("users.json", "w")


class TestRegister(unittest.TestCase):

    @patch("builtins.print")
    @patch("ejercicio1.save_user_data")
    @patch("builtins.input", return_value="mypassword")
    @patch("ejercicio1.load_user_data", return_value={})
    def test_register_new_user(self, mock_load, mock_input, mock_save, mock_print):
        """
        Verifica que se regisra un nuevo usuario correctamente
        """
        register("alex")
        mock_print.assert_called_with("User registered successfully.")
        mock_save.assert_called_once()

    @patch("builtins.print")
    @patch(
        "ejercicio1.load_user_data",
        return_value={"alex": {"password_hash": "ghkcu", "salt": "abcd"}},
    )
    def test_register_existing_user(self, mock_load, mock_print):
        """
        verifica que no se puede registrar un usuario ya existente
        """
        register("alex")
        mock_print.assert_called_with(
            "User already exists. Please choose a different username."
        )


class TestLogin(unittest.TestCase):
    @patch("builtins.print")
    @patch("ejercicio1.load_user_data", return_value={})
    def test_login_user_not_found(self, mock_load, mock_print):
        """
        verifica que el login falla si el usuario no existe
        """
        login("alex", "password123")
        mock_print.assert_called_with("User does not exist. Please register first.")

    @patch("builtins.print")
    @patch("ejercicio1.load_user_data")
    def test_login_correct_password(self, mock_load, mock_print):
        """
        verifica que el login pasa con la contraseña correcta
        """
        salt = generate_salt()
        password_hash = generate_password_hash("password123", salt)
        mock_load.return_value = {
            "alex": {"password_hash": password_hash, "salt": salt}
        }

        login("alex", "password123")
        mock_print.assert_called_with("Login successful!")

    @patch("builtins.print")
    @patch("ejercicio1.load_user_data")
    def test_login_wrong_password(self, mock_load, mock_print):
        """
        verifica que el login falla con la contraseña incorrecta
        """
        salt = generate_salt()
        password_hash = generate_password_hash("password123", salt)
        mock_load.return_value = {
            "alex": {"password_hash": password_hash, "salt": salt}
        }

        login("alex", "wrongpassword")
        mock_print.assert_called_with("Invalid password. Please try again.")


class TestMain(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["3"])
    def test_exit_immediately(self, mock_input, mock_print):
        """
        verifica que se cierra el programa al usar la opción de salir
        """
        main()
        mock_print.assert_any_call("Exiting...")

    @patch("builtins.print")
    @patch("ejercicio1.register")
    @patch("builtins.input", side_effect=["1", "alex", "3"])
    def test_register_option(self, mock_input, mock_register, mock_print):
        """
        verifica que se llama a register con el nombre correcto al usar register
        """
        main()
        mock_register.assert_called_once_with("alex")

    @patch("builtins.print")
    @patch("ejercicio1.login")
    @patch("builtins.input", side_effect=["2", "alex", "password123", "3"])
    def test_login_option(self, mock_input, mock_login, mock_print):
        """
        verifica que se llama a login con nombre y contraseña correctos al usar login
        """
        main()
        mock_login.assert_called_once_with("alex", "password123")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["99", "3"])
    def test_invalid_option(self, mock_input, mock_print):
        """
        verifica que se imprime el mensaje correcto al seleccionar una invalid choice
        """
        main()
        mock_print.assert_any_call("Invalid choice. Please try again.")
