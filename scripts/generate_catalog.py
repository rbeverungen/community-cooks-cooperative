from pathlib import Path
import yaml

cookbooks = []

catalog_path = Path("catalog/cookbooks")

for file in sorted(catalog_path.glob("*.yml")):
    with open(file, "r", encoding="utf-8") as f:
        cookbooks.append(yaml.safe_load(f))

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Cookbooks - Community Cooks Cooperative</title>

<style>

body {
    font-family: Arial, sans-serif;
    margin: 25px;
}

.catalog {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.book-card {
    width: 220px;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 12px;
    background-color: #ffffff;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

.book-card img {
    width: 150px;
    height: auto;
    display: block;
    margin: 0 auto 10px auto;
}

.title {
    font-weight: bold;
    margin-bottom: 8px;
}

.status {
    color: #555;
    font-size: 0.9em;
}

</style>

</head>
<body>

<h1>Cookbooks</h1>

<p>
<a href="collection.html">Back to Collection</a>
</p>

<div class="catalog">
"""

for book in cookbooks:

    title = book.get("title", "Unknown Title")
    isbn = book.get("isbn", "")
    status = book.get("status", "unknown")

    cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"

    html += f"""
    <div class="book-card">

        <img src="{cover_url}" alt="{title}">

        <div class="title">
            {title}
        </div>

        <div class="status">
            Status: {status}
        </div>

    </div>
    """

html += """
</div>

</body>
</html>
"""

with open("cookbooks.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {len(cookbooks)} cookbook entries.")