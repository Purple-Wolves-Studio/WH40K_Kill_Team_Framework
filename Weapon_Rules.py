weaponrules = [
    {   # Accurate 1
        "wprname":"Accurate 1",
        "wprtext":"You can retain up to 1 attack dice as normal successes without rolling them.",
    },
    {   # Balanced
        "wprname":"Balanced",
        "wprtext":"You can re-roll one of your attack dice.",
    },
    {   # Beam
        "wprname":"Beam",
        "wprtext":"Whenever this operative is shooting with this weapon, each retained "
        "critical success immediately inflicts D3 damage on each other operative along "
        "one (and only one) beam line (roll separately for each operative), but the target "
        "isn't affected. An operative is along a beam line if a targeting line can be drawn "
        "from this operative to its base, and that line crosses the base of the original "
        "target but doesn't cross Heavy terrain.",
    },
    {   # Bipod
        "wprname":"Bipod",
        "wprtext":"Whenever this operative is shooting with this weapon, if it hasn't moved "
        "during the activation, or if it's a counteraction, this weapon has the Ceaseless "
        "weapon rule. Note this operative isn't restricted from moving after shooting.",
    },
    {   # Blast 1
        "wprname":"Blast 1",
        "wprtext":"The target you select is the primary target. After shooting the primary target, "
        "shoot with this weapon against each secondary target in an order of your choice "
        "(roll each sequence separately). Secondary targets are other operatives visible to "
        "and within 1 of the primary target (they are all valid targets, regardless of a Conceal order). "
        "Secondary targets are in cover and obscured if the primary target was.",
    },
    {   # Blast 2
        "wprname":"Blast 2",
        "wprtext":"The target you select is the primary target. After shooting the primary target, "
        "shoot with this weapon against each secondary target in an order of your choice "
        "(roll each sequence separately). Secondary targets are other operatives visible to "
        "and within 2 of the primary target (they are all valid targets, regardless of a Conceal order). "
        "Secondary targets are in cover and obscured if the primary target was.",
    },
    {   # Blast 3
        "wprname":"Blast 3",
        "wprtext":"The target you select is the primary target. After shooting the primary target, "
        "shoot with this weapon against each secondary target in an order of your choice "
        "(roll each sequence separately). Secondary targets are other operatives visible to "
        "and within 3 of the primary target (they are all valid targets, regardless of a Conceal order). "
        "Secondary targets are in cover and obscured if the primary target was.",
    },
    {   # Brutal
        "wprname":"Brutal",
        "wprtext":"Your opponent can only block with critical successes.",
    },
    {   # Ceaseless
        "wprname":"Ceaseless",
        "wprtext":"You can re-roll any of your attack dice results of one result (e.g. results of 2).",
    },
    {   # Concealed Position
        "wprname":"Concealed Position",
        "wprtext":"This operative can only use this weapon the first time it's performing the "
        "Shoot action during the battle.",
    },
    {   # Detonate
        "wprname":"Detonate",
        "wprtext":"The first time you would inflict damage on an enemy operative with this "
        "weapon profile during the battle, inflict D6+6 damage on that enemy operative and "
        "each other operative within its control range if it's a normal success, or 2D6+6 damage "
        "if it's a critical success (roll separately for each). Then the action ends and you gain "
        "1 Wrecka point, plus 1 for each operative that was incapacitated during that action. "
        "Damage from this weapon rule cannot be ignored or reduced.",
    },
    {   # Devastating 2
        "wprname":"Devastating 2",
        "wprtext":"Each retained critical success immediately inflicts 2 damage on the operative "
        "this weapon is being used against. If the rule starts with a distance (e.g. 1\" Devastating 2), "
        "inflict 2 damage on that operative and each other operative visible to and within that distance of it. "
        "Note that success isn't discarded after doing so - it can still be resolved later in the sequence.",
    },
    {   # Devastating 3
        "wprname":"Devastating 3",
        "wprtext":"Each retained critical success immediately inflicts 3 damage on the operative "
        "this weapon is being used against. If the rule starts with a distance (e.g. 1\" Devastating 2), "
        "inflict 2 damage on that operative and each other operative visible to and within that distance of it. "
        "Note that success isn't discarded after doing so - it can still be resolved later in the sequence.",
    },
    {   # Explosive
        "wprname":"Explosive",
        "wprtext":"This operative can perform the Shoot action with this weapon while "
        "within control range of an enemy operative. Don't select a valid target. "
        "Instead, this operative is always the primary target and cannot be in cover or obscured.",
    },
    {   # Force Impact
        "wprname":"Force Impact",
        "wprtext":"Whenever this operative is fighting with this weapon, if it's "
        "performed the Charge action during the activation, this weapon has the Brutal weapon rule.",
    },
    {   # Heavy
        "wprname":"Heavy",
        "wprtext":"An operative cannot use this weapon in an activation in which it moved, "
        "and it cannot move in an activation in which it used this weapon. This weapon rule "
        "has no effect on preventing the Guard action.",
    },
    {   # Heavy [Reposition Only]
        "wprname":"Heavy [Dash Only]",
        "wprtext":"An operative cannot use this weapon in an activation in which it moved, "
        "and it cannot move in an activation in which it used this weapon. If the rule is "
        "Heavy (x only), where x is a move action, only that move is allowed, e.g. Heavy (Dash only). "
        "This weapon rule has no effect on preventing the Guard action.",
    },
    {   # Heavy [Reposition Only]
        "wprname":"Heavy [Reposition Only]",
        "wprtext":"An operative cannot use this weapon in an activation in which it moved, "
        "and it cannot move in an activation in which it used this weapon. If the rule is "
        "Heavy (x only), where x is a move action, only that move is allowed, e.g. Heavy (Dash only). "
        "This weapon rule has no effect on preventing the Guard action.",
    },
    {   # Hot
        "wprname":"Hot",
        "wprtext":"After an operative uses this weapon, roll one D6: if the result is less than "
        "the weapon's Hit stat, inflict damage on that operative equal to the result multiplied "
        "by two. If it's used multiple times in one action (e.g. Blast), still only roll one D6.",
    },
    {   # Lethal 5
        "wprname":"Lethal 5",
        "wprtext":"Your successes equal to or greater than 5 are critical successes, e.g. Lethal 5+.",
    },
    {   # Limited 1
        "wprname":"Limited 1",
        "wprtext":"After an operative uses this weapon a number of times in the battle "
        "equal to 1, they no longer have it. If it's used multiple times in one action "
        "(e.g. Blast), treat this as one use.",
    },
    {   # Neutron Bombardment
        "wprname":"Neutron Bombardment",
        "wprtext":"Place one of your Neutron Fallout markers within the primary target's control range.",
    },
    {   # Neutron Fragment
        "wprname":"Neutron Fragment",
        "wprtext":"If the target of this weapon isn't incapacited but you resolve any "
        "attack dice, the target gains one of your Neutron Fragment tokens. In the Ready step "
        "of each Strategy phase, separately inflict D3 damage on each operative for each of "
        "your Neutron Fragment tokens it has.",
    },
    {   # Piercing 1
        "wprname":"Piercing 1",
        "wprtext":"The defender collects 1 less defence dice.",
    },
    {   # Piercing 2
        "wprname":"Piercing 2",
        "wprtext":"The defender collects 2 less defence dice.",
    },
    {   # Piercing Crits 1
        "wprname":"Piercing Crits 1",
        "wprtext":"The defender collects 1 less defence dice. This only comes into effect "
        "if you retain any critical successes.",
    },
    {   # Pulsa
        "wprname":"Pulsa",
        "wprtext":"Don't select a valid target. Instead, place your Pulsa marker visible "
        "to this operative, or on Vantage terrain of a terrain feature that's visible to "
        "this operative. That marker gains 1 Pulsa point, then roll attack dice: it gains "
        "1 additional Pulsa point for each success (to a maximum of 3 additional points). "
        "Separately inflict D3 damage on each operative wholly within x\" of that marker, "
        "where x is that marker's Pulsa points. Then the action ends.",
    },
    {   # Punishing
        "wprname":"Punishing",
        "wprtext":"If you retain any critical successes, you can retain one of your fails "
        "as a normal success instead of discarding it.",
    },
    {   # Range 4
        "wprname":"Range 4",
        "wprtext":"Only operatives within 4\" of the active operative can be valid targets.",
    },
    {   # Range 6
        "wprname":"Range 6",
        "wprtext":"Only operatives within 6\" of the active operative can be valid targets.",
    },
    {   # Range 8
        "wprname":"Range 8",
        "wprtext":"Only operatives within 8\" of the active operative can be valid targets.",
    },
    {   # Range 9
        "wprname":"Range 9",
        "wprtext":"Only operatives within 9\" of the active operative can be valid targets.",
    },
    {   # Relentless
        "wprname":"Relentless",
        "wprtext":"You can re-roll any of your attack dice.",
    },
    {   # Rending
        "wprname":"Rending",
        "wprtext":"If you retain any critical successes, you can retain one of your "
        "normal successes as a critical success instead.",
    },
    {   # Salvo
        "wprname":"Salvo",
        "wprtext":"Select up to two valid targets. Shoot with this weapon against both "
        "of them in an order of your choice (roll each sequence separately).",
    },
    {   # Saturate
        "wprname":"Saturate",
        "wprtext":"The defender cannot retain cover saves.",
    },
    {   # Seek
        "wprname":"Seek",
        "wprtext":"When selecting a valid target, operatives with a Conceal order cannot use "
        "terrain for cover. While this can allow operatives to be targeted (assuming they're visible), "
        "it doesn't remove their cover save (if any).",
    },
    {   # Seek Light
        "wprname":"Seek Light",
        "wprtext":"When selecting a valid target, operatives with a Conceal order cannot use "
        "Light terrain for cover. While this can allow operatives to be targeted "
        "(assuming they're visible), it doesn't remove their cover save (if any).",
    },
    {   # Severe
        "wprname":"Severe",
        "wprtext":"If you don't retain any critical successes, you can change one of your "
        "normal successes to a critical success. Any rules that take effect as a result of "
        "retaining a critical success (e.g. Devastating, Piercing Crits, etc.) still do.",
    },
    {   # Shock
        "wprname":"Shock",
        "wprtext":"The first time you strike with a critical success in each sequence, "
        "also discard one of your opponent's unresolved normal successes (or one of their "
        "critical successes if there are none).",
    },
    {   # Silent
        "wprname":"Silent",
        "wprtext":"An operative can perform the Shoot action with this weapon while it has a Conceal order.",
    },
    {   # Skytorch
        "wprname":"Skytorch",
        "wprtext":"An operative can only use this weapon during an activation in "
        "which it performed the Reposition action with FLY. If it does, don't select "
        "a valid target. Instead, shoot against each operative within its torch zone "
        "(excluding operatives wholly underneath Vantage terrain); they aren't in cover "
        "or obscured. Roll each sequence separately in order of furthest operative to closest. "
        "The torch zone is the area between the operative's current and previous location. "
        "A 28mm round Skytorch marker can be temporarily placed underneath this operative before "
        "it moves to help determine this. Torrent 0\" means you cannot select secondary targets "
        "outside of its torch zone, but this weapon still has the Torrent weapon rule for all other "
        "rules purposes, e.g. the Condensed Stronghold rule (see Killzone: Volkus, Kill Team Core Book).",
    },
    {   # Smash
        "wprname":"Smash",
        "wprtext":"Whenever you strike, you can move the enemy operative in a straight line increment of up "
        "to 1\". If you do, it must end the move further away from this operative and in a location it can be "
        "placed. Then move this operative in a straight line increment of up to 1\", but it must end that move "
        "within that enemy operative's control range (if either isn't possible, you cannot move them).",
    },
    {   # Stun
        "wprname":"Stun",
        "wprtext":"If you retain any critical successes, subtract 1 from the APL stat of the "
        "operative this weapon is being used against until the end of its next activation.",
    },
    {   # Torrent 0
        "wprname":"Torrent 0",
        "wprtext":"Cannot select secondary targets, but works the same otherwise... what?",
    },
    {   # Torrent 1
        "wprname":"Torrent 1",
        "wprtext":"Select a valid target as normal as the primary target, then select any "
        "number of other valid targets within 1 of the first valid target as secondary targets. "
        "Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).",
    },
    {   # Torrent 2
        "wprname":"Torrent 2",
        "wprtext":"Select a valid target as normal as the primary target, then select any "
        "number of other valid targets within 2 of the first valid target as secondary targets. "
        "Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).",
    },
    {   # Warrior Instincts
        "wprname":"Warrior Instincts",
        "wprtext":"Whenever this operative is shooting, if you don't spend "
        "Communion points during that sequence, its neutron blaster has the "
        "Accurate 1 weapon rule until the end of that sequence.",
    },
]