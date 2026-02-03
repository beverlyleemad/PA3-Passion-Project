import arcade

#
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "A Boar's Life"

BOAR_SPEED = 5
BOAR_SCALING = 1.5


BOAR_WALK_FOLDER = "/Users/beverlylee/Downloads/ezgif-split"
BOAR_ATTACK_FOLDER = "/Users/beverlylee/Downloads/ezgif-split-3"
TIMER_FOLDER = "/Users/beverlylee/Downloads/0100"


STATE_WELCOME = 0
STATE_PLAYING = 1
  

class BoarsLife(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.sprite_list = None  # Combined sprite list for all sprites
        self.boar = None
        self.timer_sprite = None

        self.game_state = STATE_WELCOME

        # animation
        self.current_frame = 0
        self.frame_timer = 0
        self.current_direction = "down"

        self.attacking = False
        self.attack_frame = 0
        self.attack_timer = 0
        self.attack_direction = "down"

        self.timer_frames = []
        self.timer_index = 60   # start at 60 seconds
        self.timer_elapsed = 0

        arcade.set_background_color(arcade.color.ANDROID_GREEN)

    def setup(self):
        """Initialize the game"""
        self.sprite_list = arcade.SpriteList()  # Single sprite list for everything

        # manual frames
        boar_frames = [
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile000.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile001.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile002.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile003.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile004.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile005.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile006.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile007.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile008.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile009.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile010.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile011.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile012.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile013.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile014.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile015.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile016.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile017.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile018.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile019.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile020.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile021.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile022.png"),
            arcade.load_texture(f"{BOAR_WALK_FOLDER}/tile023.png"),
        ]

        boar_attack_frames = [
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile000.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile001.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile002.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile003.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile004.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile005.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile006.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile007.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile008.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile009.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile010.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile011.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile012.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile013.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile014.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile015.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile016.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile017.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile018.png"),
            arcade.load_texture(f"{BOAR_ATTACK_FOLDER}/tile019.png"),
        ]

        timer_frames = [
            arcade.load_texture(f"{TIMER_FOLDER}/1.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/2.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/3.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/4.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/5.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/6.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/7.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/8.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/9.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/10.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/11.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/12.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/13.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/14.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/15.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/16.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/17.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/18.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/19.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/20.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/21.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/22.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/23.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/24.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/25.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/26.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/27.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/28.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/29.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/30.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/31.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/32.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/33.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/34.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/35.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/36.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/37.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/38.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/39.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/40.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/41.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/42.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/43.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/44.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/45.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/46.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/47.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/48.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/49.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/50.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/51.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/52.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/53.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/54.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/55.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/56.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/57.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/58.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/59.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/60.png"),
            arcade.load_texture(f"{TIMER_FOLDER}/61.png")
        ]
        

        # directions
        self.down_frames = list(range(0, 6))
        self.up_frames = list(range(6, 12))
        self.left_frames = list(range(12, 18))
        self.right_frames = list(range(18, 24))

        # boar sprite
        self.boar = arcade.Sprite()
        self.boar.textures = boar_frames
        self.boar.set_texture(0)
        self.boar_attack_frames = boar_attack_frames

        self.boar.center_x = SCREEN_WIDTH // 2
        self.boar.center_y = 150
        self.boar.scale = BOAR_SCALING

        self.boar.change_x = 0
        self.boar.change_y = 0

        # Add boar to sprite list
        self.sprite_list.append(self.boar)

        # Create timer sprite
        self.timer_frames = timer_frames
        self.timer_sprite = arcade.Sprite()
        self.timer_sprite.textures = self.timer_frames
        self.timer_sprite.set_texture(self.timer_index - 1)
        self.timer_sprite.center_x = SCREEN_WIDTH - 100
        self.timer_sprite.center_y = SCREEN_HEIGHT - 550
        self.timer_sprite.scale = 0.05

        # Add timer to sprite list
        self.sprite_list.append(self.timer_sprite)


    def on_draw(self):
        self.clear()

        if self.game_state == STATE_WELCOME:
            self.draw_welcome()
        elif self.game_state == STATE_PLAYING:
            self.draw_game()

    def draw_welcome(self):
        arcade.draw_text(
            "Welcome to A Boar's Life!",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2 + 50,
            arcade.color.BLACK,
            font_size=36,
            anchor_x="center"
        )
        arcade.draw_text(
            "Press ENTER to start",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2 - 50,
            arcade.color.DARK_GREEN,
            font_size=24,
            anchor_x="center"
        )

    def draw_game(self):
        # Draw all sprites from the single sprite list
        self.sprite_list.draw()

    def on_key_press(self, key, modifiers):
        if self.game_state == STATE_WELCOME and key == arcade.key.ENTER:
            self.game_state = STATE_PLAYING
            return

        if key in [arcade.key.W, arcade.key.UP]:
            self.boar.change_y = BOAR_SPEED
        if key in [arcade.key.S, arcade.key.DOWN]:
            self.boar.change_y = -BOAR_SPEED
        if key in [arcade.key.A, arcade.key.LEFT]:
            self.boar.change_x = -BOAR_SPEED
        if key in [arcade.key.D, arcade.key.RIGHT]:
            self.boar.change_x = BOAR_SPEED
        if key == arcade.key.SPACE:
            self.start_attack()


    def on_key_release(self, key, modifiers):
        if key in [arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN]:
            self.boar.change_y = 0
        if key in [arcade.key.A, arcade.key.D, arcade.key.LEFT, arcade.key.RIGHT]:
            self.boar.change_x = 0

    def on_update(self, delta_time):
        if self.game_state != STATE_PLAYING:
            return

        # move boar
        self.boar.center_x += self.boar.change_x
        self.boar.center_y += self.boar.change_y

        # Keep boar on screen
        if self.boar.left < 0:
            self.boar.left = 0
        if self.boar.right > SCREEN_WIDTH:
            self.boar.right = SCREEN_WIDTH
        if self.boar.bottom < 0:
            self.boar.bottom = 0
        if self.boar.top > SCREEN_HEIGHT:
            self.boar.top = SCREEN_HEIGHT

        # TIMER COUNTDOWN
        self.timer_elapsed += delta_time

        if self.timer_elapsed >= 1.0 and self.timer_index > 0:
            self.timer_elapsed = 0
            self.timer_index -= 1
            self.timer_sprite.set_texture(self.timer_index - 1)

        # GAME OVER when timer hits 0
        if self.timer_index <= 0:
            print("TIME UP!")
            self.game_state = STATE_WELCOME
            return

        # Attack animation
        if self.attacking:
            self.attack_timer += delta_time
            if self.attack_timer > 0.07:  # attack speed
                self.attack_timer = 0
                self.attack_frame += 1

            # stop after 5
            if self.attack_frame >= 5:
                self.attacking = False
                return

            # direction
            if self.attack_direction == "down":
                base = 0
            elif self.attack_direction == "up":
                base = 5
            elif self.attack_direction == "left":
                base = 10
            else:  # right
                base = 15

            self.boar.texture = self.boar_attack_frames[base + self.attack_frame]
            return  # stop walk animation during attack

        # Determine direction and frames for walking
        frames = []
        if self.boar.change_y < 0:
            self.current_direction = "down"
            frames = self.down_frames
        elif self.boar.change_y > 0:
            self.current_direction = "up"
            frames = self.up_frames
        elif self.boar.change_x < 0:
            self.current_direction = "left"
            frames = self.left_frames
        elif self.boar.change_x > 0:
            self.current_direction = "right"
            frames = self.right_frames
        else:
            # Not moving → idle frame
            frames = self.get_direction_frame()
            self.current_frame = 0
            self.boar.set_texture(frames[self.current_frame])
            return

        # Animation for walking
        self.frame_timer += delta_time
        if self.frame_timer > 0.1:  # animation speed
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.boar.set_texture(frames[self.current_frame])

    def get_direction_frame(self):
        if self.current_direction == "down":
            return self.down_frames
        elif self.current_direction == "up":
            return self.up_frames
        elif self.current_direction == "left":
            return self.left_frames
        elif self.current_direction == "right":
            return self.right_frames
        return self.down_frames  # fallback
    
    def start_attack(self):
        if self.attacking:
            return  # prevent spam

        self.attacking = True
        self.attack_frame = 0
        self.attack_timer = 0
        self.attack_direction = self.current_direction



def main():
    window = BoarsLife()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()