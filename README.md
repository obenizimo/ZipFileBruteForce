# ZipFileBruteForce
# ZIP Password Cracker

ZIP Password Cracker is a simple Python script designed to crack the password of a specified ZIP file. This script tries all password combinations between the specified lengths using a character set that includes uppercase letters, lowercase letters, numbers, and special characters.

## Use

1. Download and install Python 3.x.
2. Download the ZIP Password Cracker script.
3. Edit the script and set the `zip_folder` variable to the folder where the ZIP file you want to crack is located.
4. Edit the script and set the `zip_file_name` variable to the name of the ZIP file you want to crack.
5. If you want to change the password length, set the number "9" in the `for password_length in range(1, 9):` line to the maximum password length you want.
6. Open command prompt or terminal and navigate to the directory where the script is located.
7. Run the script by entering the command `python zip_password_cracker.py` (assuming the name of the script is "zip_password_cracker.py").

The script will try to open the encrypted ZIP file by trying all possible password combinations. When successful, the script prints the message "Password cracked" and the password found.

## Warning

This script is for educational and informational purposes only. Attempting to crack encrypted files without the permission of others is illegal and unethical. Use this script only when you have forgotten the password of your own files or within legal and ethical limits.
