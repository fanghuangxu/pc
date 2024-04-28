from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
 
app=Ursina()
 
grass_texture=load_texture("texture/grass.jpg")
dirt_texture=load_texture("texture/dirt.jpg")
sky_texture=load_texture("texture/sky.jpg")
cobblestone_texture=load_texture("texture/cobblestone.png")
plank_texture=load_texture("texture/plank.jpg")
stone_texture=load_texture("texture/stone.jpg")
bedrock_texture=load_texture("texture/bedrock.jpg")
brick_texture=load_texture("texture/brick.png")
endstone_texture=load_texture("texture/endstone.jpg")
lapis_texture=load_texture("texture/lapis.jpg")
leaf_texture=load_texture("texture/leaf.jpg")
lucky_block_texture=load_texture("texture/luckyblock.png")
tie_stone=load_texture(r"texture\tie_stone.png")
select_texture=grass_texture

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            scale=1500,
            texture=sky_texture,
            double_sided=True,
            position=(0,0,0)
        )
punch_sound   = Audio('sine',loop = False, autoplay = False)
block_pick = 1
block_texture_dict={1:grass_texture,2:stone_texture,3:brick_texture,4:dirt_texture,5:'white_cube'}
diction={}
class Hand(Entity):
    def __init__(self,texture=grass_texture,scale_x=0.5,scale_y=0.5):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = texture,
            scale_x = scale_x,
            scale_y = scale_y,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))
 
    def update(self):
        if block_pick==5:
            self.scale_x=0.2
            self.scale_y=0.2
        else:
            self.scale_x=self.scale_y=0.5
        self.texture=block_texture_dict[block_pick]
 
 
    def active(self):
        self.position = Vec2(0.2,-0.4)
 
    def passive(self):
        self.position = Vec2(0.4,-0.6)
global HAND
HAND=Hand(select_texture)
class Block(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            highlight_color=color.lime,
            color=color.white,
            texture=texture,
            origin_y=0.5
        )
 
    def input(self,key):
        if self.hovered:
            if key=="right mouse down":
                Block(position=self.position+mouse.normal,texture=select_texture)
            if key=="left mouse down":
                if self.texture!=bedrock_texture:
                    destroy(self)
 
    def update(self):
        global select_texture,HAND
        if held_keys["1"]: 
            select_texture=grass_texture
            HAND()
        if held_keys["2"]: 
            select_texture=dirt_texture
        if held_keys["3"]: 
            select_texture=cobblestone_texture
        if held_keys["4"]: 
            select_texture=plank_texture
        if held_keys["5"]: 
            select_texture=stone_texture
        if held_keys["6"]: 
            select_texture=brick_texture
        if held_keys["7"]: 
            select_texture=endstone_texture
        if held_keys["8"]: 
            select_texture=lapis_texture
        if held_keys["9"]: 
            select_texture=leaf_texture
        if held_keys["0"]: 
            select_texture=lucky_block_texture
        if held_keys["-"]: 
            select_texture=sky_texture
        if held_keys["q"]:
            select_texture=tie_stone
            print(player.y)
        if held_keys["escape"]:quit()
        if held_keys['left mouse'] or held_keys['right mouse']:
            HAND.active()
        else:
            HAND.passive()
height=1
a=0

for y in range(0,height):
    for z in range(-15,16):
        for x in range(-15,16):
            a+=1
            print(f"{a}/6727")
            texture=bedrock_texture
            Block(position=(x,y,z),texture=texture)
   
for y in range(1,5):
    for z in range(-15,16):
        for x in range(-15,16):
            a+=1
            print(f"{a}/6727")
            texture=bedrock_texture
            aaaaa=random.randrange(1,300)
            print(aaaaa)
            if aaaaa == 1:
                Block(position=(x,y,z),texture=tie_stone)

            else:
                Block(position=(x,y,z),texture=stone_texture)
            
for y in range(4,6):
    for z in range(-15,16):
        for x in range(-15,16):
            a+=1
            print(f"{a}/6727")
            texture=bedrock_texture
            Block(position=(x,y,z),texture=grass_texture)


player=FirstPersonController()

sky=Sky()
back_music    = Audio(r"gangqinqu.mp3",autoplay=False,loop=True)
back_music.play()
app.run()
