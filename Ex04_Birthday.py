months = (
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
)

birthday = input("Tgl Lahir (DD-MM-YYYY): ")

index = int(birthday[3:5]) - 1
bd_month = months[index]

print("Lahir Pada ", bd_month)
