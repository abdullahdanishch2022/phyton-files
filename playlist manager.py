class playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        self.songs=[]
        print("playlist" ,self.name)
        print("genre" ,self.genre)

    def add_song(self,song):
        self.songs.append(song)
        print(f"{song} added to {self.name}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print(f"{song} is not found in playlist")
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i,song in enumerate(self.songs,1):
                print(f"{i}.{song}")
        else:
            print("no songs yet add some")
    def __del__(self):
        print(f"playlist {self.name} has been deleted. goodbye") 


my_playlist1=playlist("calm music","classical")
while True:

    print("\n1. Add Song 2. Remove Song 3. View Playlist 4. Delete & Quit")

    choice = input("Enter your choice: ")       
    if choice=="1":
        song=input("enter song name")
        my_playlist1.add_song(song)
    elif choice=="2":
        song=input("enter song to remove")
        my_playlist1.remove_song(song)
    elif choice=="3":
        my_playlist1.display()
    elif choice=="4":
        del my_playlist1
        break
    else:
        print("invalid choice. enter 1,2,3,4")