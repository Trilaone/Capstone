import pyinputplus as pyip

data_murid = []

# Function to add student data
def add_student():
    nama = pyip.inputStr("Masukkan Nama Murid:")
    murid = {"Nama": nama, "Nilai":{}}
    
    while True:
        subject = pyip.inputStr("Masukkan Mata Pelajaran(Ketik 'Selesai' Jika Sudah):").lower()
        if subject == 'selesai':
            break
        nilai = pyip.inputFloat(f"Masukkan Nilai {subject}:")
        murid["Nilai"][subject] = nilai
    
    data_murid.append(murid)
    print("Sukses Masukkan Data Murid")
# Test Run
# add_student() 

# Function to Calculate Average Score
def nilai_rata2(murid):
    scores = murid["Nilai"]
    if scores:
        total_score = sum(scores.values())
        average_score = total_score / len(scores)
        return round(average_score)
    else:
        return None
# Test Run
# student_index = 0
# selected_student = data_murid[student_index]
# average_score = nilai_rata2(selected_student)
# print(f"Average Score for {selected_student['Nama']}: {average_score}")

# Function to Display All Student Data
def tampilkan_murid():
    if not data_murid:
        print("Data Murid Tidak Ditemukan")
    else:
        for idx, murid in enumerate(data_murid, start=1):
            print(f"{idx}. Nama: {murid['Nama']}")
            if murid["Nilai"]:
                print("Nilai:")
                for subject, score in murid["Nilai"].items():
                    print(f"{subject}: {score}")
                average_score = nilai_rata2(murid)
                print(f"Nilai Rata2: {average_score:.2f}")
            else:
                print("Nilai Tidak Tersedia")
# Test Run
# tampilkan_murid()
                
# Function to Update student Score
def update_nilai():
    if not data_murid:
        print("Data Murid Tidak Ditemukan.")
        return
    
    tampilkan_murid()
    choice = int(input("Pilih Nomer Murid untuk Diupdate:")) - 1
    if 0 <= choice < len(data_murid):
        murid = data_murid[choice]
        while True:
            subject = input("Tambah/Update Mata Pelajaran dan Nilai(Ketik 'Selesai' Jika Sudah):")
            if subject.lower() == 'selesai':
                break
            nilai = float(input(f'Masukkan Nilai {subject}:'))
            murid["Nilai"][subject] = nilai
        print("Nilai Berhasil Diupdate!!")
    else:
        print("Pilihan Salah")
# Test Run
# update_nilai()

# Function to Delete Student Data
def hapus_data():
    if not data_murid:
        print("Data Murid Tidak Ditemukan.")
        return
    
    tampilkan_murid()
    choice = int(input("Pilih Murid Untuk Dihapus:")) - 1
    if 0 <= choice < len(data_murid):
        del data_murid[choice]
        print("Berhasil Menghapus Data Murid!!!")
    else:
        print("Pilihan Salah!!!")
# Test Run
# hapus_data()

# Main Function
def main():
    while True:
        print("\nSistem Penilaian Siswa")
        print("1. Update Siswa")
        print("2. Tampilkan Nama dan Nilai Siswa")
        print("3. Update Nilai dan Matpel Siswa")
        print("4. Hapus Data Siswa")
        print("5. Exit")
        choice = input("Enter Your Choice!!!")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            tampilkan_murid()
        elif choice == "3":
            update_nilai()
        elif choice == "4":
            hapus_data()
        elif choice == "5":
            break
        else:
            print("Invalid Choice, Please Try Again!!!")
main()        