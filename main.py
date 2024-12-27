import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Mengimport data csv dari file
file_path = "StudentPerformanceFactors.csv"

# Membaca data CSV
data = pd.read_csv(file_path)

# Menampilkan informasi dataset
st.title('Analisis Dataset Performance Mahasiswa')

# Data deskripsi kolom
column_data = {
    "Kolom": [
        "gender", "age", "study_time", "absences", 
        "parental_education", "G1", "G2", "G3", 
        "internet", "health"
    ],
    "Deskripsi": [
        "Jenis kelamin siswa (misalnya, Male atau Female).",
        "Usia siswa dalam tahun.",
        "Waktu belajar siswa dalam jam per minggu.",
        "Jumlah ketidakhadiran siswa.",
        "Tingkat pendidikan orang tua siswa (misalnya, High School).",
        "Nilai siswa pada ujian pertama.",
        "Nilai siswa pada ujian kedua.",
        "Nilai akhir siswa (target variable).",
        "Akses siswa ke internet di rumah (Yes/No).",
        "Status kesehatan siswa (skala 1-5)."
    ]
}

# Membuat DataFrame deskripsi kolom
description_df = pd.DataFrame(column_data)

# Menampilkan DataFrame deskripsi kolom tanpa indeks angka
st.subheader("Deskripsi Kolom Dataset")
st.write(description_df.style.hide_index())  # Menyembunyikan kolom indeks

# Menampilkan 5 baris pertama dataset
st.subheader('5 Baris Pertama Dataset:')
st.write(data.head().style.hide_index())  # Menyembunyikan kolom indeks
# Menghitung persentase nilai yang missing
missing_percentage = (missing_values / len(data)) * 100

# Menggabungkan hasil ke sebuah dataframe yang terdiri dari 2 kolom yaitu Jumlah dan persentase nilai yang hilang
availability_check = pd.DataFrame({
    "Missing_Values": missing_values,
    "Missing_Percentage(%)": missing_percentage
}).sort_values(by="Missing_Values", ascending=False) # Mengurutkan nilai yang hilang dari yang terbanyak

# Menampilkan data frame
st.subheader('Nilai Missing dan Persentase:')
st.write(availability_check)

# Descriptive statistik untuk kolom-kolom numerik
numerical_stats = data.describe()
st.subheader('Descriptive Statistik untuk Kolom Numerik:')
st.write(numerical_stats)

# Memilih kolom-kolom dengan tipe data object
categorical_columns = data.select_dtypes(include='object').columns

# Menghitung jumlah kemunculan tiap kategori pada kolom
categorical_stats = {col: data[col].value_counts() for col in categorical_columns}

# Menampilkan distribusi frekuensi untuk kolom kategori
st.subheader('Distribusi Frekuensi untuk Kolom Kategori:')
for col in categorical_columns:
    st.write(f'Kolom: {col}')
    fig = plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x=col, palette='Set2')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Menghitung matriks korelasi antar kolom numerik
numeric_columns = data.select_dtypes(include=['number'])
numeric_columns = numeric_columns.dropna()  # Menghapus baris yang nilainya hilang
correlation_matrix = numeric_columns.corr()

# Menampilkan matriks korelasi
st.subheader('Matriks Korelasi:')
st.write(correlation_matrix)

# Menampilkan heatmap untuk matriks korelasi
st.subheader('Heatmap Matriks Korelasi:')
fig = plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', fmt=".2f")
plt.title('Correlation Heatmap')
st.pyplot(fig)
