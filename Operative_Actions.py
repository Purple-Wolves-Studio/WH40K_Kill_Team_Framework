actions = [
    {   # Breach
        "actname":"Breach",
        "actcost":1,
        "acttext1":"Place one of your Breach markers within this operative's control range as "
        "close as possible to a terrain feature within control range of it. Whenever an operative "
        "is within 1\" of that marker, it treats parts of that terrain feature that are no more "
        "than 1\" thick as Accessible terrain.",
        "acttext2":"This operative can perform this action during the Charge or Reposition action, "
        "and it can do so for 1 less AP during those actions. Any remaining move distance can be "
        "used after it does so.",
        "actrule":"This operative cannot perform this action while within control range of an enemy "
        "operative, or if a terrain feature isn't within its control range.",
    },
    {   # Break Stuff
        "actname":"Break Stuff",
        "actcost":1,
        "acttext1":"Select a terrain feature within this operative's control range. If it's an "
        "equipment terrain feature, remove it. Otherwise, place one of your Breach markers within "
        "this operative's control range as close as possible to that terrain feature. Whenever an "
        "operative is within 1\" of that marker, it treats parts of that terrain feature that are "
        "no more than 1\" thick as Accessible terrain.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy "
        "operative, or if a terrain feature isn't within its control range.",
    },
    {   # Dakka Dash
        "actname":"Dakka Dash",
        "actcost":1,
        "acttext1":"Perform a free Dash action and a free Shoot action with this operative in any order. "
        "You can only select a dakka shoota for that Shoot action",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while it has a Conceal order, or while "
        "within control range of an enemy operative.",
    },
    {   # Fog of Dreams
        "actname":"Fog of Dreams",
        "actcost":1,
        "acttext1":"PSYCHIC. Select one ready enemy operative visible to this operative and roll one D6. "
        "Until the end of the turning point, that enemy operative cannot be activated or perform actions "
        "until it's the last enemy operative to be activated, or until your opponent has activated a number "
        "of enemy operatives after this action equal to the result of the D6 (whichever comes first).",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Get it Dun!
        "actname":"Get it Dun!",
        "actcost":1,
        "acttext1":"SUPPORT: Select one other friendly Kommando operative [excluding Bomb Squig] "
        "visible to and within 6\" of this operative. Until the end of that operative's next "
        "activation, add 1 to its APL stat.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of "
        "an enemy operative, or while counteracting",
    },
    {   # Grappling Hook
        "actname":"Grappling Hook",
        "actcost":1,
        "acttext1":"Select a visible point on a terrain feature for this operative. Remove this operative "
        "from the killzone and set it back up within 1\" horizontally of that point in a location it can be "
        "placed, not within control range of enemy operatives, and with that point visible to it. This "
        "operative cannot perform the Operate Hatch action during this action.",
        "acttext2":"",
        "actrule":"This action is treated as a Reposition action. This operative cannot perform this "
        "action while within control range of an enemy operative, or during an activation in which it "
        "performed the Charge or Fall Back action [or vice versa].",
    },
    {   # Listen In
        "actname":"Listen In",
        "actcost":1,
        "acttext1":"SUPPORT: Select one other friendly Kommando operative [excluding Bomb Squig] "
        "visible to and within 6\" of this operative. Until the end of that operative's next "
        "activation, add 1 to its APL stat.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Mirror of Minds
        "actname":"Mirror of Minds",
        "actcost":1,
        "acttext1":"PSYCHIC. Select one enemy operative that's a valid target for and within 8\" of "
        "this operative. Both players roll five D6. Pair your dice with your opponent's dice based on "
        "matching results. For each matching pair, inflict D3 damage on that enemy operative [to a "
        "maximum of 8]. For example, if you rolled 6, 5, 5, 2, 1 and your opponent rolled 6, 5, 4, 3, 1, "
        "you would inflict 3D3 damage on that enemy operative.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Pistol Barrage
        "actname":"Pistol Barrage",
        "actcost":1,
        "acttext1":"Perform two free Shoot actions with this operative (this takes precedence "
        "over action restrictions). You must select its fusion pistol for one action and its "
        "shuriken pistol for the other (in any order).",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while it has a Conceal order, or "
        "during an activation in which it performed the Shoot action (or vice versa).",
    },
    {   # Soul Channel
        "actname":"Soul Channel",
        "actcost":1,
        "acttext1":"PSYCHIC. Select one other friendly CORSAIR VOIDSCARRED operative visible to and "
        "within 6\" of this operative. Until the end of that operative's next activation, add 1 to its APL stat.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Soul Heal
        "actname":"Soul Heal",
        "actcost":1,
        "acttext1":"PSYCHIC. Select one friendly CORSAIR VOIDSCARRED operative visible to and "
        "within 6\" of this operative. That operative regains up to 2D3 lost wounds.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Warp Fold
        "actname":"Warp Fold",
        "actcost":1,
        "acttext1":"PSYCHIC. Select two friendly CORSAIR VOIDSCARRED operatives visible to and within 5\" of "
        "this operative. Remove them both from the killzone and set them back up in each other's previous "
        "locations (in other words, swap their positions). If one of them performed the Charge, Fall Back "
        "or Reposition action during this turning point and the other is ready, the other cannot perform "
        "any of those actions in its activation during this turning point.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
    {   # Warding Shield
        "actname":"Warding Shield",
        "actcost":1,
        "acttext1":"PSYCHIC. Select one friendly CORSAIR VOIDSCARRED operative visible to and within 6\" of "
        "this operative. Until the start of this operative's next activation, until it's incapacitated or "
        "until it performs this action again (whichever comes first), the first time an attack dice inflicts "
        "Normal Dmg on that friendly operative, ignore that inflicted damage.",
        "acttext2":"",
        "actrule":"This operative cannot perform this action while within control range of an enemy operative.",
    },
]