import turtle
import random

# Pencere oluştur
win = turtle.Screen()
win.title("Uzay Oyunu")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Skor
score = 0

# Skor tablosunu gösteren metin
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 270)
score_display.write("Skor: {}".format(score), align="left", font=("Courier", 24, "normal"))

# Uzay aracını oluştur
spaceship = turtle.Turtle()
spaceship.speed(0)
spaceship.shape("triangle")
spaceship.color("white")
spaceship.shapesize(stretch_wid=1, stretch_len=3)
spaceship.penup()
spaceship.goto(0, -250)

# Düşmanın başlangıç boyutu
enemy_size = 3.0

# Düşman yarat
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("circle")
enemy.color("red")
enemy.shapesize(stretch_wid=enemy_size, stretch_len=enemy_size)
enemy.penup()
enemy.goto(-290, 150)
enemy.dx = 0.175

# Düşman rengini ayarla
def set_enemy_color():
    colors = ["red", "blue", "yellow", "green"]
    enemy.color(random.choice(colors))

# Düşmanı vurduğunda yapılacak işlemler
def hit_enemy():
    global score, enemy_size
    score += 1
    score_display.clear()
    score_display.write("Skor: {}".format(score), align="left", font=("Courier", 24, "normal"))
    
    if score == 13:
        score = 0
        score_display.clear()
        score_display.write("Skor: {}".format(score), align="left", font=("Courier", 24, "normal"))
        enemy_size = 3.0  # Düşman boyutunu başlangıç değerine döndür
        reset_enemy()  # Düşmanı yeniden doğur

    else:
        reset_enemy()  # Düşmanı yeniden doğur
        set_enemy_color()  # Düşman rengini ayarla
        enemy_size *= 0.8  # Düşman boyutunu küçült

# Düşmanın yeniden doğduğu konum
def reset_enemy():
    enemy.goto(-290, 150)
    enemy.shapesize(stretch_wid=enemy_size, stretch_len=enemy_size)

# Uzay gemisinin hareket fonksiyonları
def go_left():
    x = spaceship.xcor()
    x -= 20
    if x < -290:
        x = -290
    spaceship.setx(x)

def go_right():
    x = spaceship.xcor()
    x += 20
    if x > 290:
        x = 290
    spaceship.setx(x)

# Uzay gemisinin ateş etme fonksiyonu
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = spaceship.xcor()
        y = spaceship.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Mermi oluştur
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("triangle")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.penup()
bullet.goto(0, -250)
bullet.hideturtle()
bullet_state = "ready"

# Mermi hareketi
def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += 3  # Mermi hızını yarıya indir
        bullet.sety(y)

        if y > 275:
            bullet.hideturtle()
            bullet_state = "ready"

# Tuş bağlantıları
win.listen()
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")
win.onkeypress(fire_bullet, "space")

# Ana oyun döngüsü
while True:
    win.update()

    # Düşmanın hareketi
    x = enemy.xcor()
    x += enemy.dx
    enemy.setx(x)

    if x > 290 or x < -290:
        enemy.dx *= -1
        y = enemy.ycor()
        y -= 20
        enemy.sety(y)

    # Mermi ve düşman çarpışması kontrolü
    if bullet_state == "fire" and bullet.distance(enemy) < 15:
        bullet.hideturtle()
        bullet_state = "ready"
        hit_enemy()  # Düşmanı vurduğunda işlemler

    move_bullet()  # Mermi hareketini kontrol et
