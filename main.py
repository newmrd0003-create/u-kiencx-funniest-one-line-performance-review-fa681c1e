import os

ENTRY = "Rating: Meets expectations. Asked me to write his own review, forwarded it to HR, and asked me to make it pop. Growth area: originality."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
