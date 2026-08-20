from io import BytesIO
import unittest

from PIL import Image

from swagger_server.service.technical_report_pdf import TechnicalReportPdf


class TestTechnicalReportPdf(unittest.TestCase):
    def test_builds_pdf_with_record_data_and_images(self):
        image = BytesIO()
        Image.new("RGB", (640, 480), "#2F5FA7").save(image, "JPEG")
        requested_paths = []

        def load_image(path):
            requested_paths.append(path)
            return image.getvalue()

        record = {
            "id_record": 7,
            "resume": "Instalación y pruebas completadas.",
            "status": "Completo",
            "vehicle": "GME-511",
            "client_name": "Cliente de prueba",
            "location_name": "Sede norte",
            "task_code": "INSTALACIÓN",
            "created_at": "2026-08-20T10:00:00",
            "technical_staff": [{"name": "Técnico Uno"}],
            "materials": [{"material": "DASHCAM", "quantity": 2}],
            "images": ["/files/evidencia-1.jpg", "/files/evidencia-2.jpg"],
        }

        result = TechnicalReportPdf.build(record, image_loader=load_image)

        self.assertTrue(result.getvalue().startswith(b"%PDF"))
        self.assertGreater(len(result.getvalue()), 2000)
        self.assertEqual(requested_paths, record["images"])


if __name__ == "__main__":
    unittest.main()
