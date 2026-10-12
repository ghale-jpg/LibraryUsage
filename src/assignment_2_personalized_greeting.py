
import emoji

# Maps keywords in the user's activity to an emoji shortcode.
ACTIVITY_EMOJIS = {
    "read": ":open_book:",
    "book": ":open_book:",
    "code": ":laptop:",
    "program": ":laptop:",
    "music": ":musical_note:",
    "sing": ":microphone:",
    "game": ":video_game:",
    "football": ":soccer_ball:",
    "soccer": ":soccer_ball:",
    "cricket": ":cricket_game:",
    "cook": ":cooking:",
    "travel": ":airplane:",
    "hike": ":hiking_boot:",
    "swim": ":person_swimming:",
    "draw": ":artist_palette:",
    "paint": ":artist_palette:",
    "dance": ":woman_dancing:",
}
DEFAULT_ACTIVITY_EMOJI = ":star:"


def say(text: str) -> None:
  
    # language="alias" accepts friendly names such as :smile: and :thumbs_up:.
    print(emoji.emojize(text, language="alias"))


def read_non_empty(prompt: str) -> str:
    
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def pick_activity_emoji(activity: str) -> str:
    
    lowered = activity.lower()
    for keyword, shortcode in ACTIVITY_EMOJIS.items():
        if keyword in lowered:
            return shortcode
    return DEFAULT_ACTIVITY_EMOJI


def main() -> None:
    name = read_non_empty("Enter your name: ").title()
    say(f"Hello {name}! :smile:")
    say("Keep learning Python! :thumbs_up:")

    activity = read_non_empty("What is your favorite activity? ")
    activity_emoji = pick_activity_emoji(activity)
    say(f"{name} loves {activity.lower()} {activity_emoji}")
    say("That sounds wonderful, enjoy it! :red_heart:")

if __name__ == "__main__":
    main()
