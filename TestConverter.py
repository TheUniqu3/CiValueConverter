import pytest
import requests
from TestAnswers import *


class TestConverter:

    @pytest.mark.parametrize('weight_opt', weight_options)
    def test_weight_api(self, weight_opt):
        value = 100
        resp = requests.get(f'http://localhost:5000/convert/{value}/weight/gram/{weight_opt}').json()
        assert (resp == answer_weight[weight_opt])

    @pytest.mark.parametrize('length_opt', length_options)
    def test_length_api(self, length_opt):
        value = 10
        resp = requests.get(f'http://localhost:5000/convert/{value}/length/meter/{length_opt}').json()
        assert (resp == answer_length[length_opt])

    @pytest.mark.parametrize('temp_opt', temp_options)
    def test_temp_api(self, temp_opt):
        value = 273
        resp = requests.get(f'http://localhost:5000/convert/{value}/temperature/kelvin/{temp_opt}').json()
        assert (resp == answer_temp[temp_opt])

    @pytest.mark.parametrize('speed_opt', speed_options)
    def test_speed_api(self, speed_opt):
        value = 25
        resp = requests.get(f'http://localhost:5000/convert/{value}/speed/meter_per_second/{speed_opt}').json()
        assert (resp == answer_speed[speed_opt])
