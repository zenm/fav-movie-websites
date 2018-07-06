import fresh_tomatoes
import media


matrix = media.Movie(
    "The Matrix",
    "Guy learnes he's in a metaphysical world. \
    He busts out, but at what cost?",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

equilibrium = media.Movie(
    "Equilibrium",
    "In a future where feeling is outlawed, \
    a police officer/judge begins to feel.",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Equilibriumposter.jpg",
    "https://www.youtube.com/watch?v=raleKODYeg0")

jiro_sushi = media.Movie(
    "Jiro Dreams of Sushi",
    "Jiro, a master sushi maker lifts the \
    kimono on his expertise and shows just how disappointed \
    he is in his sons.",
    "https://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg",
    "https://www.youtube.com/watch?v=buF540VBwAE")

enter_the_dragon = media.Movie(
    "Enter the Dragon",
    "A fight club on an island with a \
    bad dude with a claw. Hiiiyaaaaa",
    "https://upload.wikimedia.org/wikipedia/en/e/ef/Enter_the_dragon.jpg",
    "https://www.youtube.com/watch?v=81jCPIag4KA")

gladiator = media.Movie(
    "Gladiator",
    "The Emporer is murdered and is blamed on \
    their star general. He becomes a slave is \
    forced to fight the Gladiator circuit to \
    help uncover the truth.",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=IvTT29cavKo")

gattaca = media.Movie(
    "Gattaca",
    "In a dystopian future, Vincent fakes \
    his way in working at a space station. \
    He's cleared to travel to Titan, but a \
    murder risks uncovering his ruse and \
    derailing the project.",
    "https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",
    "https://www.youtube.com/watch?v=hWjlUj7Czlk")

moana = media.Movie(
    "Moana",
    "Moana wants a better life, a Demigod \
    wants his magic wand, the villagers \
    want a better life. Who gets what they want?",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=LKFuXETZUsI")

braveheart = media.Movie(
    "Braveheart",
    "William Wallace rallies the Scottish to kick some ass.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=1cnoM8EiGGU")

field_of_dreams = media.Movie(
    "Field of Dreams",
    "A farmer hears voices of building a field. \
    He does, and 'they' come.",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Field_of_Dreams_poster.jpg",
    "https://www.youtube.com/watch?v=Ut06d4dptWo")

bugs_life = media.Movie(
    "A Bugs Life",
    "Grasshopper bullies want the Ants Food. \
    Who's going to stand up to them?",
    "https://upload.wikimedia.org/wikipedia/en/c/cc/A_Bug%27s_Life.jpg",
    "https://www.youtube.com/watch?v=Ljk2YJ53_WI")

terminator2 = media.Movie(
    "Terminator 2",
    "A robot comes back in time to save the world \
    to prevent Judgement Day.",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
    "https://www.youtube.com/watch?v=-W8CegO_Ixw")


movies = [matrix, equilibrium, jiro_sushi, enter_the_dragon, gladiator,
          gattaca, moana, braveheart, field_of_dreams, bugs_life, terminator2]


fresh_tomatoes.open_movies_page(movies)
