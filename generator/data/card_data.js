var card_data = [
    {
        "count": 1,
        "color": "indigo",
        "title": "Cunning Action",
        "icon": "white-book",
        "icon_back": "cloak-dagger",
        "contents": [
            "subtitle | Rogue feature",
            "rule",
            "fill | 2",
            "text | You can take a <b>bonus action on each of your turns</b> in combat. This action can be used only to take the <b>Dash, Disengage, or Hide</b> action.",
            "fill | 2",
            "section | Fast hands (Thief 3rd)",
            "text | You can also use the bonus action to make a Dexterity (<b>Sleight of Hand</b>) check, use your thieves' tools to <b>disarm a trap</b> or <b>open a lock</b>, or take the <b>Use an Object</b> action."
        ],
        "tags": ["feature", "rogue", "lucy"]
    },
    {
        "count": 1,
        "color": "indigo",
        "title": "Thieve's Cant",
        "icon": "white-book",
        "icon_back": "cloak-dagger",
        "contents": [
            "subtitle | Rogue feature",
            "rule",
            "fill | 2",
			"text | You hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages.",
            "fill | 1",
			"text | It takes four times longer to convey such a Message than it does to speak the same idea plainly.",
			"text | In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.",
        ],
        "tags": ["feature", "rogue", "lucy"]
    },
    {
        "count": 2,
        "color": "dimgray",
        "title": "Dagger",
        "icon": "mixed-swords",
        "contents": [
            "subtitle | Simple melee weapon (2gp)",
            "rule",
            "property | Damage | 1d4 piercing",
            "property | Modifier | Strength or Dexterity",
            "property | Properties | Light, Finesse, Thrown (20/60)",
            "rule",
            "fill | 2",
            "description | Finesse | Use your choice of Strength or Dexterity modifier for attack and damage.",
            "description | Light | When you attack while dual wielding light weapons, you may use a bonus action to attack with your off hand.",
            "description | Thrown | You can throw the weapon to make a ranged attack with the given range.",
            "fill | 3"
        ],
        "tags": ["item", "weapon", "lucy"]
    },
    {
        "count": 1,
        "color": "dimgray",
        "title": "Rapier",
        "icon": "crossed-swords",
        "contents": [
            "subtitle | Simple melee weapon (25gp)",
            "rule",
            "property | Damage | 1d8 piercing",
            "property | Modifier | Strength or Dexterity",
            "property | Properties | Finesse",
            "rule",
            "fill | 2",
            "description | Finesse | Use your choice of Strength or Dexterity modifier for attack and damage.",
            "fill | 3"
        ],
        "tags": ["item", "weapon", "lucy"]
    },
    {
        "count": 1,
        "color": "dimgray",
        "title": "Shortbow",
        "icon": "high-shot",
        "contents": [
            "subtitle | Simple range weapon (25gp)",
            "rule",
            "property | Damage | 1d6 piercing",
            "property | Modifier | Dexterity",
            "property | Misc | Ammunition, 2 handed",
            "rule",
            "fill | 2",
        ],
        "tags": ["item", "weapon", "lucy"]
    },
	{
        "count": 1,
        "color": "dimgray",
        "title": "Thieves' Tools",
        "icon": "pincers",
        "contents": [
            "subtitle | Thieves kit (25 gp 1 lb)",
            "rule",
            "fill | 1",
			"text | This set of tools includes a <b>small file</b>, a set of <b>lock picks</b>, a <b>small mirror</b> mounted on a metal handle, a set of narrow-bladed <b>scissors</b>, and a <b>pair of pliers</b>.",
			"text | Proficiency with these tools lets you add your proficiency bonus to any ability checks you make to disarm traps or open locks.",
            "fill | 1",
        ],
        "tags": ["item", "kit", "lucy"]
    },
	{
        "count": 1,
        "color": "dimgray",
        "title": "Poisoner's Kit",
        "icon": "poison-bottle",
        "contents": [
            "subtitle | Poison kit (25 gp 2 lb)",
            "rule",
            "fill | 1",
			"text | A poisoner’s kit includes the vials, chemicals, and other equipment necessary for the <b>creation of poisons</b>.",
			"text | Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to <b>craft</b> or <b>use</b> poisons.",
            "fill | 1",
        ],
        "tags": ["item", "kit", "lucy"]
    },
	{
        "count": 1,
        "color": "dimgray",
        "title": "Disguise Kit",
        "icon": "poison-bottle",
        "contents": [
            "subtitle | Disguise kit (25 gp 3 lb)",
            "rule",
            "fill | 1",
			"text | This pouch of cosmetics, hair dye, and small props lets you create disguises that change your physical appearance.",
			"text | Proficiency with this kit lets you add your proficiency bonus to create a visual disguise.",
            "fill | 1",
        ],
        "tags": ["item", "kit", "lucy"]
    },
	{
        "count": 1,
        "color": "dimgray",
        "title": "Mess Kit",
        "icon": "cauldron",
        "contents": [
            "subtitle | Mess kit(1sp 1lb)",
            "rule",
			"text | This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl.",
            "fill | 1",
        ],
        "tags": ["item", "kit", "lucy"]
    },
	{
        "count": 1,
        "color": "dimgray",
        "title": "Waterskin",
        "icon": "magic-potion",
        "contents": [
            "subtitle | Waterskin (2sp 5lb(full))",
            "rule",
			"text | 4 pints of water (or maybe something stronger)",
            "fill | 1",
        ],
        "tags": ["item", "kit", "lucy"]
    },
	{
        "count": 1,
        "color": "green",
        "title": "Devil Weed",
        "icon": "wheat",
        "contents": [
            "subtitle | 5 doses of Devil Weed",
            "rule",
			"text | For each dose above 1 per hour",
			"property | charisma | +2 (not stackable)",
			"property | Wisdom and Intelligence | -2 ",
            "rule",
			"text | An addictive drug fairly popular.",
			"text | The weed is chewed, exhausted weed and saliva is spit out.",
			"text | One dose gives <b>minor hallucinations</b> and <b>euphoria</b>.",
			"section | Addiction",
			"text | The user experiences withdrawal after 48 hours and is sickened for 1d6 hours.", 
			"section | Doses",
			"boxes | 5 | 2.5"
        ],
        "tags": ["item", "lucy"]
    },
    {
        "count": 2,
        "color": "dimgray",
        "title": "Potion of Healing",
        "icon": "drink-me",
        "contents": [
            "subtitle | Potion (50gp)",
            "rule",
            "property | Use time | 1 action",
            "property | Hit points restored | 2d4+2",
            "rule",
            "fill | 2",
            "text | When you drink this potion, you regain 2d4+2 hitpoints.",
            "text | Drinking or administering a potion takes 1 action.",
            "fill | 3"
        ],
        "tags": ["item", "consumable"]
    },
]
