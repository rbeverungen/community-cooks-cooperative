
from pathlib import Path
import yaml

cookbooks = []

catalog_path = Path("catalog/cookbooks")

for file in sorted(catalog_path.glob("*.yml")):
    print(file)
    try:
        with open(file, "r", encoding="utf-8") as f:
             cookbooks.append(yaml.safe_load(f))
    except Exception as e:
        print(f"Error loading {file}: {e}") 
        raise

html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Cookbooks</title>
</head>
<body>

<h1>Cookbooks</h1>

<p>
<a href="collection.html">Back to Collection</a>
</p>

"""

for book in cookbooks:

    title = book.get("title", "Unknown Title")
    isbn = book.get("isbn", "")
    status = book.get("status", "unknown")

    cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"

    html += f"""
    <div style="margin-bottom:30px;">

        <img src="{cover_url}" width="150">

        <br><br>

        <strong>{title}</strong>

        <br>

        Status: {status}

    </div>
    """

html += """
</body>
</html>
"""

with open("cookbooks.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {len(cookbooks)} cookbook entries.")