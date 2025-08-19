from highrise import *
from highrise.models import *

class MyBot(BaseBot):

    heights = {"1": 0, "2": 7.5, "3": 14.5}

    # Lista oryginalnych nazw emotek i odpowiadających kodów
    free_emotes = {
        "Sit": "idle-loop-sitfloor",
        "Enthused": "idle-enthusiastic",
        "Yes": "emote-yes",
        "The Wave": "emote-wave",
        "Tired": "emote-tired",
        "Snowball Fight!": "emote-snowball",
        "Snow Angel": "emote-snowangel",
        "Shy": "emote-shy",
        "Sad": "emote-sad",
        "No": "emote-no",
        "Model": "emote-model",
        "Flirty Wave": "emote-lust",
        "Laugh": "emote-laughing",
        "Kiss": "emote-kiss",
        "Sweating": "emote-hot",
        "Hello": "emote-hello",
        "Greedy Emote": "emote-greedy",
        "Face Palm": "emote-exasperatedb",
        "Curtsy": "emote-curtsy",
        "Confusion": "emote-confused",
        "Charging": "emote-charging",
        "Bow": "emote-bow",
        "Thumbs Up": "emoji-thumbsup",
        "Tummy Ache": "emoji-gagging",
        "Flex": "emoji-flex",
        "Cursing Emote": "emoji-cursing",
        "Raise The Roof": "emoji-celebrate",
        "Angry": "emoji-angry",
        "Savage Dance": "dance-tiktok8",
        "Don't Start Now": "dance-tiktok2",
        "Let's Go Shopping": "dance-shoppingcart",
        "Russian Dance": "dance-russian",
        "Penny's Dance": "dance-pennywise",
        "Macarena": "dance-macarena",
        "K-Pop Dance": "dance-blackpink",
        "Hyped": "emote-hyped",
        "Jinglebell": "dance-jinglebell",
        "Nervous": "idle-nervous",
        "Toilet": "idle-toilet",
        "Astronaut": "emote-astronaut",
        "Dance Zombie": "dance-zombie",
        "Heart Eyes": "emote-hearteyes",
        "Swordfight": "emote-swordfight",
        "TimeJump": "emote-timejump",
        "Snake": "emote-snake",
        "Heart Fingers": "emote-heartfingers",
        "Float": "emote-float",
        "Telekinesis": "emote-telekinesis",
        "Penguin dance": "dance-pinguin",
        "Creepy puppet": "dance-creepypuppet",
        "Sleigh": "emote-sleigh",
        "Maniac": "emote-maniac",
        "Energy Ball": "emote-energyball",
        "Singing": "idle_singing",
        "Frog": "emote-frog",
        "Superpose": "emote-superpose",
        "Cute": "emote-cute",
        "TikTok Dance 9": "dance-tiktok9",
        "Weird Dance": "dance-weird",
        "TikTok Dance 10": "dance-tiktok10",
        "Pose 7": "emote-pose7",
        "Pose 8": "emote-pose8",
        "Casual Dance": "idle-dance-casual",
        "Pose 1": "emote-pose1",
        "Pose 3": "emote-pose3",
        "Pose 5": "emote-pose5",
        "Cutey": "emote-cutey",
        "Punk Guitar": "emote-punkguitar",
        "Fashionista": "emote-fashionista",
        "Gravity": "emote-gravity",
        "Ice Cream Dance": "dance-icecream",
        "Wrong Dance": "dance-wrong",
        "UwU": "idle-uwu",
        "TikTok Dance 4": "idle-dance-tiktok4",
        "Advanced Shy": "emote-shy2",
        "Anime Dance": "dance-anime",
        "Kawaii": "dance-kawai",
        "Scritchy": "idle-wild",
        "Ice Skating": "emote-iceskating",
        "SurpriseBig": "emote-pose6",
        "Celebration Step": "emote-celebrationstep",
        "Creepycute": "emote-creepycute",
        "Pose 10": "emote-pose10",
        "Boxer": "emote-boxer",
        "Head Blowup": "emote-headblowup",
        "Ditzy Pose": "emote-pose9",
        "Teleporting": "emote-teleporting",
        "Touch": "dance-touch",
        "Air Guitar": "idle-guitar",
        "This Is For You": "emote-gift",
        "Push it": "dance-employee",
    }

    async def on_start(self, session_metadata: SessionMetadata):
        print("Bot uruchomiony!")

    async def on_chat(self, user: User, message: str):
        msg = message.strip()

        if msg.lower().startswith("tp "):
            floor = msg.split(" ", 1)[1]
            if floor in self.heights:
                pos = Position(5, self.heights[floor], 2)
                await self.highrise.teleport(user.id, pos)
                await self.highrise.chat(f"{user.username} was teleported to floor {floor}")
            else:
                await self.highrise.chat("Floor doesn't exist")

        elif msg.lower().startswith("emote "):
            emote_name = msg[6:].strip()  
            match = None
            for name in self.free_emotes:
                if name.lower() == emote_name.lower():
                    match = name
                    break

            if match:
                emote_code = self.free_emotes[match]
                await self.highrise.send_emote(emote_code, user.id)
                await self.highrise.chat(f"{user.username} używa emotki {match}")
            else:
                await self.highrise.chat("This emote is disabled")

    async def on_user_join(self, user: User, position: Position | AnchorPosition):
        await self.highrise.chat(f"Welcome {user.username}!")
