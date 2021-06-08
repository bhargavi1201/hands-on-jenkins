from flask import Flask, render_template
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://tenor.com/view/dog-sweep-hair-shocked-scared-gif-15766698",
    "https://tenor.com/view/no-toilet-paper-wiping-cleaning-spring-hectic-gif-16593196",
    "https://tenor.com/view/poop-toilet-paper-shortage-wipe-gif-16838273",
    "https://tenor.com/view/poop-elmo-pooping-gif-5112871",
    "https://tenor.com/view/relax-chill-dog-cute-swing-gif-16656710",
    "https://tenor.com/view/corgi-dogs-gif-9077936",
    "https://tenor.com/view/dog-puppy-cute-playful-dog-tongue-out-gif-15159934",
    "https://tenor.com/view/dog-sweep-hair-shocked-scared-gif-15766698",
    "https://tenor.com/view/no-toilet-paper-wiping-cleaning-spring-hectic-gif-16593196",
    "https://tenor.com/view/poop-toilet-paper-shortage-wipe-gif-16838273",
    "https://tenor.com/view/poop-elmo-pooping-gif-5112871"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
