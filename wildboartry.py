import arcade
import random

#
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "A Boar's Life"

BOAR_SPEED = 5
BOAR_SCALING = 1.8


BOAR_WALK_FOLDER = "/Users/beverlylee/Downloads/ezgif-split"


STATE_WELCOME = 0
STATE_PLAYING = 1
  

class BoarsLife(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.sprite_list = None  # Combined sprite list for all sprites
        self.boar = None
        self.baby_boars = arcade.SpriteList()
        self.boar_positions = []
        self.baby_data = []

        self.boar = None
        self.star = None

        self.game_state = STATE_WELCOME
        self.current_frame = 0
        self.frame_timer = 0
        self.current_direction = "down"
        self.boar_texture_index = 0

        self.boar_score = 0

        arcade.set_background_color(arcade.color.ANDROID_GREEN)

    def spawn_star(self):
        """Place star randomly on screen"""
        self.star.center_x = random.randint(50, SCREEN_WIDTH - 50)
        self.star.center_y = random.randint(50, SCREEN_HEIGHT - 50)


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
        
        # welcome
        self.welcome_sprite = arcade.Sprite(
    "/Users/beverlylee/Downloads/welcome to a boars life.png"
)
        self.welcome_sprite.center_x = SCREEN_WIDTH // 2
        self.welcome_sprite.center_y = SCREEN_HEIGHT // 2
        self.welcome_sprite.scale = 0.5

        # Put it in a sprite list
        self.welcome_list = arcade.SpriteList()
        self.welcome_list.append(self.welcome_sprite)

        # directions
        self.down_frames = list(range(0, 6))
        self.up_frames = list(range(6, 12))
        self.left_frames = list(range(12, 18))
        self.right_frames = list(range(18, 24))

        # boar sprite
        self.boar = arcade.Sprite()
        self.boar.textures = boar_frames
        self.boar.set_texture(0)

        self.boar.center_x = SCREEN_WIDTH // 2
        self.boar.center_y = 150
        self.boar.scale = BOAR_SCALING

        self.boar.change_x = 0
        self.boar.change_y = 0

        # Add boar to sprite list
        self.sprite_list.append(self.boar)

        # Create star sprite
        self.star = arcade.Sprite(":resources:/images/tiles/mushroomRed.png", scale=0.5)
        self.spawn_star()
        self.sprite_list.append(self.star)

        print(self.star.center_x, self.star.center_y)

    def on_draw(self):
        self.clear()

        if self.game_state == STATE_WELCOME:
            self.draw_welcome()
        elif self.game_state == STATE_PLAYING:
            self.draw_game()

    def draw_welcome(self):
        self.welcome_list.draw()


    def draw_game(self):
        # Draw all sprites from the single sprite list
        self.sprite_list.draw()
        
        self.baby_boars.draw()

        arcade.draw_text(f"Babies: {self.boar_score}",
            10, SCREEN_HEIGHT - 30,
            arcade.color.BLACK, 20)

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
        

# save path
        self.boar_positions.insert(0, (self.boar.center_x, self.boar.center_y))
        self.boar_positions = self.boar_positions[:len(self.baby_boars) * 25 + 1]

        # move babies + detect direction
        for i, baby in enumerate(self.baby_boars): # for loop for babies
            index = (i + 1) * 10 # picks a spot ten pixels away
            if index < len(self.boar_positions):
                old_x, old_y = baby.center_x, baby.center_y # save old position + set baby there
                baby.center_x, baby.center_y = self.boar_positions[index] # set baby's new position to that poin

                dx = baby.center_x - old_x # find change in x (so physics coded yay) and then see if its going + or -
                dy = baby.center_y - old_y # find change in y (so physics coded yay) and then see if its going + or -
                data = self.baby_data[i] # append to index of directions for animation and stuff

                if abs(dx) > abs(dy):
                    data["direction"] = "right" if dx > 0 else "left" # pick the direction
                else:
                    data["direction"] = "up" if dy > 0 else "down"

        # Animation for walking
        self.frame_timer += delta_time
        if self.frame_timer > 0.1:  # animation speed
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.boar.set_texture(frames[self.current_frame])

        for i, baby in enumerate(self.baby_boars):
            data = self.baby_data[i]

            if data["direction"] == "down":
                frames = self.down_frames
            elif data["direction"] == "up":
                frames = self.up_frames
            elif data["direction"] == "left":
                frames = self.left_frames
            else:
                frames = self.right_frames

            data["timer"] += delta_time
            if data["timer"] > 0.15:
                data["timer"] = 0
                data["frame"] = (data["frame"] + 1) % len(frames)

            baby.set_texture(frames[data["frame"]])


        # CHECK COLLISION WITH STAR (FOOD)
        if arcade.check_for_collision(self.boar, self.star):
            self.boar_score = self.boar_score + 1
            self.spawn_star()   # respawn food

            baby = arcade.Sprite()
            baby.textures = self.boar.textures
            baby.set_texture(self.boar_texture_index)
            baby.scale = BOAR_SCALING * 0.75
            baby.center_x = self.boar.center_x
            baby.center_y = self.boar.center_y

            self.baby_boars.append(baby)
            self.baby_data.append({"direction": "down", "frame": 0, "timer": 0})


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



def main():
    window = BoarsLife()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()