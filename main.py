# main.py

import pandas as pd

def process_data(input_csv_path, output_json_path):
    """
    CSV verisini okur, işler ve arayüzün kullanması için bir JSON dosyasına kaydeder.
    """
    try:
        # Adım 1: Veriyi Pandas DataFrame'e okuma
        df = pd.read_csv(input_csv_path)

        # Adım 2: Veriyi doğrudan JSON formatına çeviriyoruz (her satır bir kayıt)
        # Frontend'in (JavaScript) kolayca kullanabilmesi için 'records' formatını kullanıyoruz.
        df.to_json(output_json_path, orient='records', indent=4)
        
        print(f"Başarılı: '{input_csv_path}' işlendi ve '{output_json_path}' olarak kaydedildi.")

    except FileNotFoundError:
        print(f"Hata: '{input_csv_path}' dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Bu script doğrudan çalıştırıldığında aşağıdaki kod bloğu çalışır.
if __name__ == "__main__":
    CSV_FILE = 'education_tracking_dataset_clean_en.csv'
    JSON_OUTPUT_FILE = 'data.json'  # JavaScript bu dosyayı okuyacak
    process_data(CSV_FILE, JSON_OUTPUT_FILE)