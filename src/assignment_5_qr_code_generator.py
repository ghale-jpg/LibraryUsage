

import re
from pathlib import Path

import qrcode

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "qrcodes"


def read_non_empty(prompt: str) -> str:
   
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def safe_filename(text: str) -> str:
    
    cleaned = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return cleaned[:40] or "qrcode"


def normalize_url(url: str) -> str:
    
    if not re.match(r"^https?://", url, flags=re.IGNORECASE):
        return "https://" + url
    return url


def create_qr(data: str, filename: str) -> Path:
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"{filename}.png"
    qrcode.make(data).save(path)
    return path


def main() -> None:
    # Part 1: personal message or name.
    message = read_non_empty("Enter your name or a short message: ")
    message_path = create_qr(message, f"message_{safe_filename(message)}")
    print(f"QR code saved as {message_path}")

    # Part 2: favorite website.
    website = normalize_url(read_non_empty("Enter your favorite website: "))
    website_path = create_qr(website, f"website_{safe_filename(website)}")
    print(f"QR code saved as {website_path}")

    print("\nVerify: open each image and scan it with your phone camera.")
    print(f"  Expected 1: {message}")
    print(f"  Expected 2: {website}")


if __name__ == "__main__":
    main()
