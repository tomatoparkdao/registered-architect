# Occupancy Classification -- Edge Cases and Special Provisions

## Overview

Correct occupancy classification is the most consequential code decision in a
building project. Misclassification cascades through every subsequent analysis:
construction type, height and area, egress, fire protection, and accessibility.
This reference addresses the classification scenarios that are most frequently
mishandled in practice.

---

## Section 1: Mixed Occupancy

When a building contains two or more occupancy groups, the architect must choose
between two approaches per IBC Section 508.

### Nonseparated Occupancies (IBC 508.3)

All occupancies are treated as a single building without physical fire separation
between uses.

**Rules:**
- The most restrictive height and area requirements of any occupancy present
  govern the entire building
- The most restrictive construction type requirements govern
- The most restrictive fire protection system requirements apply throughout

**When to use:**
- Small accessory uses that do not warrant fire-rated separation
- Uses that are functionally intermingled (e.g., office and assembly in a
  conference center)
- When the penalty of the most restrictive occupancy is acceptable

**Example:** A 2-story building with Group B offices (upper floor) and Group M
retail (ground floor), nonseparated. Both are governed by the more restrictive
of B or M for height, area, and construction type. For most construction types,
B and M have similar allowances, so nonseparated is efficient.

### Separated Occupancies (IBC 508.4)

Occupancies are physically separated by fire barriers with fire resistance
ratings per IBC Table 508.4.

**Rules:**
- Each occupancy is evaluated independently for height and area
- Fire barriers between occupancies must extend from floor slab to floor slab
  (or roof) above
- Fire barriers must meet IBC 707 requirements
- Each occupancy must comply with its own fire protection requirements
- The construction type of the building must be permitted for ALL occupancies
  present

**Separation ratings (IBC Table 508.4):**

| Occupancy Groups | Sprinklered | Nonsprinklered |
|---------------------------------------------|-------------|----------------|
| A + B | 1 hr | 2 hr |
| A + R | 1 hr | 2 hr |
| B + M | 1 hr | 2 hr |
| B + R | 1 hr | 2 hr |
| Any + H-2 | 2 hr | 3 hr |
| Any + H-3, H-4, H-5 | 1 hr | 2 hr |
| Any + I-2 | 2 hr | NP |
| Any + H-1 | NP | NP |
| F-1, S-1 + R | 1 hr | 2 hr |

(NP = Not Permitted in same building)

**When to use:**
- Mixed-use buildings where different uses have significantly different code
  requirements (e.g., residential over retail, assembly within office)
- When separating occupancies allows more favorable area calculations for
  each use
- When one occupancy requires sprinklers but another does not (separation
  may avoid sprinklering the entire building in limited cases)

### Mixed Occupancy Height Interaction

Critical rule for separated occupancies: the construction type must be
permitted for ALL occupancies at the proposed height. If the building is
6 stories, every occupancy must be permitted at 6 stories under the chosen
construction type, even if that occupancy only occupies 1 story.

**Example:** A 6-story building with R-2 on floors 2-6 and A-2 on floor 1.
- Type IB: R-2 allowed 12 stories, A-2 allowed 12 stories. Both work.
- Type IIIA: R-2 allowed 5 stories (sprinklered), A-2 allowed 4 stories
  (sprinklered). At 6 stories, neither works. Need Type IB or higher.

---

## Section 2: Accessory Occupancies

IBC Section 508.2 provides an exception for accessory uses.

### Definition

An accessory occupancy is a use that:
- Is subordinate to the main occupancy
- Does not exceed 10% of the floor area of the story it is on
- Does not exceed the tabular area limits per Table 506.2 for the
  accessory occupancy

### Treatment

- No fire-rated separation required between accessory and main occupancy
- The accessory use is classified as part of the main occupancy for
  height/area purposes
- The accessory space must still comply with its own occupancy requirements
  for egress, fire protection features, and other applicable code sections

### Common Accessory Use Examples

| Main Occupancy | Accessory Use | Notes |
|----------------|------------------------------|--------------------------------|
| B (Office) | A-3 (conference room) | Conference rooms < 10% of floor |
| M (Retail) | S-1 (stockroom) | Stockroom < 10% of floor |
| R-2 (Apartment) | A-3 (community room) | Fitness/party room < 10% |
| B (Office) | M (ground floor cafe) | Cafe serving occupants < 10% |
| E (School) | A-1 (auditorium) | Auditorium may exceed 10% -- then requires separation |

### Accessory vs Incidental

Accessory occupancies are not the same as incidental uses (IBC Table 509).
Accessory relates to occupancy classification. Incidental relates to specific
hazardous functions within a building that require either fire-rated separation
or sprinkler protection.

---

## Section 3: Incidental Uses

IBC Section 509 and Table 509 identify specific uses within buildings that
pose an elevated risk and require either separation or suppression.

### Incidental Use Table (IBC Table 509)

| Incidental Use | Separation or Protection |
|-------------------------------------------|-------------------------------|
| Furnace room (fuel-fired, > 400 MBH) | 1 hr or sprinklers + barriers |
| Boiler rooms (> 15 psi, > 10 HP) | 1 hr or sprinklers + barriers |
| Refrigerant machinery rooms | 1 hr or sprinklers + barriers |
| Hydrogen fuel gas rooms | 1 hr + sprinklers |
| Incinerator rooms | 2 hr + sprinklers |
| Paint shops (not H) | 2 hr or 1 hr + sprinklers |
| Laboratories and vocational shops (not H) | 1 hr or sprinklers + barriers |
| Laundry rooms > 9.3 m² (100 ft²) | 1 hr or sprinklers + barriers |
| Waste/linen collection > 9.3 m² | 1 hr or sprinklers + barriers |
| Storage rooms > 9.3 m² (100 ft²) | 1 hr or sprinklers + barriers |
| Stationary lead-acid battery systems | 1 hr + sprinklers per IFC 608 |

### Key Principle

Incidental uses are NOT reclassified as a different occupancy. They remain
part of the main occupancy but require additional protection. A boiler room
in an office building is still Group B -- it is not reclassified as F or H.

When the table offers "separation OR sprinklers + barriers," the architect
may choose either path. Sprinklers and smoke-tight barriers are often more
economical than full fire-rated enclosures, especially in sprinklered buildings.

---

## Section 4: Atriums (IBC Section 404)

### Classification Challenges

An atrium is a floor opening connecting two or more stories that is NOT:
- An enclosed stairway, ramp, or elevator shaft
- A mezzanine complying with Section 505

### Code Requirements

1. **Sprinklers:** NFPA 13 sprinklers required throughout the building
2. **Fire barrier separation:** Atrium must be separated from adjacent spaces
   by 1-hour fire barriers OR a glass wall + sprinkler curtain system (IBC
   404.6). The glass wall option requires closely spaced sprinklers on the
   atrium side, wetting the glass surface.
3. **Smoke control:** Required per Section 909. Active smoke control system
   must maintain tenable conditions during evacuation. Typically mechanical
   exhaust with natural or mechanical makeup air.
4. **Travel distance:** Through the atrium to an exit must not exceed limits.
   Occupants within the atrium are counted separately.
5. **Standby power:** Smoke control system must have standby power.

### Occupancy Interaction

The atrium itself is not a separate occupancy -- it takes the occupancy of
the uses it serves. But uses opening onto the atrium may need to be separated
from the atrium volume depending on the fire strategy.

### Common Design Solutions

- Glass walls with sprinkler curtain (most common in commercial atriums)
- Smoke reservoirs at atrium top (min 3 m / 10 ft depth)
- Balcony spill plume calculations per NFPA 92
- Mechanical exhaust sizing: typically 4-8 air changes per hour depending
  on atrium volume and fire size

---

## Section 5: High-Rise Buildings (IBC Section 403)

### Definition

A high-rise building has an occupied floor located more than 23 m (75 ft)
above the lowest level of fire department vehicle access.

### Classification Impact

High-rise status triggers additional requirements regardless of occupancy:

1. **Construction type:** Type IB minimum (2-hour structural frame). Exception:
   R-2 may use Type IIA with additional fire protection per 403.2.1.1
2. **Sprinklers:** NFPA 13 throughout, secondary water supply
3. **Fire alarm:** Voice/alarm communication per NFPA 72, fire command center
4. **Standpipe:** Class I standpipe in all exit stairways
5. **Elevators:** At least one fire service access elevator (ASME A17.1)
   serving all floors; two required in buildings > 36.6 m (120 ft)
6. **Emergency power:** Generator for fire alarm, elevators, egress lighting,
   fire pump; 2-hour fuel supply minimum
7. **Stairway communication:** Two-way communication at every 5th floor
8. **Luminous egress markings:** Photoluminescent or self-luminous markings
   on stair treads, landings, handrails, perimeters, and exit signs

### Stairway Pressurization

Stairways in high-rise buildings must have smokeproof enclosures (IBC 403.5.4):
- Option 1: Stair pressurization system (most common) -- maintaining positive
  pressure of 12.5 Pa (0.05 in w.g.) minimum with all doors closed, max
  87 Pa (0.35 in w.g.) to allow door opening
- Option 2: Natural ventilation (open exterior stair) -- rare in high-rise
- Option 3: Vestibule with mechanical ventilation

---

## Section 6: Underground Buildings (IBC Section 405)

### Definition

A building with an occupied floor level more than 9.1 m (30 ft) below the
lowest level of exit discharge.

### Additional Requirements

1. **Construction type:** Type I required
2. **Sprinklers:** NFPA 13 throughout
3. **Smoke control:** Mechanical smoke exhaust or compartment pressurization
4. **Compartmentation:** Max 139 m² (1,500 ft²) smoke compartments, or smoke
   control per Section 909
5. **Fire alarm:** Voice/alarm communication, fire command center
6. **Standpipe:** Required in exit stairways
7. **Elevator:** Fire service access elevator to lowest level

### Design Implications

Underground buildings often occur in urban contexts: transit stations, below-grade
retail, parking structures, cultural facilities (museums, performance halls).
The combination of limited egress paths, no natural ventilation, and potential
for smoke logging makes these among the most challenging fire safety designs.

---

## Section 7: Covered and Open Mall Buildings (IBC Section 402)

### Covered Mall Building

A single building enclosing multiple tenants and anchor stores with a common
pedestrian mall.

**Key provisions:**
- Mall is treated as a pedestrian way (not contributing to exit access travel
  distance once reached) if minimum 6.1 m (20 ft) wide
- Tenant spaces must have exits directly to mall or to exterior
- Max travel distance within tenant: 61 m (200 ft) to mall entrance (not to
  building exit)
- Sprinklers required throughout per NFPA 13
- Emergency voice/alarm communication system required
- Standby power for smoke control in mall
- Anchor stores (> 2 per mall) may be treated as separate buildings if
  separated by fire walls

**Occupancy:**
- Mall tenants: typically M (retail), A-2 (food court), B (offices)
- Mall building does not require occupancy separation between the mall
  walkway and tenant spaces less than 280 m² (3,000 ft²) per Section 402.4.2.1
- Large tenants (> 280 m²) require fire-rated separation or sprinkler
  protection per tenant type

### Open Mall Building

Similar to covered mall but with open-air pedestrian way.
- Less stringent smoke control requirements
- Still requires sprinklers in tenant spaces

---

## Section 8: Special Occupancy Edge Cases

### Assembly Threshold

A space becomes Group A when it is used by 50 or more persons for assembly
purposes. A conference room for 49 in an office building is Group B. The
same room for 50 becomes A-3 (accessory A-3 if < 10% of floor, separated
A-3 if larger).

### Day Care Reclassification

Day care for > 5 persons of any age is Group I-4. But if the facility is
on the level of exit discharge with direct exterior exit access and serves
children over 2.5 years, it may be classified as Group E instead. This
distinction dramatically affects construction type and egress requirements.

### Residential Care Facilities

The boundary between R-4 (5-16 persons, residential care) and I-1 (> 16 persons)
is frequently misunderstood. R-4 Condition 1 (ambulatory occupants) may use
R-3 (IRC) construction with sprinklers. R-4 Condition 2 (non-ambulatory)
must comply with I-1 requirements, effectively making it institutional
construction despite the small size.

### Laboratory Classification

Laboratories default to Group B unless materials present exceed IFC exempt
amounts, triggering Group H. University research buildings frequently contain
both B laboratories and H-2/H-3/H-4 laboratories. Each lab must be individually
classified based on its chemical inventory, and H-classified labs require
compliant separation from B spaces.

### Ambulatory Care Facilities

Outpatient surgery centers and clinics where 4+ patients are rendered incapable
of self-preservation (general anesthesia, conscious sedation) are classified
as Group B but must comply with Section 422 additional requirements:
- Sprinklers per NFPA 13
- Smoke compartments if > 4 such patients per smoke compartment on floors
  other than level of exit discharge
- Smoke detection in waiting and recovery areas

This is technically Group B with I-2-like provisions -- one of the most
confusing classification overlaps in the IBC.

### Parking Garages

- Open parking garages (Section 406.5): at least 20% open on each tier,
  uniformly distributed. Qualify for significant area and height increases.
  May be Type IIA, IIIA, or IV at reduced fire resistance.
- Enclosed parking garages: S-2 occupancy with full table compliance
- Mechanical access parking (robotic parking): S-2, no occupants in
  parking area, so no egress from parking levels needed

### Food Service within Other Occupancies

A restaurant in an office building:
- < 750 ft² and serving the building's occupants: accessory use of Group B
- >= 750 ft² or open to public: A-2 requiring separation from B

A restaurant in a hotel:
- Serving hotel guests and public: A-2 separated from R-1
- Room service kitchen only: accessory use of R-1

---

## Section 9: Occupancy Load Calculation -- Special Cases

### Multiple Functions in One Space

When a space has multiple functions, use the function that produces the
highest occupant load. A gymnasium that is also used for assembly with
chairs (0.65 m²/person) has a higher load than when used for exercise
(4.6 m²/person). Design for the worst case.

### Fixed Seating vs Calculated Load

When fixed seating is installed, count the actual seats. When seating is
not fixed, calculate by area. If the calculated load is higher, use the
calculated load. If fixed seating provides more seats than the calculated
load, use the fixed seat count.

### Outdoor Areas

Outdoor assembly areas (patios, beer gardens, roof decks) are counted in
the occupant load. Outdoor dining at a restaurant adds to the A-2 load.
Egress from outdoor areas must comply independently.

### Mezzanines

A mezzanine occupant load is added to the floor below for egress purposes
unless the mezzanine has independent egress directly to an exit.

---

## Decision Flowchart -- Occupancy Classification

1. Identify the primary use of the space
2. If sleeping accommodations: R (transient? R-1; permanent? R-2/R-3/R-4)
   or I (restrained? I-3; incapable of self-preservation? I-1/I-2)
3. If assembly >= 50 persons: A (which A subgroup?)
4. If mercantile (retail sales): M
5. If educational K-12: E
6. If factory/industrial: F-1 or F-2 based on hazard
7. If office/professional: B
8. If storage: S-1 or S-2 based on hazard
9. If hazardous materials exceed exempt quantities: H-1 through H-5
10. If none of the above: U
11. Check for mixed occupancy -- separated or nonseparated?
12. Check for accessory uses < 10%
13. Check for incidental uses requiring Table 509 protection
14. Verify against special provisions: high-rise (403), atrium (404),
    underground (405), mall (402)

---

*All references are to the IBC 2021 edition unless otherwise noted. Verify
against the locally adopted code edition and amendments. Building officials
have final interpretive authority.*
