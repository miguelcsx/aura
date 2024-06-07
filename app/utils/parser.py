# aura/app/utils/parser.py

import cairosvg


def convert_html_to_svg(html: str, output_file: str) -> None:
    """
    Convert HTML to SVG
    """
    with open(html, "r", encoding="uft-8") as file:
        html_content = file.read()
    cairosvg.svg2svg(html_content, write_to=output_file)


def convert_html_to_png(html: str, output_file: str) -> None:
    """
    Convert HTML to PNG
    """
    with open(html, "r", encoding="utf-8") as file:
        html_content = file.read()
    cairosvg.svg2png(html_content, write_to=output_file)
