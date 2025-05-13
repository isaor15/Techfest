import flet as ft
import flet_audio as fta
import random
#How the game works:
#The user selects a decade category
#Clicks "Play Song" to hear 5 seconds of a random song
#Types their guess in the text box
#Clicks "Check Answer" to see if they're correct
#Can use "Next Song" for a new song or "Pause" to stop playing
    
def main(page: ft.Page):
    page.title = "Song Quiz"
    songs = {
        "1980s": [
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Billie Jean.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\bllie jean2.jpg",  # Added comma here
                "hint": "The King of Pop says 'the kid is not my son'"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Everybody Want To Rule The World.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\everybody wants to rule the world3.jpg",  # Added comma here
                "hint": "A song by Tears for Fears about power and ambition"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Every Breath You Take.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\ebyt2.jpg",  # Added comma here
                "hint": "The Police's most famous song, 'I'll be watching you...'"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Everywhere.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\everywhere2.jpg",  # Added comma here
                "hint": "Fleetwood Mac song about following someone everywhere"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Like A Prayer.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\like a prayer2.jpg",  # Added comma here
                "hint": "Madonna's controversial religious-themed hit, featured in Deadpool & Wolverine"
            }
        ],
        "2000s": [
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Sweater Weather.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\sweater weather2.jpg",  # Added comma here
                "hint": "The Neighbourhood's song about cold weather attire"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Last Friday Night.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\last friday night2.jpg",  # Added comma here
                "hint": "Katy Perry's party anthem"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Get Lucky.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\get lcuky2.jpg",  # Added comma here
                "hint": "Daft Punk, Pharrell Williams, and song about good fortune"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Gangnam Style.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\gangnam style2.jpg",  # Added comma here
                "hint": "PSY's viral Korean hit, we all know the dance"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Danza Kuduro.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\danza kuduro2.jpg",  # Added comma here
                "hint": "Don Omar's Latin dance hit, moms love it!"
            }
        ],
        "2020s": [
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Blinding Lights.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\blinding lights2.jpg",  # Added comma here
                "hint": "The Weeknd's being blinded by something..."
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Brooklyn.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\BROOKLYN3.jpg",  # Added comma here
                "hint": "A Dominican indie groove that mentions NYC's coolest borough"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Golden Hour.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\Golden Hour3.jpg",  # Added comma here
                "hint": "JVKE's viral song about a perfect moment in time, imagine a sunset"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Let The Light In.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\let the light in3.jpg",  # Added comma here
                "hint": "One of Lana Del Rey's best songs ever (not biased)"
            },
            {
                "src": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\Levitating.mp3",
                "image": r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Images\levitating3.jpg",  # Added comma here
                "hint": "Dua Lipa with DaBaby"
            }
        ]
    }

    current_category = {"name": None, "song": None, "hint": None}

    audio_player = fta.Audio(
        src=r"C:\Users\frank\OneDrive\Desktop\SD Final Project\Desktop\Music\getlucky.mp3",
        autoplay=False,
        volume=1
    )
    page.overlay.append(audio_player)

    current_img = ft.Image(
        src="",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        visible=False
    )

    hint_txt = ft.Text(size=20)

    def close_hint(e):
        hint_sht.open = False
        page.update()

    def show_hint(e):
        if current_category.get("hint"):
            hint_sht.open = True
            hint_txt.value = current_category["hint"]
            page.update()

    def seek_rand(e):
        if current_category["song"]: 
            audio_player.pause()
            audio_player.seek(0)
            audio_player.resume()

            def stop_audio():
                audio_player.pause()
                audio_player.seek(0)
                page.update()

            page.after(5000, stop_audio)

    def rand_song(e):
        if current_category["name"]:
            song_dict = random.choice(songs[current_category["name"]])
            current_category["song"] = song_dict["src"]
            current_category["hint"] = song_dict["hint"]
            audio_player.src = current_category["song"]
            current_img.src = song_dict["image"]
            current_img.visible = True
            audio_player.play()
            page.update()

    def select_category(e):
        current_category["name"] = e.control.text
        rand_song(None)

    def pause(e):
        audio_player.pause()
        page.update()

    page.add(ft.Text("Welcome to the Song Quiz! To play, you must have great musical knowledge! Start by clicking on your preffered category, then click 'Play Song'. After clicking, listen to the song. Once you have the answer, type it in the text box and click 'Check Answer'. Now, you can guess the song playing and enjoy!", size = 17))

    category_buttons = [ft.ElevatedButton(text=category, on_click=select_category) for category in songs.keys()]

    for button in category_buttons:
        page.add(button)

    user_guess = ft.TextField(label="Write your guess here")
    result_text = ft.Text("")
    hint_sht = ft.BottomSheet(
    content=ft.Container(
        content=ft.Column(controls=[ft.Text("Hint:", size=20, weight="bold"),hint_txt,ft.ElevatedButton("Close", on_click=close_hint)]),padding=20))

    def check_guess(e):
        if current_category["name"] and user_guess.value.lower() in current_category["song"].lower():
            result_text.value = "Correct, nice work!"
        else:
            result_text.value = "Wrong answer, try again!"
        page.update()

    pause_Btn = ft.ElevatedButton(text="Pause", on_click=pause)
    check_Btn = ft.ElevatedButton("Check Answer", on_click=check_guess)
    next_Btn = ft.ElevatedButton("Next Song", on_click=rand_song)
    play_Btn = ft.ElevatedButton("Play Song", on_click=seek_rand)
    hint_btn = ft.ElevatedButton("Show Hint", on_click=show_hint)

    page.add(
        user_guess,current_img,check_Btn,pause_Btn,next_Btn,play_Btn,hint_btn,hint_sht,result_text)

ft.app(target=main)