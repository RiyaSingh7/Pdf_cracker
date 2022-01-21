import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("WordList.txt")]
crackThisPDF = "locked_pdf.pdf"

for password in tqdm(passwords, "Bruteforcing "):
    try:
        with pikepdf.open(crackThisPDF, password=password) as pdf:
            print(" Password found  : ", password)
            break
    except pikepdf._qpdf.PasswordError as e:

        continue
exit(0)
