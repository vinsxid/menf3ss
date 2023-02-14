import os

api_id = int(os.environ.get("API_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")
# =========================================================== #

db_url = os.environ.get("DB_URL", "")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", ""))
channel_2 = int(os.environ.get("CHANNEL_2", ""))
channel_log = int(os.environ.get("CHANNEL_LOG", ""))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", ""))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "20"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", ")
pic_girl = os.environ.get("PIC_GIRL", "")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱 Yanto akan membantumu untuk mengirimkan pesan secara anonim ke channel . Silakan sampaikan pesanmu atau pap cute atau video konten positif kamu\n\nSebelum menggunakan silakan baca rules terlebih dahulu ya\n\nButuh bantuan? Hubungi yanto")
menu_msg = os.environ.get("MENU_MSG","""
#Boy / #Girl untuk Mencari Pasangan, Teman , Partner FWB
#Ask untuk Bertanya
#Story untuk Berbagi Cerita
#Spill untuk Spill Masalah
#Find untuk Mencari Pasangan, Teman, Partner FWB

Wajib username ya""")
gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#Boy / #Girl untuk Mencari Pasangan, Teman , Partner FWB
#Ask untuk Bertanya
#Story untuk Berbagi Cerita
#Spill untuk Spill Masalah
#Find untuk Mencari Pasangan, Teman, Partner FWB


Wajib username ya""")
