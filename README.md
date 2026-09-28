# Warhammer 40,000 Kill Team Framework

    * Intended for use with a team building and information app.
    * Designed for multiple edition compatability.

------------------------------------------------------------------------------------------------------------------------

## Design Notes and Requirements

<details>
    <summary><b>Framework Design</b></summary>

```md

    + Unique IDs
      - All operatives, actions, rules, etc include a unique ID for accurate calls.
      - These IDs are designed to provide multi-edition compatability.
      - An index file <id_index.md> contains a list of all IDs.

```

</details>

<details>
    <summary><b>UI Requirements</b></summary>

```md

    + Operatives
        + <damage>
            - '/' UI label required between the two <damage> integers.
        + <hit>
            - '+' UI label required after the <hit> integer.
        + <move>
            - '"' UI label required after the <move> integer.
        + <save>
            - '+' UI label required after the <save> integer.
    
    + Operative Actions
        + <choices>
            - List is displayed beneath <text> string.
        + <cost>
            - 'AP' UI label required after the <cost> integer.
    
    + Operative Rules
        + <points>
            - List is displayed beneath <text> string.
    
    + Weapon Rules
        + <rule>
            - The following rules require a '+' UI label after the <rule> integer:
                - Lethal
            - The following rules require a '"' UI label after the <rule> integer:
                - Blast
                - Range
                - Torrent

```

</details>

------------------------------------------------------------------------------------------------------------------------

## Change Log

<details>
    <summary><b>v00.11</b></summary>

```md

    + Framework
        - Additional context comments added to existing frames.

    + Code Improvements
        + Existing Operatives
            - Raveners
                - File name, faction name, and all IDs have been updated.

        + Existing Operative Rules
            - Minor format updates.
                - (points:) Improper format used for several rules.
            - Expendable
            - Medic!
                - Renamed Medic! (Hearthkyn Salvager) to support Novitiates version.
            - Group Activation Operative Rule
                - Renamed Group Activation (Devotee) to support Gellerpox Infected versions.

        + Existing Weapon Rules
            - Minor format updates.
                - (name:)(id:) Removed inches (") references.

    + ID Index
        - Updated all ID tables for newly added data.
        - Format update to Faction files.
            - Faction file names  now match their faction ID.
        - Format update to Operative Actions.
            - All IDs renamed from act_ to op_act_ to fit ID format used by all rules.

    + Celestian Insidiants
        - Insidiant Superior
        - Insidiant Abjuror
        - Insidiant Censor
        - Insidiant Cremator
        - Insidiant Denuncia
        - Insidiant Mortisanctus
        - Insidiant Reliquarius
        - Insidiant Warrior

    + Deathwatch
        - Deathwatch Watch Sergeant
        - Deathwatch Aegis Veteran
        - Deathwatch Blademaster Veteran
        - Deathwatch Bombard Veteran
        - Deathwatch Breacher Veteran
        - Deathwatch Demolisher Veteran
        - Deathwatch Disruptor Veteran
        - Deathwatch Gunner Veteran
        - Deathwatch Headtaker Veteran
        - Deathwatch Horde-Slayer Veteran
        - Deathwatch Marksman Veteran

    + Gellerpox Infected
        - Vulgrar Thrice-Cursed
        - Bloatspawn
        - Fleshscreamer
        - Lumberghast
        - Mutant
        - Glitchling
        - Cursemite
        - Eyestinger Swarm
        - Sludge-grub

    + Hierotek Circle
        - Chronomancer
        - Psychomancer
        - Technomancer
        - Plasmacyte Accelerator
        - Plasmacyte Reanimator
        - Apprentek
        - Deathmark
        - Immortal Despotek
        - Immortal Guardian

    + Imperial Navy Breachers
        - Navis Sergeant-at-Arms
        - Navis Armsman
        - Navis Axejack
        - Navis C.A.T. Unit
        - Navis Endurant
        - Navis Gheistskull
        - Navis Grenadier
        - Navis Gunner
        - Navis Hatchcutter
        - Navis Surveyor
        - Navis Void-jammer

    + Murderwing
        - Murderwing Chaos Lord
        - Murderwing Champion
        - Murderwing Curseclaw
        - Murderwing Depredator
        - Murderwing Huntmaster
        - Murderwing Raptor
        - Murderwing Shrieker
        - Murderwing Skysear
        - Murderwing Warp Talon

    + Novitiates
        - Novitiate Superior
        - Novitiate Condemnor
        - Novitiate Dialogus
        - Novitiate Duellist
        - Novitiate Exactor
        - Novitiate Hospitaller
        - Novitiate Militant
        - Novitiate Penitent
        - Novitiate Preceptor
        - Novitiate Pronatus
        - Novitiate Purgatus
        - Novitiate Reliquarius

    + Wolf Scouts
        - Wolf Scout Pack Leader
        - Wolf Scout Fangbearer
        - Wolf Scout Frosteye
        - Wolf Scout Gunner
        - Wolf Scout Hunter
        - Wolf Scout Rune Priest Skjald
        - Wolf Scout Trapmaster
        - Wolf Scout Fenrisian Wolf

    + Operative Actions
        - Accelerate
        - Augment Weapon
        - Auto-Broadcaster
        - Boost
        - Breach Point
        - Call the Storm
        - Canoptek Repair
        - Carving Blow
        - Chirurgeon's Tools
        - Chronometron
        - Countertemporal Nanomine
        - Harbinger of Despair
        - Healing Balms
        - Hunter's Senses
        - Interference Pulse
        - Interstitial Command
        - Multi-Dimensional Vision
        - Nightmare Shroud
        - Nullifying Ritual
        - Raise Icon
        - Reanimate
        - Reinforce Metal
        - Shriek
        - Snatch
        - Speak of Her Deeds
        - Spiritual Mentor
        - Spot
        - Stirring Rhetoric
        - Strike From Above
        - Timesplitter
        - Vision of Madness
        - Wayfind
        - Weld Shut
        - Whip Into Frenzy

    + Operative Rules
        - Absolution Through Destruction
        - Accusing Exorcist
        - Adaptable Armoury
        - Adaptive Swordsmanship
        - Advanced Omni-Scrambler
        - Aggressive Force
        - Apprentek Assistance
        - Auspex Triangulation
        - Bladed Stance
        - Boons of Damnation
        - Breachwall
        - Brutal Assault
        - Cast the Runes
        - Caustic Demise
        - Chaos Champion
        - Clandestine Headtaker
        - Command Breach
        - Daemonic
        - Deathmarked
        - Detonate (Gheistskull)
        - Devotion
        - Disengage
        - Divine Acquisition
        - Emboldened
        - Fierce Temperament
        - Frenzied Attack
        - Gellercaust Masks
        - Glorious Hymnal
        - Grav-chute and Grapnel Launcher
        - Grizzled Veteran
        - Group Activation (Armsman)
        - Group Activation (Glitchling)
        - Group Activation (Mutant)
        - Group Activation (Mutoid Vermin)
        - Haywire Mine
        - Holy Defender
        - Holy Example
        - Horrifying Dismemberment
        - Horrifying Shrieking
        - Inspirational Example
        - Inspirational Pyre
        - Inspired Strikes
        - Instinctive Predator
        - Lupine Guile
        - Machine (C.A.T. Unit)
        - Machine (Gheistskull)
        - Medic! (Novitiate)
        - Militant Faith
        - Modified Vox-casters
        - Null Field
        - Null Rod
        - Path to Damnation
        - Path to Glory
        - Pinned Prey
        - Pounce
        - Proximity Mine
        - Purge With Flame
        - Relic Seeker
        - Scuttler (Accelerate)
        - Scuttler (Reanimate)
        - Simulacrum Nullificatus Icon Bearer
        - Slice the Veil
        - Small
        - Spiked Charger
        - Spiritual Chirurgy
        - Spread the Glorious Gifts
        - Steadfast
        - Storm Shield
        - Storm-veiled Execution
        - Strategic Command
        - Tempest's Fury
        - Tentacled Grasp
        - Thrill of Flight
        - Unflinching Example
        - Vigilant Marksman
        - Virge of Admonition Icon Bearer
        - Zealous Ultimatum

    + Weapon Rules
        - Anti-Psyker (Novitiate)
        - 1 Devastating 1
        - 2 Devastating 1
        - Engineered
        - Feast
        - Magnify
        - Phase Sweep
        - Riposte
        - Shield
        - Swipe
        - Zealous Rage

```

</details>

------------------------------------------------------------------------------------------------------------------------
<details>
    <summary><b>v00.10</b></summary>

```md

    + Frame Updates
        - Weapon rules now include bullet points.

    + ID Index
        - Updated all ID tables for newly added data.

    + Exodite Dragon Masters
        - Dragon Master Clanblade
        - Dragon Master Leystalker
        - Dragon Master Stonesinger
        - Drakolithe

    + Fellgor Ravager
        - Fellgor Ironhorn
        - Fellgor Deathknell
        - Fellgor Fluxbray
        - Fellgor Gnarlscar
        - Fellgor Gorehorn
        - Fellgor Herd-goad
        - Fellgor Mangler
        - Fellgor Shaman
        - Fellgor Toxhorn
        - Fellgor Vandal
        - Fellgor Warrior

    + Mandrakes
        - Mandrake Nightfiend
        - Mandrake Abyssal
        - Mandrake Chooser of the Flesh
        - Mandrake Dirgemaw
        - Mandrake Shadeweaver
        - Mandrake Warrior

    + Operative Actions
        - Apoplectic Rejuvenation
        - Cleaver Flurry
        - Gong Knell
        - Incite Fury
        - Mantle of Darkness
        - Pareidolic Projection
        - Song of Renewal
        - Sweeping Blow
        - Uncompromising Attack
        - Weave Darkness
        - Wreathe in Balefire

    + Operative Rules
        - Balefire
        - Beast (Drakolithe)
        - Berserker
        - Blade Whirl
        - Call the Attack
        - Champion
        - Clanblade Upgrades
        - Harrowing Whispers
        - Haunting Focus
        - Icon Bearer (Fellgor Ravager)
        - Implacable Darkscale
        - Leystalker Upgrades
        - Oubliex
        - Part Collector
        - Preternatural Evasion
        - Pox Bomb
        - Sagacious
        - Savage
        - Scaleshield
        - Shadow Portal
        - Shadow Warrior
        - Soul Harvest
        - Stonesinger Upgrades
        - Toxic Blessings
        - War Gong
        - Warrior Frenzy
        - Whip Control

    + Weapon Rules
        - Aimed
        - Headtaker
        - Soulstrike
        - Tactual Hunter
        - Vicious Blows

```

</details>

------------------------------------------------------------------------------------------------------------------------
<details>
    <summary><b>v00.09</b></summary>

```md

    + Frame Updates
        + Operative Actions
            - Frame reworked to cover types, full text, choices, and multiple rules.
        + Operative Rules
            - Frame reworked to cover types, full text, and multiple conditionals.

    + ID Index
        - Updated all ID tables for newly added data.

    + Battleclade
        - Battleclade Technoarcheologist
        - Battleclade Auto-proxy Servitor
        - Battleclade Breacher Servitor
        - Battleclade Combat Servitor
        - Battleclade Gun Servitor
        - Battleclade Servitor Underseer
        - Battleclade Technomedic Servitor

    + Goremonger
        - Goremonger Blood Herald
        - Goremonger Aspirant
        - Goremonger Bloodtaker
        - Goremonger Impaler
        - Goremonger Inciter
        - Goremonger Skullclaimer
        - Goremonger Stalker

    + Plague Marine
        - Plague Marine Champion
        - Plague Marine Bombardier
        - Plague Marine Fighter
        - Plague Marine Heavy Gunner
        - Plague Marine Icon Bearer
        - Malignant Plaguecaster
        - Plague Marine Warrior

    + Tempestus Aquilom
        - Aquilon Tempestor
        - Aquilon Grenadier
        - Aquilon Gunfighter
        - Aquilon Gunner
        - Aquilon Marksman
        - Aquilon Precursor
        - Aquilon Servo-sentry
        - Aquilon Trooper

    + Operative Actions
        - Command
        - Dash and Spray
        - Datacoronal Accumulator
        - Expedient Repair
        - Flail
        - Gaze of the Omnissiah
        - Network Override
        - Omniscanner
        - Poisonous Miasma
        - Putrescent Vitality
        - Transfusion Ritual

    + Operative Rules
        - Achillian Eye
        - Brutish
        - Claim Skull
        - Climbing Picks
        - Dynamic
        - Grandfather's Blessing
        - Grenadier (Plague Marine)
        - Gunfight
        - Icon of Contagion
        - Impending Apotheosis
        - Incite the Hunt
        - Khorne's Favour
        - Machine
        - Mechanosuture Array
        - Obsessive Bloodlust
        - Rapid Insertions
        - Repulsive Fortitude
        - Rooftop Stalker
        - Seeker of Divine Arcana
        - Sniper's Vantage
        - Swift Landing
        - Tempestus Veteran
        - Turret
        - Vicious Knife Fighter

    + Weapon Rules
        - Devastating 1
        - 1" Devastating 3
        - Drag
        - Prey
        - Range 7
        - Ritual
        - Toxic

```

</details>

------------------------------------------------------------------------------------------------------------------------
<details>
    <summary><b>v00.08</b></summary>

```md

    + Frame Updates
        - choices [] has been added to operative_actions to handle more complex actions.
        - points [] has been added to operative_rules to handle lists within text.

    + ID Index
        - Updated all ID tables for newly added data.
        - Faction ID added for all previous and newly added factions.

    + Chaos Cult
        - Cult Demagogue
        - Blessed Blade
        - Iconarch
        - Mindwitch
        - Chaos Devotee
        - Chaos Mutant

    + Ravener
        - Ravener Prime
        - Ravener Felltalon
        - Ravener Tremorscythe
        - Ravener Venomspitter
        - Ravener Warrior
        - Ravener Wrecker

    + Scout Squad
        - Scout Sergeant
        - Scout Heavy Gunner
        - Scout Hunter
        - Scout Sniper
        - Scout Tracker
        - Scout Warrior

    + Operative Actions
        - Auspex Scan
        - Distend Dorsal Sac
        - Heinous Deluge
        - Incite Slaughter
        - Incite Urgency
        - Malefic Vortex
        - Optics
        - Ruinous Icon
        - Track Enemy
        - Toxic Lunge

    + Operative Rules
        - Accursed Mutant
        - Accursed Torment
        - Adaptive Equipment
        - Astartes
        - Attuned In Purpose
        - Brute
        - Cut Them Down
        - Grapnel Assault
        - Grapnel Launcher
        - Group Activation
        - Guidance and Experience
        - Hypersensory Hunter
        - Icon Bearer
        - Instinctive Behaviour
        - Neuropredatory Crest
        - Reinforced Carapace
        - Subterranean Ambush
        - Synaptic Link
        - Unnatural Regeneration

    + Weapon Rules
        - Crush
        - Range 2
        - Range 5

```

</details>

------------------------------------------------------------------------------------------------------------------------
<details>
    <summary><b>v00.07</b></summary>

```md

    + ID Index file added.
        + Operative ID table added.
            - Added all existing operative IDs.

        + Operative Actions ID table add.
            - Added all existing operative action IDs.

        + Operative Rules ID table added.
            - Added all existing operative rule IDs.

        + Weapon Rule ID table added.
            - Added all existing weapon rule IDs.

```

</details>

------------------------------------------------------------------------------------------------------------------------

<details>
    <summary><b>v00.06</b></summary>

```md

    + XV26 Stealth Battlesuit unit data added.
        - XV26 Shas'vre
        - XV26 Designator
        - XV26 Infiltrator
        - XV26 Liberator
        - XV26 Lodestar
        - XV26 Neutraliser
        - MV15 Gun Drone
        - MV75 Marker Drone

    + Operative Actions
        - System Jam

    + Operative Rules
        - Covert Protocols
        - Electrochaff Launcher
        - For the Greater Good
        - Homing Beacon
        - Markerlight
        - Multispectrum Sensor Package
        - XV26 Drone Controller

    + Weapon Rules
        - Devastating 4
        - Lethal 4
        - Range 12

```

</details>

------------------------------------------------------------------------------------------------------------------------

<details>
    <summary><b>v00.05</b></summary>

```md

    + Blades of Khaine unit data added.
        - Dire Avenger Exarch
        - Dire Avenger Warrior
        - Howling Banshee Exarch
        - Howling Banshee Warrior
        - Striking Scorpion Exarch
        - Striking Scorpion Warrior

    + Corsair Voidscarred unit data added.
        - Voidscarred Felarch
        - Voidscarred Fate Dealer
        - Voidscarred Gunner
        - Voidscarred Heavy Gunner
        - Voidscarred Kurnathi
        - Voidscarred Kurnite Hunter
        - Voidscarred Shade Runner
        - Voidscarred Soul Weaver
        - Voidscarred Starstorm Duellist
        - Voidscarred Warrior
        - Voidscarred Way Seeker

    + Void-dancer Troupe unit data added.
        - Lead Player
        - Death Jester
        - Player
        - Shadowseer

    + Operative Actions data added.
        - Breach
        - Break Stuff
        - Dakka Dash
        - Fog of Dreams
        - Get it Dun!
        - Grappling Hook
        - Listen In
        - Mirror of Minds
        - Pistol Barrage
        - Soul Channel
        - Soul Heal
        - Warp Fold
        - Warding Shield

    + Operative Rules data added.
        - Banshee Mask
        - Blink Pack
        - Camo Cloak
        - Defence Tactics
        - Erudite Hunter
        - Exarch
        - Faolchu's Bond
        - Lead the Performance
        - Luck of the Laughing God
        - Mandiblasters
        - One Step Ahead
        - Prowling Raider
        - Quick on the Trigger
        - Shimmershield
        - Slicing Attack
        - Veteran Raider

    + Weapon Rules data added.
        - 2" Devastating 2
        - Humbling Cruelty
        - Psychic
        - Range 3
        - Corrected a typo in "Heavy (Dash Only)" name.

```

</details>

------------------------------------------------------------------------------------------------------------------------

<details>
    <summary><b>v00.03</b></summary>

```md

    + Farstalker Kinband unit data added.
        - Kroot Kill-broker
        - Kroot Bow-hunter
        - Kroot Cold-blood
        - Kroot Cut-skin
        - Kroot Heavy Gunner
        - Kroot Hound
        - Kroot Long-sight
        - Kroot Pistolier
        - Kroot Stalker
        - Kroot Tracker
        - Kroot Warrior

    + Hearthkyn Salvagers unit data added.
        - Hearthkyn Theyn
        - Hearthkyn Dozr
        - Hearthkyn Field Medic
        - Hearthkyn Grenadier
        - Hearthkyn Gunner
        - Hearthkyn Jump Pack Warrior
        - Hearthkyn Kinlynk
        - Hearthkyn Kognitaar
        - Hearthkyn Lokatr
        - Hearthkyn Lugger
        - Hearthkyn Warrior

    + Hernkyn Yaegirs unit data added.
        - Yaegir Theyn
        - Yaegir Bladekyn
        - Yaegir Bombast
        - Yaegir Gunner
        - Yaegir Ironbraek
        - Yaegir Riflekyn
        - Yaegir Tracker
        - Yaegir Warrior

    + Kommandos unit data added.
        - Kommando Boss Nob
        - Kommando Bomb Squig
        - Kommando Boy
        - Kommando Breacha Boy
        - Kommando Burna Boy
        - Kommando Comms Boy
        - Kommando Dakka Boy
        - Kommando Grot
        - Kommando Rokkit Boy
        - Kommando Slasha Boy
        - Kommando Snipa Boy

    + Wrecka Krew unit data added.
        - Wrecka Boss Nob
        - Wrecka Bomb Squig
        - Breaka Boy Demolisha
        - Breaka Boy Fighter
        - Breaka Boy Krusha
        - Tankbusta Gunner
        - Tankbusta Rokkiteer

    + Operative Rules data added.
        - Armoured Up
        - Bad-tempered
        - Beast
        - Boom!
        - Brawler
        - Brazen Killer
        - Call The Kill
        - Cold-blooded
        - Dat All You Got?
        - Energise
        - Expendable
        - Eye of the Ancestors
        - Grenadier
        - Hardy
        - HY-Pex Mines
        - I Got a Plan, Ladz
        - Intrepid
        - Irrepressible Hardiness
        - I've Got It
        - Jump Pack
        - Kompetitive Streak
        - Medic!
        - Minefield
        - Outright Conviction
        - Pan Spectral Visor
        - Quick Draw
        - Ready for Anything
        - Reckless Temperament
        - Savage Assault
        - Secure Salvage
        - Shokkwave
        - Sneaky Zogger
        - Stalker
        - Stoopid
        - Tactician
        - Taktical Wot-notz
        - Tracker
        - Veteran Adventurer
        - Vicious Duellist
        - Victory Shriek
        - Weavefield Crest
        - Weavewerke Cloak
        - Well Supplied
        - Wrecka Boss
        - Wroughtlock Negotiation

    + Weapon Rules data added.
        - Accurate 1
        - Beam
        - Bipod
        - Blast 1
        - Blast 3
        - Concealed Position
        - Detonate
        - Devastating 3
        - Explosive
        - Force Impact
        - Heavy (Dash Only)
        - Heavy (Reposition Only)
        - Pulsa
        - Range 4
        - Range 9
        - Salvo
        - Seek Light
        - Smash
        - Torrent 0
        - Torrent 2

```

</details>

------------------------------------------------------------------------------------------------------------------------

<details>
    <summary><b>v00.02</b></summary>

```md

    + Vespid Stingwings unit data added.
        - Oversight Drone
        - Vespid Longsting
        - Vespid Shadestrain
        - Vespid Skyblast
        - Vespid Swarmguard
        - Vespid Warrior

    + Operative Rules data added.
        - Camouflaged
        - Evasive Drone
        - Ghost Rig
        - Neutron Fallout
        - Warrior Instincts

    + Weapon Rules data added.
        - Neutron Bombardment
        - Neutron Fragment
        - Range 6
        - Range 8
        - Skytorch
        - Torrent 0
        - Warrior Instincts

```

</details>

------------------------------------------------------------------------------------------------------------------------

<details>
    <summary><b>v00.01</b></summary>

```md

    + Pathfinders unit data added.
        - Shas'ui Pathfinder
        - Assault Grenadier Pathfinder
        - Blooded Pathfinder
        - Comms Specialist Pathfinder
        - Drone Controller Pathfinder
        - Marksman Pathfinder
        - Medical Technician Pathfinder
        - Shas'la Pathfinder
        - Transpectral Interference Pathfinder
        - Weapons Expert Pathfinder
        - MB3 Recon Drone
        - MV1 Gun Drone
        - MV4 Shield Drone
        - MV7 Marker Drone
        - MV31 Pulse Accelerator Drone
        - MV33 Grav-Inhibitor Drone

    + Vespid Stingwings unit data added.
        - Vespid Strain Leader

    + Operative Rules data added.
        - Analyse
        - Commune
        - Communion Helm
        - Drone
        - Fearless on the Frontline
        - High-intensity Markerlight
        - Inertia Dampener
        - Shield Generator

    + Weapon Rules data added.
        - Accurate
        - Balanced
        - Blast 2
        - Brutal
        - Ceaseless
        - Devastating 2
        - Heavy
        - Hot
        - Lethal 5
        - Limited 1
        - Piercing 1
        - Piercing 2
        - Piercing Crits 1
        - Punishing
        - Relentless
        - Rending
        - Saturate
        - Seek
        - Severe
        - Shock
        - Silent
        - Stun
        - Torrent 1

```

</details>

------------------------------------------------------------------------------------------------------------------------
