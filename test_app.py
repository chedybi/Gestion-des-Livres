import unittest
from app import app  # Importez votre application Flask

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        # Configurer une version de test de l'application Flask
        self.app = app.test_client()
        self.app.testing = True

    # Test de la route d'accueil
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenue', response.data)

    # Test de lister les livres (Read)
    def test_lister_livres(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    # Test d'ajouter un livre (Create)
    def test_ajouter_livre(self):
        new_livre = {
            "isbn": "1234567890",
            "titre": "Mon Nouveau Livre",
            "auteur": "Auteur Exemple"
        }
        response = self.app.post('/books', json=new_livre)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Livre ajouté avec succès', response.json.get('message'))

    # Test de modifier un livre (Update)
    def test_modifier_livre(self):
        updated_data = {"titre": "Titre Mis à Jour"}
        response = self.app.put('/books/1234567890', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre mis à jour avec succès', response.json.get('message'))

    # Test de supprimer un livre (Delete)
    def test_supprimer_livre(self):
        response = self.app.delete('/books/1234567890')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre supprimé avec succès', response.json.get('message'))

if __name__ == '__main__':
    unittest.main()
