#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import argparse
import os
import pickle
import itertools
import jinja2
import json

log = logging.getLogger()

ubase = 'http://dnd5eapi.co/api/'
args = None

jsonTemplate = '''[
{%- for spell in spells %}
	{
	"count": 1,
	"color": "{{spell.color}}",
	"title": "{{spell.name}}",
	"icon": "white-book-{{spell.level}}",
	"icon_back": "ankh",
	"contents": [
		"subtitle | {{spell.school}} level {{spell.level}} {{spell.page}}",
		"rule",
		"property | Casting time | {{spell.casting}}",
		"property | Range | {{spell.range}}",
		"property | Components | {{spell.components}}",
		"property | Duration | {{spell.duration}} {{spell.concentration}} {{spell.ritual}}",
		"rule",
		{%- for desc in spell.descriptions %}
		"text | {{desc}}",
		{%- endfor %}
		{%if spell.higher%}"text | {{spell.higher}}",{%endif%}
	],
	"tags": {{spell.tags}},
	},
{%- endfor %}
]
'''

# the  js version for the card generator
sTemplate = 'var card_spells = \n' + jsonTemplate

moreSpells = [
{
	"name": "Fire Bolt",
	"desc": ["You hurl a mote of fire at a creature or object within range. Make a ranged spell Attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.",],
	"higher_level": ["This spell's damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)",],
	"page": "",
	"range": "120 feet",
	"components": [ "V", "S"],
	"ritual": "no",
	"duration": "Instantaneous",
	"concentration": "no",
	"casting_time": "1 action",
	"level": 0,
	"school": { "name": "Evocation" },
},
{
	"name": "Poison Spray",
	"desc": ["You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage."],
	"higher_level": ["This spell's damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12)."],
	"page": "",
	"range": "10 feet",
	"components": [ "V", "S"],
	"ritual": "no",
	"duration": "Instantaneous",
	"concentration": "no",
	"casting_time": "1 action",
	"level": 0,
	"school": { "name": "Conjuration" },
},
{
	"name": "Spare The Dying",
	"desc": ["You touch a living creature that has 0 hit points. The creature becomes stable. This spell has no effect on Undead or constructs."],
	"higher_level": [],
	"page": "",
	"range": "touch",
	"components": [ "V", "S"],
	"ritual": "no",
	"duration": "Instantaneous",
	"concentration": "no",
	"casting_time": "1 action",
	"level": 0,
	"school": { "name": "Necromancy" },
},

{
	"name": "Hellish Rebuke",
	"desc": ["You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one."],
	"higher_level": ["When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st"],
	"page": "",
	"range": "60 feet",
	"components": [ "V", "S"],
	"ritual": "no",
	"duration": "Instantaneous",
	"concentration": "no",
	"casting_time": "1 reaction, must see 60 feet",
	"level": 1,
	"school": { "name": "Evocation" },
},
{
	"name": "Witch Bolt",
	"desc": ["Make a ranged spell attack against that creature. On a hit, the target takes 1d12 lightning damage, and on each of your turns for the duration, you can use your action to deal 1d12 lightning damage to the target automatically. The spell ends if you use your action to do anything else. The spell also ends if the target is ever outside the spell’s range or if it has total cover from you."],
	"higher_level": ["using a spell slot of 2nd level or higher, the initial damage increases by 1d12 for each slot level above 1st."],
	"page": "",
	"range": "30 feet",
	"components": [ "V", "S", "M"],
	"ritual": "no",
	"duration": "1 minute",
	"concentration": "yes",
	"casting_time": "1 action",
	"level": 1,
	"school": { "name": "Evocation" },
},
{
	"name": "Phantasmal Force",
	"desc": ["see adventurer guide for lots of detail"],
	"higher_level": [],
	"page": "",
	"range": "60 feet",
	"components": [ "V", "S", "M"],
	"ritual": "no",
	"duration": "1 minute",
	"concentration": "yes",
	"casting_time": "1 action",
	"level": 2,
	"school": { "name": "Illusion" },
},

]

def dnd5Api(category):
	"""Fetch all category items from the dnd database"""
	items = requests.post(ubase+category+'/').json()
	log.info("Found %s %s" % (items['count'], category))
	for item in items['results']:
		log.info("fetching %s" % item['name'])
		yield requests.get(item['url']).json()

def getTags(spell):
	if spell.name.lower() in map(lambda s: s.lower(), [
			'Eldritch blast', 'Fire bolt', 'Mage hand', 'Poison spray', 'Spare the dying', #cantrips
			'Comprehend languages', 'Detect magic', 'Faerie fire', 'Hellish Rebuke', 'Sleep', 'Witch bolt', # level1
			'Calm emotions', 'Invisibility', 'Phantasmal Force', # level2
			]):
		return ["rad"]
	return []

class Spell(object):
	def __init__(self, js):
		self.js=js
	def __repr__(self): return '%s<%s>' % (self.__class__.__name__, self.name)
	@property
	def name(self): return self.js['name']
	@property
	def color(self): return 'black'
	@property
	def school(self): return self.js['school']['name']
	@property
	def components(self): return ','.join(filter(bool, self.js['components']))
	@property
	def duration(self): return self.js['duration']
	@property
	def higer(self): return self.js['higher_level']
	@property
	def descriptions(self): 
		# ugly workaround to avoid stripping '"" when the last character is actuall '\"'
		wa = lambda desc:  desc+' ' if desc and desc[-1] == '"' else desc
		return (json.dumps(wa(desc)).strip('"') for desc in self.js['desc'])
	@property
	def page(self): return self.js['page']
	@property
	def level(self): return self.js['level']
	@property
	def ritual(self): return '' if self.js['ritual'] == 'no' else 'ritual'
	@property
	def casting(self): return self.js['casting_time']
	@property
	def range(self): return self.js['range']
	@property
	def concentration(self): return '' if self.js['concentration'] == 'no' else 'concentration'
	@property
	def tags(self): return json.dumps(['spells']+ getTags(self))


def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--verbose', '-v', action='count')
	parser.add_argument('--max-spell', '-m', type=int)
	args = parser.parse_args()
	pfile = 'spells.pickle'

	if os.path.exists(pfile):
		log.warning('Found serialized spells, delete %s to refresh the tokens from %s' % (pfile, ubase))
		with open(pfile, 'r') as fpickle:
			spells = pickle.load(fpickle)
	else:
		# fetch token using dnd5api on the net or above spell description

		spells = itertools.chain((Spell(s) for s in moreSpells), (Spell(s) for s in dnd5Api('spells')))

	sSpells = [] # used for further serialization
	for spell in itertools.islice(spells, args.max_spell):
		log.info(spell)
		sSpells.append(spell)

	# generate the json file
	with open('card_spells.json', "w") as jsfile:
		jsfile.write(jinja2.Template(jsonTemplate).render(spells=sSpells).encode('utf-8'))

	# and the javascript
	with open('card_spells.js', "w") as jsfile:
		jsfile.write(jinja2.Template(sTemplate).render(spells=sSpells).encode('utf-8'))

	# serialize the data if not already done
	if not os.path.exists(pfile):
		with open(pfile, 'w') as fpickle:
			pickle.Pickler(fpickle).dump(sSpells)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	main()
