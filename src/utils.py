import hashlib
import zlib
import os

def hash_object(data, type="blob"):
    
    
    header = f"{type} {len(data)}\x00".encode('utf-8')
    full_data = header + data

    
    sha1 = hashlib.sha1(full_data).hexdigest()

   
    compressed_content = zlib.compress(full_data)

    return sha1, compressed_content

def write_object(sha1, compressed_content):
    
    folder = os.path.join(".git", "objects", sha1[:2])
    filename = os.path.join(folder, sha1[2:])

   
    os.makedirs(folder, exist_ok=True)
    
   
    with open(filename, "wb") as f:
        f.write(compressed_content)