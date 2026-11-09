from datetime import datetime
from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)


def salam_waktu(jam):
  # Menentukan salam berdasarkan rentang jam
  if 4 <= jam <= 10:
    return "Selamat pagi"
  elif 11 <= jam <= 14:
    return "Selamat siang"
  elif 15 <= jam <= 17:
    return "Selamat sore"
  else:
    return "Selamat malam"


@app.route("/", methods=["GET", "POST"])
def home():
  # Ambil tanggal, jam server saat ini, serta jam dalam format integer untuk salam
  now = datetime.now()
  current_time = now.strftime("%d-%m-%Y %H:%M:%S")
  jam_sekarang = now.hour

  # Panggil fungsi salam_waktu berdasarkan jam saat ini
  salam = salam_waktu(jam_sekarang)

  nama = None
  if request.method == "POST":
    nama = request.form.get("nama")

  # Kirim variabel salam, time, dan nama ke template
  return render_template(
      "index.html", salam=salam, time=current_time, nama=nama
  )


if __name__ == "__main__":
  app.run(debug=True)