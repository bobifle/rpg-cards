#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import argparse
import os
import pickle
import itertools
import jinja2

log = logging.getLogger()

ubase = 'http://dnd5eapi.co/api/'
args = None

sTemplate = '''var card_spells = [
{% for spell in spells -%}
	{
	"count": 1,
	"color": "orange",
	"title": "{{spell.name}}",
	"icon": "white-book-0",
	"icon_back": "ankh",
	"contents": [
		"subtitle | {{spell.school}} level {{spell.level}} {{spell.page}}",
		"rule",
		"property | Casting time | {{spell.casting}}",
		"property | Range | {{spell.range}}",
		"property | Components | {{spell.components}}",
		"property | Duration | {{spell.duration}} {{spell.concentration}} {{spell.ritual}}",
		"rule",
		{% for desc in spell.descriptions -%}}
		"text | {{desc}}",
		{%- endfor %}
		"text | {{spell.higher}}",
	],
	"tags": {{spell.tags}}
	},
{%- endfor %}
]
'''

def dnd5Api(category):
	"""Fetch all category items from the dnd database"""
	items = requests.post(ubase+category+'/').json()
	log.info("Found %s %s" % (items['count'], category))
	for item in items['results']:
		log.info("fetching %s" % item['name'])
		yield requests.get(item['url']).json()

class Spell(object):
	def __init__(self, js):
		self.js=js
	@property
	def name(self): return self.js['name']
	@property
	def school(self): return self.js['school']['name']
	@property
	def components(self): return ','.join(self.js['components'])
	@property
	def duration(self): return self.js['duration']
	@property
	def higer(self): return self.js['higher_level']
	@property
	def desc(self): return self.js['desc']
	@property
	def phb(self): return self.js['page']
	@property
	def level(self): return self.js['level']
	@property
	def ritual(self): return self.js['ritual']
	@property
	def casting(self): return self.js['casting_time']


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
		# fetch token using dnd5api on the net
		spells = (Spell(s) for s in dnd5Api('spells'))

	sSpells = [] # used for further serialization
	for spell in itertools.islice(spells, args.max_spell):
		log.info(spell)
		sSpells.append(spell)
	
	with open('card_spells.js', "w") as jsfile:
		jsfile.write(jinja2.Template(sTemplate).render(spells=spells))
	
	# serialize the data if not already done
	if not os.path.exists(pfile):
		with open(pfile, 'w') as fpickle:
			pickle.Pickler(fpickle).dump(sSpells)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	main()
