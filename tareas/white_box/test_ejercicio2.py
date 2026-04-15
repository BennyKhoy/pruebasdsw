import unittest
from unittest.mock import patch

from ejercicio2 import Song, SongStore, main


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Party mj", "Cris mj", "Malvekes", 2025)

    def test_initialize_song(self):
        """
        Verifica que Song se inicializa correctamente
        """
        self.assertEqual(self.song.title, "Party mj")
        self.assertEqual(self.song.author, "Cris mj")
        self.assertEqual(self.song.album, "Malvekes")
        self.assertEqual(self.song.year, 2025)

    @patch("builtins.print")
    def test_display_song(self, mock_print):
        """
        Verifica que display imprime la información de la canción
        """
        self.song.display()

        mock_print.assert_any_call("Title: Party mj")
        mock_print.assert_any_call("Author: Cris mj")
        mock_print.assert_any_call("Album: Malvekes")
        mock_print.assert_any_call("Year: 2025")


class TestSongStore(unittest.TestCase):
    def setUp(self):
        self.store = SongStore()
        self.song = Song("Party mj", "Cris mj", "Malvekes", 2025)

    def test_initialize_store(self):
        """
        Verifica que el store se inicializa vacio
        """
        self.assertEqual(self.store.songs, [])

    @patch("builtins.print")
    def test_add_song(self, mock_print):
        """
        Verifica agregar una canción
        """
        self.store.add_song(self.song)
        self.assertEqual(len(self.store.songs), 1)
        mock_print.assert_called_with("Song 'Party mj' added to the store.")

    @patch("builtins.print")
    def test_display_songs_empty(self, mock_print):
        """
        Verifica el mensaje cuando no hay canciones en la tienda
        """
        self.store.display_songs()
        mock_print.assert_called_with("No songs in the store.")

    @patch("builtins.print")
    def test_display_songs_with_items(self, mock_print):
        """
        Verifica que se muestran las canciones cuando si hay canciones en la tienda
        """
        self.store.add_song(self.song)
        self.store.display_songs()

        mock_print.assert_any_call("Songs available in the store:")

    @patch("builtins.print")
    def test_search_song_found(self, mock_print):
        """
        Verifica la búsqueda de canciones por titulo
        """
        self.store.add_song(self.song)
        self.store.search_song("Party mj")

        mock_print.assert_any_call("Found 1 song(s) with title 'Party mj':")

    @patch("builtins.print")
    def test_search_song_not_found(self, mock_print):
        """
        Verifica el caso cuando no se encuentra una canción por titulo
        """
        self.store.search_song("Después de la 1")

        mock_print.assert_called_with("No song found with title 'Después de la 1'.")

    @patch("builtins.print")
    def test_search_song_case_insensitive(self, mock_print):
        """
        Verifica que acepta la búsqueda acepta mayúsculas o minúsculas
        """
        self.store.add_song(self.song)
        self.store.search_song("PARTY MJ")

        mock_print.assert_any_call("Found 1 song(s) with title 'PARTY MJ':")


class TestMain(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input", side_effect=["4"])
    def test_exit_immediately(self, mock_input, mock_print):
        """
        Verifica que se cierra el programa al usar la opción de salir
        """
        main()
        mock_print.assert_any_call("Exiting...")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "4"])
    def test_display_songs_empty_then_exit(self, mock_input, mock_print):
        """
        Verifica que se muestra el mensaje correcto cuando no hay canciones y se cierra el programa
        """
        main()
        mock_print.assert_any_call("No songs in the store.")
        mock_print.assert_any_call("Exiting...")

    @patch("builtins.print")
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "Party mj",
            "Cris mj",
            "Malvekes",
            "2025",
            "1",
            "4",
        ],
    )
    def test_add_and_display_song(self, mock_input, mock_print):
        """
        Verifica que se agrega una canción y se muestra
        """
        main()
        mock_print.assert_any_call("Song 'Party mj' added to the store.")
        mock_print.assert_any_call("Songs available in the store:")
        mock_print.assert_any_call("Title: Party mj")

    @patch("builtins.print")
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "Party mj",
            "Cris mj",
            "Malvekes",
            "2025",
            "2",
            "Party mj",
            "4",
        ],
    )
    def test_search_existing_song(self, mock_input, mock_print):
        """
        Verifica que se puede buscar una canción existente
        """
        main()
        mock_print.assert_any_call("Found 1 song(s) with title 'Party mj':")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["2", "Después de la 1", "4"])
    def test_search_non_existing_song(self, mock_input, mock_print):
        """
        Verifica que se muestra el mensaje correcto al buscar una canción que no existe
        """
        main()
        mock_print.assert_any_call("No song found with title 'Después de la 1'.")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["99", "4"])
    def test_invalid_option(self, mock_input, mock_print):
        """
        Verifica que se muestra el mensaje correcto al seleccionar una opción inválida
        """
        main()
        mock_print.assert_any_call("Invalid choice. Please try again.")