import json
import pdfplumber

def convert_pdf_to_json(pdf_file_path, output_json_path):
    matches = []
    
    with pdfplumber.open(pdf_file_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            lines = text.split('\n')
            
            # PDF Şablonunuza göre satır ayrıştırma mantığı
            for line in lines:
                # Örnek ayrıştırma mantığı (Satır içi aka / ao taraması)
                if "VS" in line or "-" in line:
                    matches.append({
                        "tatami": 1, # İstenirse kategoriden tatami atanabilir
                        "category": "KUMITE ELEME",
                        "aka": "SPORCU AKA",
                        "akaClub": "KULÜP A",
                        "ao": "SPORCU AO",
                        "aoClub": "KULÜP B",
                        "status": "waiting"
                    })

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)
    
    print(f"Dönüştürme tamamlandı: {output_json_path}")

# Kullanım:
# convert_pdf_to_json("kura_listesi.pdf", "kura.json")