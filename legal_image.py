from PIL import Image, ImageDraw, ImageFont


def create_legal_image(text, filename="legal_info.png"):
    # Schriftart wählen (Standard-Systemschrift oder Pfad zu einer .ttf)
    try:
        # Für Linux/Mac oft: /Library/Fonts/Arial.ttf oder /usr/share/fonts/...
        font = ImageFont.truetype("Arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # Größe des Bildes basierend auf dem Text berechnen
    # Wir erstellen ein temporäres Bild für die Berechnung
    temp_img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(temp_img)

    # Text in Zeilen teilen
    lines = text.split("\n")

    # Maximale Breite und Gesamthöhe berechnen
    max_width = 0
    total_height = 0
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        max_width = max(max_width, bbox[2] - bbox[0])
        total_height += (bbox[3] - bbox[1]) + 10  # 10px Zeilenabstand

    # Finales Bild erstellen (Transparent)
    img = Image.new("RGBA", (max_width + 40, total_height + 40), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Text zeichnen (Farbe: Hellgrau passend zu deinem Design)
    current_y = 20
    for line in lines:
        draw.text((20, current_y), line, fill=(200, 200, 200, 255), font=font)
        bbox = draw.textbbox((0, 0), line, font=font)
        current_y += (bbox[3] - bbox[1]) + 10

    img.save(filename)
    print(f"Bild wurde als {filename} gespeichert!")


# Hier deine Daten eintragen
impressum_text = """oac-labs
P. Bschl
Drfstr. 51
02999 Lhs

E-Mail: info [at] oac-labs.com"""

create_legal_image(impressum_text)
