import os

JOKE = (
    "My kid asked what a dad joke is. I said it's a regular joke, except it "
    "comes with a mortgage, a lawn to mow, and a man who laughs at his own punchline."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()  # one joke, written and printed: fully deterministic
