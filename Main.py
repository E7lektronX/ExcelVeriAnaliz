import pandas as pd
import os

# Excel dosyasını oku
file_path = "AFETZEDE.xlsx"
df = pd.read_excel(file_path)

output_all = r"C:\Users\furka\Desktop\E7X\Code\Python\Veri Analizi\All"
os.makedirs(output_all, exist_ok=True)

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

# Klasörleri oluştur
for path in output_paths.values():
    os.makedirs(path, exist_ok=True)

# İl ve ilçe bazında verileri ayır ve kaydet
for il in iller:
    il_df = df[df['GELDİĞİ İL'] == il]
    il_df.to_excel(os.path.join(output_paths[il], f"{il}.xlsx"), index=False)

    # İl bazında toplam sayım
    il_count = len(il_df)
    il_all = pd.DataFrame({"İL": [il], "SAYI": [il_count]})

    all_file = os.path.join(output_all, "Toplam.xlsx")
    if os.path.exists(all_file):
        all_df = pd.read_excel(all_file)
        all_df = pd.concat([all_df, il_all], ignore_index=True)
    else:
        all_df = il_all

    all_df.to_excel(all_file, index=False)

    # İlçe bazında veri sayımı
    rows = []
    rows.append([il, "TOPLAM", il_count])

    if il in ilceler:
        for ilce in ilceler[il]:
            ilce_df = il_df[il_df['GELDİĞİ İLÇE'] == ilce]
            ilce_count = len(ilce_df)
            rows.append([il, ilce, ilce_count])

            ilce_df.to_excel(os.path.join(output_paths[il], f"{ilce}.xlsx"), index=False)

    count_df = pd.DataFrame(rows, columns=["İL", "İLÇE", "SAYI"])

    # İlçeler bazında toplam sayımı ekleyerek dosyaları kaydet
    with pd.ExcelWriter(os.path.join(output_paths[il], f"{il}.xlsx"), engine='openpyxl', mode='a') as writer:
        count_df.to_excel(writer, sheet_name="İlçe Sayım", index=False)


print("Hatay Başarılı")
print("Kahramanmaraş Başarılı")
print("Malatya Başarılı")
print("GaziAntep Başarılı")
print("Osmaniye Başarılı")
print("Adıyaman Başarılı")
print("DiyarBakır Başarılı")
print("Adana Başarılı")
print("By Ramazan Furkan Büber")
print("Copyright (c) 2024 Ramazan Furkan Büber")

