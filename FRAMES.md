# Framework Templates

### Operatives

```py

operatives = [
    {   # Operative Name
        "opname":"",
        "stats":{
            "apl":,
            "move":,
            "save":,
            "wounds":,
        },
        "rweaps":[
            {   # Weapon Name
                "wpname":"",
                "atk":,
                "hit":,
                "dmg1":,
                "dmg2":,
                "wprule":[
                ],
            },
        ],
        "mweaps":[
            {   # Weapon Name
                "wpname":"",
                "atk":,
                "hit":,
                "dmg1":,
                "dmg2":,
                "wprule":[
                ],
            },
        ],
        "oprule":[
        ],
        "opact":[
        ],
        "faction":"",
        "keywords":[
        ],
    },
]

```

### Operative Actions

```py

actions = [
    {   # Action Name
        "actname":"",
        "actcost":,
        "acttext1":"",
        "acttext2":"",
        "actrule":"",
    },
]

```

### Operative Rules

```py

oprules = [
    {   # Rule Name
        "oprname":"",
        "oprtext":"",
    },
]

```

### Weapon Rules

```py

weaponrules = [
    {   # Rule Name
        "wprname":"",
        "wprtext":"",
    },
]

```