import json
import os
from copy import deepcopy

import requests
from bs4 import BeautifulSoup


WIKI_URL = "https://en.wikipedia.org/wiki/ASEAN"
OUTPUT_FILE = "asean_urban_areas.json"


def fetch_urban_areas_table():
    resp = requests.get(WIKI_URL)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    # Buscar la sección "Urban areas"
    header = soup.find(id="Urban_areas")
    if header is None:
        raise RuntimeError("No se encontró la sección 'Urban areas' en la página.")
    # Buscar la tabla siguiente
    table = header.find_next("table", {"class": "wikitable"})
    if table is None:
        raise RuntimeError("No se encontró la tabla 'Urban areas' después del encabezado.")

    rows = table.find_all("tr")
    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

    data = []
    for row in rows[1:]:
        cols = row.find_all(["td", "th"])
        if len(cols) != len(headers):
            continue
        entry = {headers[i]: cols[i].get_text(strip=True) for i in range(len(headers))}
        data.append(entry)

    return data


def parse_and_build_dict(rows):
    result = {}
    for entry in rows:
        country = entry.get("Country", "")
        core_city = entry.get("Core city", "")
        population_s = entry.get("Population", "").replace(",", "")
        area_s = entry.get("Area (km²)", "").replace(",", "")
        try:
            population = float(population_s)
            area = float(area_s)
            density = population / area if area != 0 else None
        except ValueError:
            population = None
            area = None
            density = None

        city_data = {
            "core_city": core_city,
            "population": population,
            "area_km2": area,
            "density_per_km2": density,
        }
        result.setdefault(country, {"cities": []})["cities"].append(city_data)

    return result


def load_existing_data(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    print("Obteniendo datos desde Wikipedia...")
    rows = fetch_urban_areas_table()

    print("Construyendo diccionario de países y ciudades...")
    countries_dict = parse_and_build_dict(rows)

    print("Cargando datos existentes (si existen)...")
    old_data = load_existing_data(OUTPUT_FILE)

    if old_data != countries_dict:
        print("Se detectaron cambios. Guardando nuevo archivo...")
        save_data(OUTPUT_FILE, countries_dict)
    else:
        print("No hay cambios. El archivo no se reescribe.")

    print(json.dumps(countries_dict, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
