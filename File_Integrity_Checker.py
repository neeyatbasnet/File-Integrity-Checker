import hashlib

def generate_hash(filepath):
    sha256=hashlib.sha256()

    try:
        with open(filepath,"rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None
    
def save_hash(hash_value,hash_file="stored_hash.txt"):
    with open(hash_file,'w') as f:
        f.write(hash_value)

def verify_hash(filepath,hash_file="stored_hash.txt"):
    new_hash=generate_hash(filepath)
    try:
        with open(hash_file,'r') as f:
            stored_hash=f.read()

        if new_hash==stored_hash:
            print("Integrity checked. File is not compromised")
        else:
            print("Hash mismatch . File Compromised")
    except FileNotFoundError:
        print("Stored hash not found")

def main():
    print("___FILE INTEGRITY___")
    choice=input("Enter your choice\n1.Generate and store hash for a file\n2.Verify file integrity")
    fp=input("Enter File path")
    if choice=="1":
        hash_value=generate_hash(fp)
        if hash_value:
            save_hash(hash_value)
            print("Hash Generated and stored successfully in the file")
    elif choice=="2":
        verify_hash(fp)
    else:
        print("Invalid Choice")

if __name__=="__main__":
    main()

        