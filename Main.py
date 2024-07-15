import pandas as pd
import os

# Excel dosyasını oku
file_path = "AFETZEDE.xlsx"
df = pd.read_excel(file_path)

# İl ve ilçe bilgileri
iller = ['HATAY', 'KAHRAMANMARAŞ', 'MALATYA', 'GAZİANTEP', 'OSMANİYE', 'ADIYAMAN', 'DİYARBAKIR', 'ADANA']
ilceler = {
    'KAHRAMANMARAŞ': ["ONİKİŞUBAT", "DULKADİROĞLU", "AFŞİN", "PAZARCIK", "ELBİSTAN", "MERKEZ", "TÜRKOĞLU", "GÖKSUN",
                      "ANDIRIN", "EKİNÖZÜ"],
    'ADANA': ["YÖRÜKHAN", "YÜREGİR", "ÇUKUROVA", "SEYHAN", "SARIÇAM", "CEYHAN", "YUMURTALIK", "POZANTI"],
    'ADIYAMAN': ["MERKEZ", "GÖLBAŞI", "KAHTA"],
    'DİYARBAKIR': ["BAĞLAR", "ERGANİ", "ÇERMİK"],
    'GAZİANTEP': ["ŞAHİNBEY", "ISLAHİYE", "ŞEHİTKAMİL", "MERKEZ", "NURDAĞI", "OĞUZELİ", "İHSANİYE"],
    'HATAY': ["ANTAKYA", "İSKENDERUN", "DEFNE", "KIRIKHAN", "OVAKENT", "ALTINÖZÜ", "SAMANDAĞ", "NARLICA", "ARSUZ",
              "DÖRTYOL", "HASSA", "REYHANLI", "BELEN"],
    'MALATYA': ["YEŞİLYURT", "AKÇADAĞ", "MERKEZ", "BATTALGAZİ", "DOĞANŞEHİR"],
    'OSMANİYE': ["BAHÇE", "KADİRLİ", "MERKEZ", "TOPRAKKALE"]
}

# Klasörler
output_paths = {
    'KAHRAMANMARAŞ': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\KahramanMaraş',
    'MALATYA': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Malatya',
    'ADANA': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Adana',
    'OSMANİYE': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Osmaniye',
    'HATAY': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Hatay',
    'GAZİANTEP': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\GaziAntep',
    'DİYARBAKIR': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Diyarbakır',
    'ADIYAMAN': r'C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\Adiyaman'
}

# Kaydedilicek Klasör Kontrol
for path in output_paths.values():
    os.makedirs(path, exist_ok=True)

# İl ve ilçe bazında verileri ayır ve kaydet
for il in iller:
    il_df = df[df['GELDİĞİ İL'] == il]
    il_df.to_excel(os.path.join(output_paths[il], f"{il}.xlsx"), index=False)

    if il in ilceler:
        for ilce in ilceler[il]:
            ilce_df = il_df[il_df['GELDİĞİ İLÇE'] == ilce]
            ilce_df.to_excel(os.path.join(output_paths[il], f"{ilce}.xlsx"), index=False)

print("Tüm işlemler başarılı!")
