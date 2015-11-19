# Data Model

### There are five basic types of data:

- Actions: describes what the player can *do*
- Entities: describes what the player can do things *with*
- Places: describes where the player *does things*
- Meta: describes the game, provides the title, etc

## Actions

#### Actions are defined as descriptions of what the player can do.

Any way the player interacts with anything is here. They usually take a set of
entities as an argument.

For example:

    attack Jeff with sword

Is parsed as:

    attack
      what `Jeff`
      with `sword`

Actions then use the information about the entities to generate a reaction.
This reaction usually modifies the game world somehow, for instance the
attack command will examine the `sword` and check it's `hit-chance` and
it's `damage`.

It will then make an attempt to hit the entity with the `sword` and reduce
it's `hit_points` by `damage`.

### Interpreting Actions

A major challenge of this type of input is figuring out what the person typing
is trying to communicate.

    ¬ eat candy
      might be exactly the same as
    ¬ open candy and eat it
      or
    ¬ hit zombie with shoe
      might mean
    ¬ attack zombie with shoe


It's important therefor that we define special grammar that change how an
action will be interpreted.

- `and` should break an action and start another action, assuming the first
one ran correctly

- `it` should be guessed. If the player inputs an attack command and there is
only one entity that can be attacked in the room, assume it means that entity,
unless that entity has the `important` flag, in which case ask for confirmation

 It can also be guessed by previous context. If a player referred to some
 command earlier like `open candy` and their next command uses an `it`, there's a good chance they're talking about the candy

- `with` is straightforward, it defines the entity we're using to complete
the action

### Interpreting Movement

I think it's also important I mention how I handled movement. At any given
stage in a game, there are usually quite a few places a player will want to
go.

    ¬ go through door
      if the door is in the north direction they might want to say
    ¬ go north
      or if they know what's through the door they might want to say
    ¬ go to kitchen

Since this type of grammar is movement related, it's been separated from
normal actions.

- `to` refers to a specific place. If `to` refers a world item, like a window
  sill or fireplace, we can assume the player wants to `inspect` the item.

  If `to` refers to a place we just go to the place.

  If `to ` is a direction, we just `go <direction>` Every pathway defines it's
  position in terms of a cardinal direction, so we can just go through the
  pathway

- `through` refers to following a pathway. We check if there are any pathways
the player can go through, and if there are just go there.

## Entities

#### Entities are defined as the objects a player can interact with.

### Types of entities include:

- Items:
  - Weapons
  - Consumables
  - World Items
    - Pathways
    - Walls
    - Traps
    - etc
  - Misc Items
    - Books
    - Tapes
    - etc.
- Non Player Characters
  - Monsters
  - People
- Player

## Places

#### Places are defined as areas the player exists in.

When the game is loaded, the places all assume a default state.

As the player enters the rooms and interacts, these states change. If a player
completes a task or puzzle in one place, that might cause something to change
in some other place.

Places are all linked in the game, but data wise they're separated. They define
a list of objects that are in the area as well as a description of the area.

Pathways define how the player moves between areas, and they're just a special
type of entity.

If the player wants to look in a direction, the `look` action will check
pathways too.
