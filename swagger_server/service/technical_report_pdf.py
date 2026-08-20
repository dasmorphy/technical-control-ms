from __future__ import annotations

from datetime import datetime
from io import BytesIO
from typing import Callable, Iterable
from urllib.parse import urlsplit

import requests
from PIL import Image as PillowImage, ImageOps
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    BaseDocTemplate,
    Frame,
    PageTemplate,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


IMAGE_BASE_URL = "https://n8n.telearseg.net"
BLUE = colors.HexColor("#2F5FA7")
LIGHT_BLUE = colors.HexColor("#BDD4EA")
LIGHT_GRAY = colors.HexColor("#ECECEC")
DARK_GRAY = colors.HexColor("#505050")


class ImageDownloadError(RuntimeError):
    pass


class TechnicalReportPdf:
    """Builds the technical record PDF without relying on local brand assets."""

    @classmethod
    def build(
        cls,
        record: dict,
        image_loader: Callable[[str], bytes] | None = None,
    ) -> BytesIO:
        output = BytesIO()
        document = BaseDocTemplate(
            output,
            pagesize=A4,
            rightMargin=20 * mm,
            leftMargin=20 * mm,
            topMargin=32 * mm,
            bottomMargin=27 * mm,
            title=cls._title(record),
            author="technical-control-ms",
        )
        frame = Frame(
            document.leftMargin,
            document.bottomMargin,
            document.width,
            document.height,
            id="technical-report",
        )
        document.addPageTemplates([
            PageTemplate(id="technical-report", frames=[frame], onPage=cls._decorate_page, pagesize=A4)
        ])
        story = cls._build_story(record, image_loader or cls._download_image)
        document.build(story)
        output.seek(0)
        return output

    @classmethod
    def _build_story(cls, record: dict, image_loader: Callable[[str], bytes]):
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=BLUE,
            alignment=TA_CENTER,
            spaceAfter=12 * mm,
        )
        section_style = ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=BLUE,
            spaceBefore=7 * mm,
            spaceAfter=5 * mm,
        )
        body_style = ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=15,
            alignment=0,
        )
        table_style = ParagraphStyle(
            "TableText",
            parent=body_style,
            fontSize=9,
            leading=11,
        )

        story = [Paragraph(cls._title(record), title_style)]
        story.append(cls._metadata_table(record, table_style))
        story.extend(
            [
                Paragraph("1. Resumen del trabajo realizado", section_style),
                Paragraph(cls._safe(record.get("resume"), "Sin resumen registrado."), body_style),
                Paragraph("2. Equipos utilizados", section_style),
                cls._materials_table(record.get("materials") or [], table_style),
            ]
        )

        paths = [path for path in (record.get("images") or []) if path]
        if paths:
            story.extend([PageBreak(), Paragraph("3. Anexos, Registro Fotográfico del trabajo realizado", section_style)])
            story.extend(cls._image_tables(paths, image_loader, table_style))

        return story

    @classmethod
    def _metadata_table(cls, record: dict, style: ParagraphStyle) -> Table:
        staff = ", ".join(
            cls._safe(person.get("name"))
            for person in (record.get("technical_staff") or [])
            if person and person.get("name")
        )
        rows = [
            ("Cliente:", record.get("client_name")),
            ("Ubicación del Proyecto:", record.get("location_name")),
            ("Fecha de Instalación:", cls._format_date(record.get("created_at"))),
            ("Técnico Responsable:", staff or None),
            ("Vehículo:", record.get("vehicle")),
            ("Estado:", record.get("status")),
            ("Código de tarea:", record.get("task_code")),
        ]
        data = [
            [Paragraph(f"<b>{label}</b>", style), Paragraph(cls._safe(value), style)]
            for label, value in rows
            if value not in (None, "")
        ]
        table = Table(data, colWidths=[65 * mm, 90 * mm], hAlign="CENTER")
        commands = [
            ("LINEABOVE", (0, 0), (-1, 0), 0.45, colors.HexColor("#9C9C9C")),
            ("LINEBELOW", (0, -1), (-1, -1), 0.45, colors.HexColor("#9C9C9C")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
        for row_index in range(len(data)):
            if row_index % 2:
                commands.append(("BACKGROUND", (0, row_index), (-1, row_index), LIGHT_GRAY))
        table.setStyle(TableStyle(commands))
        return table

    @classmethod
    def _materials_table(cls, materials: Iterable[dict], style: ParagraphStyle) -> Table:
        data = [[
            Paragraph("<b>ITEM</b>", style),
            Paragraph("<b>DESCRIPCIÓN</b>", style),
            Paragraph("<b>CANTIDAD</b>", style),
        ]]
        for index, material in enumerate(materials, start=1):
            data.append([
                Paragraph(f"<b>{index}</b>", style),
                Paragraph(cls._safe(material.get("material")), style),
                Paragraph(cls._safe(material.get("quantity"), "0"), style),
            ])
        if len(data) == 1:
            data.append([Paragraph("1", style), Paragraph("Sin equipos registrados", style), Paragraph("0", style)])

        table = Table(data, colWidths=[16 * mm, 118 * mm, 25 * mm], repeatRows=1, hAlign="CENTER")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), LIGHT_BLUE),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (-1, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 0.55, colors.black),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        return table

    @classmethod
    def _image_tables(cls, paths: list[str], loader: Callable[[str], bytes], style: ParagraphStyle):
        flowables = []
        cells = []
        for index, path in enumerate(paths, start=1):
            try:
                image_bytes = loader(path)
                report_image = cls._reportlab_image(image_bytes, max_width=76 * mm, max_height=105 * mm)
            except Exception as exc:
                raise ImageDownloadError(f"No se pudo cargar la imagen {index}: {path}") from exc
            cells.append([report_image, Paragraph(f"Imagen {index}", style)])

        for row_start in range(0, len(cells), 2):
            if row_start:
                flowables.append(PageBreak())
            row = cells[row_start:row_start + 2]
            while len(row) < 2:
                row.append([Spacer(1, 1), Paragraph("", style)])
            image_row = [cell[0] for cell in row]
            caption_row = [cell[1] for cell in row]
            table = Table([image_row, caption_row], colWidths=[80 * mm, 80 * mm], hAlign="CENTER")
            table.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, 0), 0.45, colors.HexColor("#8A8A8A")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, 0), 5),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
                ("TOPPADDING", (0, 1), (-1, 1), 3),
                ("BOTTOMPADDING", (0, 1), (-1, 1), 8),
            ]))
            flowables.extend([table, Spacer(1, 5 * mm)])
        return flowables

    @staticmethod
    def _reportlab_image(content: bytes, max_width: float, max_height: float) -> Image:
        with PillowImage.open(BytesIO(content)) as source:
            normalized = ImageOps.exif_transpose(source).convert("RGB")
            width, height = normalized.size
            normalized.thumbnail((1800, 1800), PillowImage.Resampling.LANCZOS)
            prepared = BytesIO()
            normalized.save(prepared, format="JPEG", quality=88, optimize=True)
        prepared.seek(0)
        scale = min(max_width / width, max_height / height, 1)
        return Image(prepared, width=width * scale, height=height * scale)

    @staticmethod
    def _download_image(path: str) -> bytes:
        parsed = urlsplit(str(path).strip())
        relative_path = parsed.path if parsed.scheme or parsed.netloc else str(path).strip()
        url = f"{IMAGE_BASE_URL.rstrip('/')}/{relative_path.lstrip('/')}"
        response = requests.get(url, timeout=(5, 20), allow_redirects=True)
        response.raise_for_status()
        if len(response.content) > 20 * 1024 * 1024:
            raise ImageDownloadError("La imagen supera el límite de 20 MB")
        return response.content

    @staticmethod
    def _decorate_page(canvas, document):
        width, height = A4
        canvas.saveState()

        canvas.setFillColor(BLUE)
        canvas.setStrokeColor(BLUE)
        path = canvas.beginPath()
        path.moveTo(0, height)
        path.lineTo(72 * mm, height)
        path.lineTo(60 * mm, height - 25 * mm)
        path.lineTo(0, height - 25 * mm)
        path.close()
        canvas.drawPath(path, fill=1, stroke=0)
        canvas.setStrokeColor(DARK_GRAY)
        canvas.setLineWidth(4)
        canvas.line(0, height - 28 * mm, 58 * mm, height - 28 * mm)

        canvas.setFillColor(DARK_GRAY)
        footer = canvas.beginPath()
        footer.moveTo(0, 18 * mm)
        footer.curveTo(55 * mm, 3 * mm, 115 * mm, 31 * mm, width, 20 * mm)
        footer.lineTo(width, 0)
        footer.lineTo(0, 0)
        footer.close()
        canvas.drawPath(footer, fill=1, stroke=0)
        canvas.setFillColor(BLUE)
        footer_blue = canvas.beginPath()
        footer_blue.moveTo(0, 14 * mm)
        footer_blue.curveTo(55 * mm, 0, 115 * mm, 25 * mm, width, 16 * mm)
        footer_blue.lineTo(width, 0)
        footer_blue.lineTo(0, 0)
        footer_blue.close()
        canvas.drawPath(footer_blue, fill=1, stroke=0)

        canvas.setFillColor(colors.white)
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(width - 12 * mm, 7 * mm, f"Página {document.page}")
        canvas.restoreState()

    @staticmethod
    def _format_date(value) -> str:
        if isinstance(value, datetime):
            return value.strftime("%d/%m/%Y")
        if value:
            text = str(value)
            try:
                return datetime.fromisoformat(text.replace("Z", "+00:00")).strftime("%d/%m/%Y")
            except ValueError:
                return text
        return "No registrada"

    @classmethod
    def _title(cls, record: dict) -> str:
        task = cls._safe(record.get("name_project"), "REGISTRO TÉCNICO")
        client = cls._safe(record.get("client_name"))
        vehicle = cls._safe(record.get("vehicle"))
        detail = " - ".join(part for part in (client, vehicle) if part != "No registrado")
        return f"INFORME TÉCNICO - {task}" + f" - {client}"

    @staticmethod
    def _safe(value, default="No registrado") -> str:
        if value is None or value == "":
            return default
        return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
