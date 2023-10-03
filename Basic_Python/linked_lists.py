# Define a Node class to represent a song in the playlist

class Node:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next=None


# Define a Playlist class to manage the linked list of songs
class Playlist:
    def __init__(self):
        self.head=None 
    
    def add_song(self,title,artist):
        new_song=Node(title,artist)
        if not self.head:
            self.head=new_song
        else:
            current_song=self.head
            while current_song.next:
                current_song=current_song.next

            current_song.next=new_song

    def remove_song(self,title):
        if not self.head:
            return 
        if self.head.title==title:
            self.head=self.head.next
            return
        current_song=self.head

        while current_song.next:
            if current_song.next.title==title:
                current_song.next=current_song.next.next
                return

                current_song=current_song.next
    def display_playlist(self):
        current_song=self.head
        if not current_song:
            print("PlayList is empty")
            return
        while current_song:
            print(f"{current_song.title} by {current_song.artist}")
            current_song=current_song.next

# Create a playlist
my_playlist = Playlist()

# Add songs to the playlist
my_playlist.add_song("Song1", "Artist1")
my_playlist.add_song("Song2", "Artist2")
my_playlist.add_song("Song3", "Artist3")

# Display the playlist
print("Current Playlist:")
my_playlist.display_playlist()

# Remove a song from the playlist
my_playlist.remove_song("Song2")

# Display the updated playlist
print("\nUpdated Playlist:")
my_playlist.display_playlist()


        

            


        

        
