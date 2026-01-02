# Framework Templates

Use the following templates for any additions or updates to the framework.

<details>
<summary><b>Faction Template</b></summary>

```yaml

faction: # String: Name of the Faction
faction_keyword: # List: Core tags shared by all units (e.g., [Ork] or [Aeldari])
units: # List of units in the faction
  # --- Operative Name ---
  - id: # String: Unique alphanumeric ID for indexing/searching
    name: # String: The specific name of the operative
    stats: # List: Operative stats
      apl: # Integer: Action Point Limit
      move: # Integer: Movement distance (usually in inches)
      save: # Integer: Armor Save value (the result needed on a D6)
      wounds: # Integer: Total health/hit points
    ranged: # List: Ranged weapon profiles
      - name: # String: Weapon name (Add entire data set per profile)
        attack: # Integer: Number of attack dice rolled
        hit: # Integer: Weapon Skill (the result needed to hit)
        damage: # List [Int, Int]: [Normal Damage, Critical Damage]
        rule: # List: Special weapon traits (e.g., [Brutal, Lethal 5+])
    melee: # List: Melee weapon profiles
      - name: # String: Weapon name (Add entire data set per profile)
        attack: # Integer: Number of attack dice rolled
        hit: # Integer: Weapon Skill (the result needed to hit)
        damage: # List [Int, Int]: [Normal Damage, Critical Damage]
        rule: # List: Special weapon traits (e.g., [Brutal, Lethal 5+])
    rule: # List: Passive abilities or special rules unique to this unit
    action: # List: Unique actions the unit can perform (Strategic/Tactical ploys)
    keyword: # List: Specific unit tags (e.g., [Leader, Warrior, Scout])

```
</details>

<details>
<summary><b>Operative Actions</b></summary>

```yaml

actions: # List of operative actions
  # --- Action Name ---
  - id: # Unique Alphanumeric ID for referencing in unit files
    name: # String: Name of the action
    cost: # Integer: How many Action Points (AP) it costs
    type: # String: Provides context for certain actions (e.g., [Psychic, Support])
    text: > # String: Using '>' allows for multi-line descriptions
      Full description of the action goes here. It will be 
      stored as a single long string.
    rule: > # String: Using '>' allows for multi-line descriptions
      Full description of the action rule(s) here. It will be 
      stored as a single long string.

```
</details>

<details>
<summary><b>Operative Rules</b></summary>

```yaml

rules: # List of operative rules
  # --- Rule Name ---
  - id: # Unique Alphanumeric ID for referencing in unit files
    name: # String: Name of the rule
    text: > # String: Using '>' allows for multi-line descriptions
      Full description of the action goes here. It will be 
      stored as a single long string.

```
</details>

<details>
<summary><b>Weapon Rules</b></summary>

```yaml

rules: # List of operative rules
  # --- Rule Name ---
  - id: # Unique Alphanumeric ID for referencing in unit files
    name: # String: Name of the rule
    text: > # String: Using '>' allows for multi-line descriptions
      Full description of the action goes here. It will be 
      stored as a single long string.

```
</details>