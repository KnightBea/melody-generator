import os
import music21 as m21

KERN_DATASET_PATH = "D:\Programming\AInML\melody-generator\deutschl\kinder"

#? Load the song
def load_songs_in_kern(dataset_path):
    #go through all the files in the dataset and load them with music21
    songs = []
    for path, subdir, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == "krn":
                song = m21.converter.parse(os.path.join(path, file))
                songs.append(song)
    return songs

def preprocess(dataset_path):
    pass

    #TODO load the folk songs
    print("Loading songs...")
    songs = load_songs_in_kern(dataset_path)
    print(f"Loaded {len(songs)} songs.")

    #TODO filter out songs that have non-acceptable durations

    #TODO transpose songs to Cmaj/Amin

    #TODO encode songs with music time series representation

    #TODO save songs to text file

if __name__ == "__main__":
    songs = load_songs_in_kern(KERN_DATASET_PATH)
    print(f"Loaded {len(songs)} songs.")
    # song = songs[0]
    # song.show()