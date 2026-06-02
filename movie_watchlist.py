name = "Movie_Wishlist: "
options = """1. Add movie 
2. List all movies 
3. display single movie 
4. Mark movie as watched 
5. Close the application"""
watches = []
mid = 1
while True: 
    print(name)
    print(options)
    choice = int(input("Enter your choice ( 1 - 5 ): "))
    match choice: 
        case 1: 
            print("Adding a Movie: ")
            title = input("Enter Title: ")
            description = input("Enter description: ")
            genere = input("Enter genere: ")
            watch = {"id":mid,"title":title,"description":description,"genere":genere,"is_watched":False}
            mid = mid+1
            watches.append(watch)
        case 2:
            print("List all movies: ")
            for watch in watches:
                print(f"ID: {watch["id"]}")
                print(f"Title: {watch["title"]}")
                print()
        case 3:
            m_id = int(input("Enter the ID of Movie: "))
            target_movie = {}
            for watch in watches: 
                if watch["id"] == m_id: 
                    target_movie = watch 
                    break 
            if target_watch == {}: 
                print("Movie Not found")
            else:
                print("Movie Details: ")
                print(f"ID: {target_watch["id"]}")
                print(f"Title: {target_watch["title"]}")
                print(f"Description: {target_watch["description"]}")
                print(f"is_watched: {target_watch["is_watched"]}")
        case 4: 
            print("Mark movie as watched: ")
            m_id = int(input("Enter the ID of the Movie: "))
            target_watch = {}
            for watch in watches: 
                if watch["id"] == m_id: 
                    target_watch = watch
                    break 
            if target_watch == {}: 
                print("Movie Not found")
            else:
                watch["is_watched"]= True
        case 5:
            print("Closing the application....")
            break
        case _: 
            print("Invalid choice! Try again")
    print("-"*15)
    choice = input("Do you want to continue (y/n)?: ")
    if choice == "y":
        continue
    else:
        break 
                