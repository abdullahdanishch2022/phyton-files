file= open("bucket_list.txt","w")
file.write("1. visit the Eiffel tower\n")
file.write("2. learn to play the guitar\n")
file.write("3. code my own game\n")
file.close()
print("bucket list saved to bucket_list.txt")


# read the full file
file= open("bucket_list.txt","r")
content=file.read()
print("\n my bucketlist")
print(content)
file.close()

# use readlines
file= open("bucket_list.txt","r")
lines=file.readlines()
print(f"you have {len(lines)} items on your bucketlist")
print(lines)
file.close()

# add iitems using append mode
file= open("bucket_list.txt","a")
file.write("4. travel to Japan\n")
file.write("5. run a 5k marathon\n")
file.close()
print("2 more items added in the file")

file= open("bucket_list.txt","r")
print(file.read())
file.close()