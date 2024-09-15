import unittest
from unittest.mock import patch, MagicMock
import requests
from app import get_stats_every_5_seconds, get_all_vehicles, add_vehicle, get_all_races, add_race

# Définition de la classe de tests pour les différentes fonctions
class TestAppFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_get_stats_every_5_seconds(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'race_id': 1, 'date': '2023-09-01T12:00:00', 'distance': 50, 'speed': 80, 'battery': 90}]}
        mock_get.return_value = mock_response
        
        result = get_stats_every_5_seconds()

        # Vérification du résultat
        self.assertIsNotNone(result)
        self.assertEqual(result['data'][0]['race_id'], 1)
        self.assertEqual(result['data'][0]['speed'], 80)

    @patch('requests.get')
    def test_get_all_vehicles(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'id': 1, 'name': 'Vehicle 1'}, {'id': 2, 'name': 'Vehicle 2'}]}
        mock_get.return_value = mock_response
        
        result = get_all_vehicles()

        # Vérification du résultat
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Vehicle 1')

    @patch('requests.post')
    def test_add_vehicle(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response
        
        with patch('streamlit.success') as mock_success:
            add_vehicle('Test Vehicle')
            # Vérifier si st.success a été appelé
            mock_success.assert_called_once_with("Vehicle successfully added!")

    @patch('requests.get')
    def test_get_all_races(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'id': 1, 'vehicle_id': 1, 'name': 'Race 1'}]}
        mock_get.return_value = mock_response
        
        # Appel de la fonction
        result = get_all_races()

        # Vérification du résultat
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Race 1')

    @patch('requests.post')
    def test_add_race(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response
        
        with patch('streamlit.success') as mock_success:
            add_race(1, 'Test Race')
            # Vérifier si st.success a été appelé
            mock_success.assert_called_once_with("Race successfully added!")

if __name__ == '__main__':
    unittest.main()
