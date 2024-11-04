class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # Atribut yang bersifat private
        self.__balance = balance

    # Getter untuk balance
    @property
    def balance(self):
        return self.__balance

    # Setter untuk balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Saldo tidak bisa diatur ke nilai negatif.")

    # Method untuk menambahkan uang ke saldo
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Berhasil menambahkan Rp{amount} ke akun {self.account_holder}.")
        else:
            print("Jumlah yang dimasukkan harus lebih dari 0.")

    # Method untuk menarik uang dari saldo
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Berhasil menarik Rp{amount} dari akun {self.account_holder}.")
        else:
            print("Penarikan gagal: jumlah tidak valid atau saldo tidak mencukupi.")

# Membuat objek dari kelas BankAccount
akun1 = BankAccount("Alice", 1000000)

# Menggunakan getter untuk mengakses saldo
print(f"Saldo awal: Rp{akun1.balance}")

# Menggunakan setter untuk memperbarui saldo
akun1.balance = 2000000
print(f"Saldo setelah diatur menggunakan setter: Rp{akun1.balance}")

# Melakukan operasi deposit dan penarikan
akun1.deposit(500000)
print(f"Saldo setelah deposit: Rp{akun1.balance}")
akun1.withdraw(300000)
print(f"Saldo setelah penarikan: Rp{akun1.balance}")

# Contoh setter dengan nilai negatif (akan menampilkan pesan kesalahan)
akun1.balance = -500000