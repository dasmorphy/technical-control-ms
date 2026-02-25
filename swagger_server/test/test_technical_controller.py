# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.generic_response import GenericResponse  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.tehnical_data import TehnicalData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTechnicalController(BaseTestCase):
    """TechnicalController integration test stubs"""

    def test_post_technical(self):
        """Test case for post_technical

        Guarda el control tecnico en la base de datos.
        """
        data = dict(technical_data=TehnicalData(),
                    channel='channel_example',
                    external_transaction_id='external_transaction_id_example')
        response = self.client.open(
            '/post/technical-control',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
