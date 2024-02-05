import mysql.connector

# Ganti nilai-nilai ini sesuai dengan informasi database Anda
host = "iix1533.idcloudhost.com"
user = "nwwbgeal_ilyas"
password = "RmbXN_BRe3HA5PN"
database_name = "nwwbgeal_math-sip"

# Membuat koneksi ke database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )

    if connection.is_connected():
        print("Terhubung ke database")

        # Lakukan operasi database di sini

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Tutup koneksi setelah selesai
    if 'connection' in locals():
        connection.close()
        print("Koneksi ditutup")
