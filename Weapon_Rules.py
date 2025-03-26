weaponrules = [
    {   # Accurate X
        "wprname":"Accurate NUM",
        "wprtext":"You can retain up to NUM attack dice as normal successes without rolling them.",
    },
    {   # Balanced
        "wprname":"Balanced",
        "wprtext":"You can re-roll one of your attack dice.",
    },
    {   # Blast 2
        "wprname":"Blast 2",
        "wprtext":"The target you select is the primary target. After shooting the primary target, "
        "shoot with this weapon against each secondary target in an order of your choice "
        "(roll each sequence separately). Secondary targets are other operatives visible to "
        "and within 2 of the primary target (they are all valid targets, regardless of a Conceal order). "
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
    {   # Devastating 2
        "wprname":"Devastating 2",
        "wprtext":"Each retained critical success immediately inflicts 2 damage on the operative "
        "this weapon is being used against. If the rule starts with a distance (e.g. 1\" Devastating 2), "
        "inflict 2 damage on that operative and each other operative visible to and within that distance of it. "
        "Note that success isn't discarded after doing so - it can still be resolved later in the sequence.",
    },
    {   # Heavy
        "wprname":"Heavy",
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
    {   # Punishing
        "wprname":"Punishing",
        "wprtext":"If you retain any critical successes, you can retain one of your fails "
        "as a normal success instead of discarding it.",
    },
    {   # Range 6
        "wprname":"Range 6",
        "wprtext":"Only operatives within 6\" of the active operative can be valid targets.",
    },
    {   # Range 8
        "wprname":"Range 8",
        "wprtext":"Only operatives within 8\" of the active operative can be valid targets.",
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
    {   # Saturate
        "wprname":"Saturate",
        "wprtext":"The defender cannot retain cover saves.",
    },
    {   # Seek
        "wprname":"Seek",
        "wprtext":"When selecting a valid target, operatives with a Conceal order cannot use "
        "terrain for cover. If the rule is Seek Light, they cannot use Light terrain for cover. "
        "While this can allow operatives to be targeted (assuming they're visible), it doesn't "
        "remove their cover save (if any).",
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
    {   # Stun
        "wprname":"Stun",
        "wprtext":"If you retain any critical successes, subtract 1 from the APL stat of the "
        "operative this weapon is being used against until the end of its next activation.",
    },
    {   # Torrent 0
        "wprname":"Torrent 0",
        "wprtext":"Select a valid target as normal as the primary target, then select any "
        "number of other valid targets within 0 of the first valid target as secondary targets. "
        "Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).",
    },
    {   # Torrent 1
        "wprname":"Torrent 1",
        "wprtext":"Select a valid target as normal as the primary target, then select any "
        "number of other valid targets within 1 of the first valid target as secondary targets. "
        "Shoot with this weapon against all of them in an order of your choice (roll each sequence separately).",
    },
    {   # Warrior Instincts
        "wprname":"Warrior Instincts",
        "wprtext":"Whenever this operative is shooting, if you don't spend "
        "Communion points during that sequence, its neutron blaster has the "
        "Accurate 1 weapon rule until the end of that sequence.",
    },
]