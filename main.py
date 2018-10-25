import encryptor as e
import decryptor as d





if __name__ == "__main__":
	mode = input("Please enter a mode. Enter 'e' for encryption and 'd' for decryption: ")
	if (mode.lower() == "e"):
		e.encrypt()
	elif (mode.lower() == "d"):
		print(d.decrypt())
	else:
		print("Invalid mode. Exiting.")   #Eventually make this so that it loops until valid input is entered


	input("\nPress Enter key to quit")
