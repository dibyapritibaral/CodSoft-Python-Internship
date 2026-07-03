# Simple Movie Recommendation System

movies = {
    "action": [
        "Avengers: Endgame",
        "Mission Impossible",
        "John Wick",
        "Mad Max: Fury Road"
    ],
    "comedy": [
        "Home Alone",
        "The Hangover",
        "3 Idiots",
        "Welcome"
    ],
    "romance": [
        "Titanic",
        "The Notebook",
        "Jab We Met",
        "Yeh Jawaani Hai Deewani"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Stree",
        "Bhool Bhulaiyaa"
    ],
    "science fiction": [
        "Interstellar",
        "Inception",
        "Avatar",
        "The Matrix"
    ],
    "animation": [
        "Frozen",
        "Coco",
        "Toy Story",
        "Kung Fu Panda"
    ]
}

print("🎬 Welcome to Movie Recommendation System!")
print("Available genres: Action, Comedy, Romance, Horror, Science Fiction, Animation")
print("Type 'exit' to close the program.\n")

while True:
    choice = input("Enter your favourite genre: ").lower().strip()

    if choice == "exit":
        print("Thank you for using the Movie Recommendation System!")
        break

    elif choice in movies:
        print("\n🎥 Recommended movies for you:")
        for movie in movies[choice]:
            print("-", movie)
        print()

    else:
        print("Sorry, this genre is not available.")
        print("Please choose from: Action, Comedy, Romance, Horror, Science Fiction, Animation\n")/0-'/'''''['[]]'''