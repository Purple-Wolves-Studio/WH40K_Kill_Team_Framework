oprules = [
    {   # Analyse
        "oprname":"Analyse",
        "oprtext":("Whenever this operative performs the Markerlight action, each other enemy operative "
        "that's both visible to this operative and within 3\" of the enemy operative you selected for that "
        "action also gains one of your Markerlight tokens."),
    },
    {   # Armoured Up
        "oprname":"Armoured Up",
        "oprtext":"Whenever an enemy operative is shooting this operative, or this operative is "
        "fighting or retaliating, your opponent cannot retain attack dice results of less than "
        "6 as critical successes (e.g. as a result of the Lethal, Rending or Severe weapon rules).",
    },
    {   # Bad-tempered
        "oprname":"Bad-tempered",
        "oprtext":"Whenever an enemy operative performs the Fight action, if this operative is a valid operative to fight against, you can force them to select this operative to fight against instead. Whenever an enemy operative ends the Charge action within control range of another friendly FARSTALKER KINBAND operative within 3\" of this operative, if this operative isn't within control range of enemy operatives, this operative can immediately perform a free Charge action, but must end that move within control range of that enemy operative.",
    },
    {   # Beast
        "oprname":"Beast",
        "oprtext":"This operative cannot perform any actions other than Charge, Dash, "
        "Fall Back, Fight, Gather, Guard, Reposition, Pick Up Marker and Place Marker. "
        "It cannot use any weapons that aren't on its datacard.",
    },
    {   # Boom!
        "oprname":"Boom!",
        "oprtext":"If this operative is incapacitated during a battle in which it "
        "hasn't used its explosives, roll one D6, or two D6 if you wish. If any result "
        "is a 4+, this operative performs a free Shoot action with its explosives "
        "before it's removed from the killzone.",
    },
    {   # Brawler
        "oprname":"Brawler",
        "oprtext":"Whenever this operative is fighting or retaliating; enemy operatives cannot assist. "
        "If it's incapacitated, you can strike the enemy operative in that sequence with one of your "
        "unresolved successes before it's removed from the killzone.",
    },
    {   # Brazen Killer
        "oprname":"Brazen Killer",
        "oprtext":"Whenever this operative incapacitates an enemy operative with its "
        "wroughtlock revolvers, roll one D6 separately for each other enemy operative "
        "visible to and within 2\" of that enemy operative: if the result is higher "
        "than that other enemy operative's APL stat, subtract 1 from its APL stat "
        "until the end of its next activation.",
    },
    {   # Call The Kill
        "oprname":"Call The Kill",
        "oprtext":"STRATEGIC GAMBIT. Select one enemy operative to be your mark for the turning point. "
        "Whenever a friendly FARSTALKER KINBAND operative is shooting against, fighting against or "
        "retaliating against your mark, that friendly operative's weapons have the Balanced weapon rule. "
        "Whenever your mark is incapacitated, you can select a new enemy operative to be your mark for "
        "the turning point (and can continue to do so during this turning point).",
    },
    {   # Camouflaged
        "oprname":"Camouflaged",
        "oprtext":"Whenever an operative is shooting this operative, ignore the Piercing weapon rule "
        "and all cover saves are retained as critical successes. This rule has no effect if this operative "
        "isn't selected as the valid target, e.g. if it's a secondary target from the Blast weapon rule.",
    },
    {   # Cold-blooded
        "oprname":"Cold-blooded",
        "oprtext":"Whenever this operative is shooting against, fighting against "
        "or retaliating against a wounded enemy operative, this operative's weapons "
        "have the Lethal 5+ weapon rule; if that enemy operative is also injured, "
        "this operative's weapons also have the Rending weapon rule.",
    },
    {   # Commune
        "oprname":"Commune",
        "oprtext":"""When selecting your operatives for the battle, also select one Vespid Stingwing strategy ploy.
        Whenever this operative is in the killzone and not within control range of enemy operatives, 
        that ploy costs 0 CP.""",
    },
    {   # Communion Helm
        "oprname":"Communion Helm",
        "oprtext":"Once during each of this operative's activations, you can spend 1 Communion point for free.",
    },
    {   # Dat All You Got?
        "oprname":"Dat All You Got?",
        "oprtext":"After this operative fights or retaliates, if it wasn't incapacitated, "
        "you can inflict D3 damage on the enemy operative in that sequence.",
    },
    {   # Drone
        "oprname":"Drone",
        "oprtext":"""This operative can only perform Charge, Dash, Fall Back, Fight, Reposition, and Shoot actions.
        It cannot use any other weapons.
        When determining control of an objective marker, treat this operative's APL stat as 1 lower.
        When determining what is visible to this operative, the round disc at the top is its head.""",
    },
    {   # Evasive Drone
        "oprname":"Evasive Drone",
        "oprtext":"This operative can only perform Aerial Guidance, Charge, Dash, Fall Back, "
        "Fight, and Reposition. When determining control of objective markers, treat this "
        "operative's APL stat as 1 lower. When determining what's visible to this operative, "
        "the round disc at the top is its head. When this operative has a Conceal order and "
        "is in cover, it cannot be selected as a valid target, taking precedence over all "
        "other rules. When an operative is shooting this operative, ignore the Piercing weapon rule.",
    },
    {   # Expendable
        "oprname":"Expendable",
        "oprtext":"This operative is ignored for your opponent's kill/elimination op "
        "(when it's incapacitated, and when determining your starting number of operatives). "
        "It's also ignored for victory conditions that require operatives to 'escape', 'survive' "
        "or be incapacitated (if it escapes/survives/is incapacitated, determining how many operatives "
        "must escape/survive/be incapacitated, etc.).",
    },
    {   # Eye of the Ancestors
        "oprname":"Eye of the Ancestors",
        "oprtext":"STRATEGIC GAMBIT. Select one enemy operative, or up to two "
        "enemy operatives if three or more friendly HEARTHKYN SALVAGER operatives "
        "are incapacitated. Each of those enemy operatives gains one of your Grudge tokens.",
    },
    {   # Fearless on the Frontline
        "oprname":"Fearless on the Frontline",
        "oprtext":("This operative can perform the Markerlight action while within control range of an enemy "
        "operative, taking precedence over the Markerlight action's normal conditions. In addition, "
        "this operative can perform the Fall Back action for 1 less AP."),
    },
    {   # Ghost Rig
        "oprname":"Ghost Rig",
        "oprtext":"While this operative has a Conceal order, your opponent cannot select it as a "
        "valid target unless it's within 6\" of the operative trying to target it. Note that this rule "
        "has no effect if this operative isn't selected as the valid target, e.g. if it's a secondary "
        "target from the Blast weapon rule.",
    },
    {   # Grenadier
        "oprname":"Grenadier",
        "oprtext":"This operative can use frag, krak, smoke and stun grenades "
        "(see universal equipment). Doing so doesn't count towards any limited "
        "uses you have (i.e. if you also select those grenades from equipment "
        "for other operatives). Whenever this operative is using a frag or krak "
        "grenade, improve the Hit stat of that weapon by 1.",
    },
    {   # Hardy
        "oprname":"Hardy",
        "oprtext":"Whenever an attack dice would inflict Critical Dmg on this operative, "
        "you can choose for that attack dice to inflict Normal Dmg instead.",
    },
    {   # High-intensity Markerlight
        "oprname":"High-intensity Markerlight",
        "oprtext":"When this operative uses Markerlight, the selected enemy operative gains two Markerlight tokens.",
    },
    {   # HY-Pex Mines
        "oprname":"HY-Pex Mines",
        "oprtext":"Whenever one of your reverse-side down Minefield markers is both within an "
        "enemy operative's control range and not within a friendly HERNKYN YAEGIR operative's "
        "control range, flip the marker over. If it's a blank, there's no effect. If it's a "
        "HY-Pex mine, inflict 3 damage on that enemy operative and roll one D6: if the result is "
        "less than that enemy operative's Save stat, inflict additional damage on it equal to the "
        "dice result; regardless of the result, if it isn't incapacitated, end its action (if any), "
        "even if that action's effects aren't fulfilled. If it cannot be placed, move it the minimum "
        "amount to do so. Regardless, that marker isn't removed.",
    },
    {   # I Got a Plan, Ladz
        "oprname":"I Got a Plan, Ladz",
        "oprtext":"Once during each of this operative's activations, it can "
        "perform the Pick Up Marker, Place Marker or a mission action for 1 less AP.",
    },
    {   # Inertial Dampener
        "oprname":"Inertial Dampener",
        "oprtext":"You can ignore any changes to the Hit stat of this operative's Marksman Rail Rifle.",
    },
    {   # Intrepid
        "oprname":"Intrepid",
        "oprtext":"Whenever you spend a Resourceful point for this operative, the following "
        "take precedence; if you add 1 to its APL stat, it lasts until the start of its next "
        "activation instead, and if it regains lost wounds, it regains up to 4 instead.",
    },
    {   # Irrepressible Hardiness
        "oprname":"Irrepressible Hardiness",
        "oprtext":"If this operative is incapacitated during the Fight action, you can "
        "strike the enemy operative in that sequence with one of your unresolved successes "
        "before this operative is removed from the killzone.",
    },
    {   # I've Got It
        "oprname":"I've Got It",
        "oprtext":"Once during each of this operative's activations, "
        "it can perform a mission action for 1 less AP.",
    },
    {   # Jump Pack
        "oprname":"Jump Pack",
        "oprtext":"Whenever this operative performs an action in which it moves, it can FLY. "
        "If it does, don't move it. Instead, remove it from the killzone and set it back up "
        "wholly within a distance equal to its Move stat (or 3\" if it was a Dash) of its original "
        "location, measuring the horizontal distance only (in a killzone that uses the close "
        "quarters rules, e.g. Killzone: Gallowdark, this distance cannot be measured over or through "
        "Wall terrain, and that operative cannot be set up on the other side of an access point, in other "
        "words it cannot FLY through an open hatchway). Note that it gains no additional distance when "
        "performing the Charge action. It must be set up in a location it can be placed, and unless it's "
        "the Charge action, it cannot be set up within control range of an enemy operative.",
    },
    {   # Kompetitive Streak
        "oprname":"Kompetitive Streak",
        "oprtext":"Once per Shoot action, if this operative shoots an enemy operative that "
        "another friendly operative has already shot during this turning point, you gain "
        "1 Wrecka point. Determine this when you select a valid target, but you can include "
        "any secondary targets when doing so (e.g. from the Blast weapon rule).",
    },
    {   # Medic!
        "oprname":"Medic!",
        "oprtext":"The first time during each turning point that another friendly "
        "HEARTHKYN SALVAGER operative would be removed from the killzone as incapacitated "
        "while visible to and within 3\" of this operative, you can use this rule, providing "
        "neither this nor that operative is within control range of an enemy operative. If you do, "
        "that friendly operative isn't incapacitated and has 1 wound remaining. That friendly operative "
        "can then immediately perform a free Dash action, but must end that move within this operative's "
        "control range. Subtract 1 from this and that operative's APL stats until the end of their next "
        "activations respectively, and if this rule was used during that friendly operative's activation, "
        "that activation ends. You cannot use this rule if this operative is incapacitated.",
    },
    {   # Minefield
        "oprname":"Minefield",
        "oprtext":"You have five Minefield markers for the battle. On the reverse side, "
        "three of them are HY-Pex mines (see right) and two are blank. Set up all your "
        "Minefield markers as if they were one item of equipment. Each must be set up "
        "reverse-side down (their specifics aren't revealed), more than 2\" from other "
        "markers, access points and Accessible terrain, and more than 6\" from your opponent's "
        "drop zone and your other Minefield markers. Whenever this operative is readied, if it's "
        "not within control range of enemy operatives, you can reset one of your flipped Minefield "
        "markers that's within its control range (flip the marker back over again).",
    },
    {   # Neutron Fallout
        "oprname":"Neutron Fallout",
        "oprtext":"Once during each enemy operative's activation, as soon as it's "
        "within 2\" of one of your Neutron Fallout markers, inflict D3 damage on "
        "that operative (multiple markers aren't cumulative).",
    },
    {   # Outright Conviction
        "oprname":"Outright Conviction",
        "oprtext":"The first time this operative would be incapacitated during the battle, "
        "it's not incapacitated, has 1 wound remaining and cannot be incapacitated for the "
        "remainder of the action. All remaining attack dice are discarded (including yours "
        "if this operative is fighting or retaliating).",
    },
    {   # Pan Spectral Visor
        "oprname":"Pan Spectral Visor",
        "oprtext":"Whenever this operative is shooting an operative "
        "within 6\" of it; this operative's weapons have the Seek Light "
        "weapon rule and that operative cannot be obscured.",
    },
    {   # Quick Draw
        "oprname":"Quick Draw",
        "oprtext":"Once per turning point, when an enemy operative is performing the Shoot action "
        "and this operative is selected as the valid target (or if it will be a secondary target "
        "from the Blast weapon rule), if this operative is ready, you can interrupt that action "
        "to use this rule. If you do, this operative can immediately perform a free Shoot action "
        "with its dual Kroot pistols (focused) against that enemy operative (you can change its order "
        "to Engage to do so), but that enemy operative must be a valid target.",
    },
    {   # Ready for Anything
        "oprname":"Ready for Anything",
        "oprtext":"Once per turning point, during a friendly WARRIOR operative's activation, "
        "you can use the Meat, Piercing Shot or Toxin Shot rule (see faction equipment) for "
        "that operative. Doing so doesn't count for its once per turning point limit.",
    },
    {   # Reckless Temperament
        "oprname":"Reckless Temperament",
        "oprtext":"Normal Dmg of 4 or more inflicts 1 less damage on this operative; "
        "if this operative has an Engage order, Critical Dmg of 4 or more also inflicts "
        "1 less damage on this operative.",
    },
    {   # Savage Assault
        "oprname":"Savage Assault",
        "oprtext":"The first time this operative performs the Fight action during each of "
        "its activations, if neither it nor the enemy operative in that sequence is incapacitated, "
        "this operative can immediately perform a free Fight action afterwards, but you cannot "
        "select any other enemy operative to fight against during that action (and only if it's still "
        "valid to fight against). This takes precedence over action restrictions.",
    },
    {   # Secure Salvage
        "oprname":"Secure Salvage",
        "oprtext":"Whenever an enemy operative is shooting against, fighting against or "
        "retaliating against this operative, if this operative contests an objective "
        "marker or one of your mission markers, in the Resolve Attack Dice step, you "
        "can subtract 1 from the damage inflicted on it from one success.",
    },
    {   # Shield Generator
        "oprname":"Shield Generator",
        "oprtext":("This operative ignores the Piercing weapon rule. Once per turn, when an attack die "
        "inflicts Normal Damage on this operative, you can ignore that inflicted damage. "
        "You can use Saviour Protocols for 0 CP if this is the specified Drone operative."),
    },
    {   # Shokkwave
        "oprname":"Shokkwave",
        "oprtext":"Whenever an operative is within x\" of your Pulsa marker (see left), "
        "worsen the Hit stat of its weapons by 1 and subtract 2\" from its Move stat. "
        "This is cumulative with being injured. X is that marker's Pulsa points. In the Ready "
        "step of each Strategy phase, subtract 1 from your Pulsa marker's points. If a Pulsa "
        "marker ever has 0 points, remove it.",
    },
    {   # Sneaky Zogger
        "oprname":"Sneaky Zogger",
        "oprtext":"This operative cannot have an Engage order. Whenever this operative is in cover, "
        "it cannot be selected as a valid target, taking precedence over all other rules "
        "(e.g. Seek, Vantage terrain) except being within 2\".",
    },
    {   # Stalker
        "oprname":"Stalker",
        "oprtext":"This operative can perform the Charge action while it has a Conceal order.",
    },
    {   # Stoopid
        "oprname":"Stoopid",
        "oprtext":"In the Firefight phase, whenever you determine this operative's order, you "
        "cannot select Conceal. This operative cannot perform any actions other than Charge, "
        "Dash, Fight, Reposition and Shoot. It cannot use any weapons that aren't on its datacard.",
    },
    {   # Tactician
        "oprname":"Tactician",
        "oprtext":"STRATEGIC GAMBIT. Place either your Attack or Defence marker in the killzone. "
        "Whenever a friendly HEARTHKYN SALVAGER operative is shooting against, fighting against "
        "or retaliating against an enemy operative that's within 3\" of your Attack marker, you can "
        "re-roll one of your attack dice. Whenever an enemy operative is shooting a friendly "
        "HEARTHKYN SALVAGER operative that's within 3\" of your Defence marker, you can re-roll one of "
        "your defence dice. In the Ready step of the next Strategy phase, remove that marker.",
    },
    {   # Taktical Wot-notz
        "oprname":"Taktical Wot-notz",
        "oprtext":"You can do each of the following once per turning point: "
        "One friendly KOMMANDO BOY operative can perform the Smoke Grenade action. "
        "One friendly KOMMANDO BOY operative can perform the Stun Grenade action. "
        "The rules for these actions are found in universal equipment. "
        "Performing these actions using this rule doesn't count towards their action limits "
        "(i.e. if you also select those grenades from equipment).",
    },
    {   # Tracker
        "oprname":"Tracker",
        "oprtext":"Whenever this operative is shooting against or fighting "
        "against an expended operative within 6\" of it, this operative's "
        "weapons have the Punishing weapon rule.",
    },
    {   # Veteran Adventurer
        "oprname":"Veteran Adventurer",
        "oprtext":"In the Ready step of each Strategy phase after the first, if this "
        "operative isn't within control range of enemy operatives, you gain 1 Resourceful point.",
    },
    {   # Vicious Duellist
        "oprname":"Vicious Duellist",
        "oprtext":"Whenever this operative is fighting or retaliating, for each attack dice "
        "your opponent discards as a fail, inflict 1 damage on the enemy operative in that sequence.",
    },
    {   # Victory Shriek
        "oprname":"Victory Shriek",
        "oprtext":"Whenever your mark is incapacitated, you can select one friendly "
        "FARSTALKER KINBAND operative within 6\" of this operative. Until the end of "
        "the battle, that operative's weapons have the Balanced weapon rule. "
        "Each friendly operative can only be selected for this rule once per battle.",
    },
    {   # Weavefield Crest
        "oprname":"Weavefield Crest",
        "oprtext":"The first time an attack dice inflicts 4 or more damage on "
        "this operative during the battle, ignore that inflicted damage.",
    },
    {   # Weavewerke Cloak
        "oprname":"Weavewerke Cloak",
        "oprtext":"Whenever an operative is shooting this operative; "
        "Ignore the Saturate weapon rule. If you can retain any cover "
        "saves, you can retain one additional cover save, or you can "
        "retain one cover save as a critical success instead. This isn't "
        "cumulative with improved cover saves from Vantage terrain",
    },
    {   # Well Supplied
        "oprname":"Well Supplied",
        "oprtext":"You can select one additional equipment option.",
    },
    {   # Wrecka Boss
        "oprname":"Wrecka Boss",
        "oprtext":"Whenever this operative performs the Shoot or Fight action "
        "(excluding Guard), you gain 1 Wrecka point.",
    },
    {   # Wroughtlock Negotiation
        "oprname":"Wroughtlock Negotiation",
        "oprtext":"STRATEGIC GAMBIT. This operative can immediately perform "
        "a free Shoot action (you can change its order to Engage to do so).",
    },
]