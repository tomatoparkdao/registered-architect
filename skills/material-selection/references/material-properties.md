# Material Properties — Deep Reference

Comprehensive material property tables for architectural specification and design. All values are typical ranges for design reference; verify specific products against manufacturer datasheets and test certificates.

---

## 1. Concrete

### 1.1 Structural Concrete Grades

| Grade (EN) | Cylinder/Cube fck (MPa) | Elastic Modulus Ecm (GPa) | Density (kg/m³) | Typical Use |
|---|---|---|---|---|
| C12/15 | 12/15 | 27 | 2,350 | Blinding, unreinforced foundations |
| C16/20 | 16/20 | 29 | 2,350 | Mass fill, strip foundations |
| C20/25 | 20/25 | 30 | 2,400 | Pad foundations, ground slabs |
| C25/30 | 25/30 | 31 | 2,400 | Residential slabs and beams |
| C28/35 | 28/35 | 32 | 2,400 | General structural RC frames |
| C30/37 | 30/37 | 33 | 2,400 | Columns, beams, slabs (standard commercial) |
| C32/40 | 32/40 | 33 | 2,400 | Water-retaining structures |
| C35/45 | 35/45 | 34 | 2,400 | Prestressed elements, high-rise columns |
| C40/50 | 40/50 | 35 | 2,400 | High-rise columns, long-span PT slabs |
| C50/60 | 50/60 | 37 | 2,450 | Prestressed beams, bridge elements |
| C60/75 | 60/75 | 39 | 2,450 | High-performance precast |
| C90/105 | 90/105 | 44 | 2,500 | UHPC columns, special applications |

### 1.2 Concrete Thermal and Acoustic Properties

| Property | Normal Weight | Lightweight (1400 kg/m³) | AAC (600 kg/m³) |
|---|---|---|---|
| Thermal conductivity λ (W/mK) | 1.0-1.8 | 0.5-0.8 | 0.12-0.18 |
| Specific heat c (J/kgK) | 840-1,000 | 840-1,000 | 1,000 |
| Thermal admittance Y (W/m²K) | 5.0-6.0 | 3.0-4.0 | 1.0-1.5 |
| Decrement factor (200 mm wall) | 0.35 | 0.50 | 0.65 |
| Sound reduction Rw (200 mm) | 52-55 dB | 45-48 dB | 36-40 dB |
| NRC (painted surface) | 0.02-0.05 | 0.05-0.10 | 0.10-0.15 |

### 1.3 Concrete Fire Performance

| Cover to Reinforcement (mm) | Beam REI | Column REI | Slab REI | Wall REI |
|---|---|---|---|---|
| 20 | 30 | 30 | 30 | 30 |
| 25 | 60 | 60 | 60 | 60 |
| 35 | 90 | 90 | 90 | 90 |
| 40 | 120 | 120 | 120 | 120 |
| 55 | 240 | 240 | 180 | 240 |

Minimum section dimensions also apply (e.g., column 250 mm for REI 120, 350 mm for REI 240).

### 1.4 Concrete Embodied Carbon by Mix Design

| Mix Description | Cement Content (kg/m³) | GGBS/PFA (%) | Embodied Carbon A1-A3 (kgCO2e/m³) |
|---|---|---|---|
| C30/37 OPC only | 340 | 0% | 235 |
| C30/37 with 30% PFA | 240 OPC + 100 PFA | 30% | 175 |
| C30/37 with 50% GGBS | 170 OPC + 170 GGBS | 50% | 145 |
| C30/37 with 70% GGBS | 100 OPC + 240 GGBS | 70% | 100 |
| C40/50 OPC only | 400 | 0% | 280 |
| C40/50 with 50% GGBS | 200 OPC + 200 GGBS | 50% | 170 |
| UHPC (120+ MPa) | 800+ | Variable | 350-500 |
| GRC panel (15 mm) | N/A | N/A | 12-18 kgCO2e/m² |

---

## 2. Steel

### 2.1 Structural Steel Properties

| Property | Carbon Steel (S355) | Stainless 304 | Stainless 316 | Weathering (Corten) |
|---|---|---|---|---|
| Density (kg/m³) | 7,850 | 7,900 | 8,000 | 7,850 |
| Yield strength (MPa) | 355 | 210 | 220 | 345 |
| Tensile strength (MPa) | 470-630 | 520-720 | 530-680 | 480-620 |
| Elastic modulus (GPa) | 210 | 193 | 193 | 210 |
| Thermal conductivity (W/mK) | 50 | 16 | 16 | 50 |
| Thermal expansion (×10⁻⁶/°C) | 12 | 17.3 | 16.0 | 12 |
| Specific heat (J/kgK) | 440 | 500 | 500 | 440 |
| Embodied carbon (kgCO2e/kg) | 1.55 (BOF) | 4.5-6.2 | 5.0-6.8 | 1.55 |
| Recycled content (typical) | 30-60% | 60-85% | 60-85% | 30-60% |
| Recyclability | ~98% | ~95% | ~95% | ~98% |
| Euroclass fire | A1 | A1 | A1 | A1 |
| Critical temp (50% strength loss) | 550°C | 700°C | 700°C | 550°C |
| Cost (relative to S355) | 1.0 | 4-6× | 5-8× | 1.1-1.3× |

### 2.2 Steel Section Properties (Common UK/EU Sections)

| Section | Depth (mm) | Mass (kg/m) | Moment Capacity Mc (kNm) | Application |
|---|---|---|---|---|
| 152×152 UC | 152 | 23-37 | 42-75 | Light columns, posts |
| 203×203 UC | 203 | 46-86 | 120-250 | Medium columns |
| 254×254 UC | 254 | 73-167 | 250-650 | Heavy columns, transfer |
| 305×165 UB | 305 | 40-54 | 165-240 | Office floor beams (6-8 m) |
| 406×178 UB | 406 | 54-74 | 340-490 | Standard floor beams (8-10 m) |
| 457×191 UB | 457 | 67-98 | 490-760 | Long-span beams (10-12 m) |
| 533×210 UB | 533 | 82-122 | 640-1,060 | Long-span (12-15 m) |
| 610×229 UB | 610 | 101-140 | 870-1,280 | Transfer beams, long-span |

---

## 3. Timber

### 3.1 Softwood Structural Properties

| Species | Density at 12% MC (kg/m³) | Bending fm,k (MPa) | Tension ft,0,k (MPa) | Compression fc,0,k (MPa) | Shear fv,k (MPa) | E0,mean (GPa) | Strength Class |
|---|---|---|---|---|---|---|---|
| European Spruce | 380-450 | 16-24 | 10-14 | 17-21 | 2.5-4.0 | 8-11 | C16-C24 |
| Scots Pine | 440-530 | 18-27 | 11-16 | 18-22 | 3.0-4.0 | 9-12 | C18-C27 |
| Douglas Fir | 480-560 | 24-30 | 14-18 | 21-26 | 3.5-4.5 | 11-13 | C24-C30 |
| Larch | 470-560 | 24-27 | 14-16 | 21-24 | 3.0-4.0 | 10-12 | C24-C27 |
| Sitka Spruce | 380-440 | 16-20 | 10-12 | 17-19 | 2.5-3.0 | 8-10 | C16-C20 |
| Western Red Cedar | 330-380 | 14-16 | 8-10 | 14-17 | 2.0-2.5 | 7-8 | C14-C16 |

### 3.2 Hardwood Structural Properties

| Species | Density (kg/m³) | Bending fm,k (MPa) | Compression fc,0,k (MPa) | E0,mean (GPa) | Durability Class | Janka Hardness (N) |
|---|---|---|---|---|---|---|
| European Oak | 600-720 | 38-50 | 26-34 | 10-12 | 2 | 5,600 |
| Iroko | 550-680 | 35-45 | 22-30 | 9-11 | 1-2 | 5,100 |
| Teak | 580-680 | 40-50 | 28-35 | 10-13 | 1 | 4,700 |
| American White Oak | 600-720 | 42-52 | 28-36 | 11-13 | 2 | 6,000 |
| European Beech | 660-740 | 45-55 | 30-38 | 12-14 | 5 | 6,400 |
| American Black Walnut | 560-640 | 38-48 | 24-32 | 10-12 | 3 | 4,500 |
| Sapele | 560-650 | 36-46 | 24-30 | 10-12 | 2-3 | 5,200 |
| Accoya (modified) | 510 | 33-40 | 22-28 | 8-10 | 1 | 4,000 |

### 3.3 Engineered Timber Properties

| Product | Density (kg/m³) | Bending (MPa) | Compression (MPa) | E (GPa) | Charring Rate (mm/min) | Embodied Carbon (kgCO2e/m³) |
|---|---|---|---|---|---|---|
| Glulam GL24h | 420-460 | 24 | 24 | 11.6 | 0.70 | -450 to -600 |
| Glulam GL28h | 440-480 | 28 | 26.5 | 12.6 | 0.70 | -450 to -600 |
| Glulam GL32h | 460-500 | 32 | 29 | 13.7 | 0.70 | -450 to -600 |
| CLT (5-ply, 160 mm) | 420-500 | 24 (major) / 12 (minor) | 21 / 9 | 12 / 4 | 0.65 | -500 to -700 |
| LVL (Kerto-S) | 480-520 | 44 | 35 | 13.8 | 0.65 | -400 to -550 |
| Plywood (structural birch) | 600-680 | 40-50 | 30-40 | 10-12 | 1.0 (thin layers) | -300 to -400 |

### 3.4 Timber Thermal and Acoustic Properties

| Property | Softwood | Hardwood | CLT (160 mm) | Plywood (18 mm) |
|---|---|---|---|---|
| Thermal conductivity λ (W/mK) | 0.13 | 0.18 | 0.13 | 0.15 |
| Specific heat c (J/kgK) | 1,600 | 1,600 | 1,600 | 1,600 |
| Thermal admittance Y (W/m²K) | 3.5 | 4.5 | 3.5 | N/A |
| Rw (160 mm CLT bare) | N/A | N/A | 33-36 dB | N/A |
| Rw (CLT + resilient + plasterboard) | N/A | N/A | 52-58 dB | N/A |
| NRC (unfinished timber) | 0.05-0.10 | 0.05-0.08 | 0.05-0.10 | 0.10-0.15 |
| NRC (timber with gaps/slats) | 0.30-0.60 | 0.25-0.50 | N/A | N/A |

---

## 4. Masonry

### 4.1 Brick Properties

| Brick Type | Density (kg/m³) | Compressive (MPa) | Water Absorption (%) | λ (W/mK) | Embodied Carbon (kgCO2e/kg) | Euroclass |
|---|---|---|---|---|---|---|
| Common clay (wirecut) | 1,700-1,900 | 15-40 | 8-16 | 0.60-0.80 | 0.22 | A1 |
| Facing clay (stock) | 1,800-2,100 | 20-80 | 5-12 | 0.70-0.96 | 0.24 | A1 |
| Engineering Class A | 2,100-2,400 | ≥ 70 | < 4.5 | 1.00-1.20 | 0.28 | A1 |
| Engineering Class B | 2,000-2,200 | ≥ 50 | < 7.0 | 0.90-1.10 | 0.26 | A1 |
| Calcium silicate | 1,800-2,100 | 15-50 | 8-16 | 0.70-1.10 | 0.16 | A1 |
| Concrete brick | 1,800-2,200 | 7-40 | 5-12 | 0.70-1.20 | 0.09 | A1 |
| Handmade clay | 1,700-1,900 | 10-30 | 10-20 | 0.55-0.75 | 0.24 | A1 |
| Reclaimed (Victorian) | 1,700-2,100 | 10-50 | 8-18 | 0.60-0.90 | ~0 (reuse) | A1 |

### 4.2 Block Properties

| Block Type | Density (kg/m³) | Compressive (MPa) | λ (W/mK) | Rw per 100 mm (dB) | Embodied Carbon (kgCO2e/kg) |
|---|---|---|---|---|---|
| Dense concrete | 2,000-2,200 | 7.3-22.5 | 1.0-1.5 | 40-43 | 0.10 |
| Medium dense | 1,400-1,700 | 3.5-10.5 | 0.50-0.80 | 36-39 | 0.09 |
| Lightweight aggregate | 600-1,400 | 2.8-7.3 | 0.15-0.50 | 32-38 | 0.08 |
| AAC (Aircrete) 600 | 400-600 | 2.5-4.0 | 0.10-0.15 | 30-33 | 0.30 (per block) |
| AAC (Aircrete) 800 | 600-800 | 3.5-7.0 | 0.14-0.20 | 33-37 | 0.34 (per block) |
| Hollow block (215 mm) | 1,400-1,800 | 3.5-7.3 | 0.30-0.60 | 38-42 | 0.08 |

### 4.3 Natural Stone Properties

| Stone | Density (kg/m³) | Compressive (MPa) | Flexural (MPa) | λ (W/mK) | Absorption (%) | Embodied Carbon (kgCO2e/kg) | Durability |
|---|---|---|---|---|---|---|---|
| Portland limestone | 2,100-2,300 | 20-50 | 3-8 | 1.3 | 5-12 | 0.09 | Good |
| Bath limestone | 1,900-2,200 | 15-35 | 2-5 | 1.1 | 8-18 | 0.09 | Moderate |
| Yorkstone (sandstone) | 2,200-2,400 | 30-70 | 5-12 | 1.5 | 3-10 | 0.06 | Good |
| Red sandstone | 2,000-2,300 | 20-50 | 3-8 | 1.3 | 5-15 | 0.06 | Variable |
| Granite (grey) | 2,600-2,700 | 130-250 | 10-20 | 2.8-3.5 | 0.3-1.5 | 0.70 | Excellent |
| Granite (black/gabbro) | 2,800-3,000 | 180-300 | 12-25 | 3.0-3.5 | 0.2-1.0 | 0.70 | Excellent |
| Carrara marble | 2,600-2,800 | 50-100 | 8-15 | 2.5 | 0.3-1.5 | 0.12 | Good (interior) |
| Slate (Welsh) | 2,700-2,800 | 100-180 | 30-50 | 2.0 | 0.1-0.5 | 0.03 | Excellent |
| Travertine | 2,200-2,500 | 30-70 | 5-10 | 1.3 | 2-8 | 0.12 | Moderate |
| Basalt | 2,800-3,000 | 150-300 | 15-30 | 1.6-2.0 | 0.2-1.0 | 0.60 | Excellent |

---

## 5. Glass Properties

| Glass Type | Thickness (mm) | Weight (kg/m²) | VLT (%) | SHGC | U-value (W/m²K) | Rw (dB) | Embodied Carbon (kgCO2e/kg) |
|---|---|---|---|---|---|---|---|
| Clear float (single) | 6 | 15 | 87 | 0.86 | 5.8 | 31 | 0.86 |
| Clear float (single) | 10 | 25 | 84 | 0.83 | 5.7 | 33 | 0.86 |
| Tinted (grey body) | 6 | 15 | 45-55 | 0.55-0.65 | 5.8 | 31 | 0.90 |
| Toughened | 10 | 25 | 84 | 0.83 | 5.7 | 33 | 1.00 |
| Laminated (6.4 mm = 3+3) | 6.4 | 16 | 85 | 0.84 | 5.7 | 34 | 0.95 |
| Laminated (10.8 = 5+5) | 10.8 | 27 | 83 | 0.82 | 5.6 | 37 | 0.95 |
| IGU clear (4-16air-4) | 24 | 20 | 79 | 0.70 | 2.8 | 29 | 0.86 |
| IGU low-e (4-16arg-4) | 24 | 20 | 70 | 0.37 | 1.1-1.3 | 30 | 0.90 |
| IGU solar control (6-16arg-6) | 28 | 30 | 42 | 0.25 | 1.1-1.4 | 32 | 0.95 |
| Triple low-e (4-12arg-4-12arg-4) | 40 | 30 | 60 | 0.30 | 0.5-0.7 | 33 | 0.95 |
| Triple low-e krypton | 36 | 30 | 62 | 0.28 | 0.5 | 34 | 1.00 |
| Electrochromic (tinted state) | 24-30 | 22-28 | 2-60 | 0.09-0.41 | 1.3-1.7 | 30-33 | 2.00-3.00 |
| Fire-rated (intumescent) | 15-33 | 35-85 | 75-82 | 0.65-0.75 | 3.0-4.5 | 38-44 | 2.50 |
| Channel glass (Profilit) | 6-7 (×2) | 10-20 | 25-50 | 0.30-0.45 | 1.4-3.0 | 33-40 | 0.90 |

---

## 6. Aluminum Properties

| Property | 6063-T6 (extrusion) | 5005-H34 (sheet) | 3003-H14 (sheet) |
|---|---|---|---|
| Density (kg/m³) | 2,700 | 2,700 | 2,730 |
| Yield strength (MPa) | 170 | 140 | 115 |
| Tensile strength (MPa) | 205 | 160 | 150 |
| Elastic modulus (GPa) | 69 | 69 | 69 |
| Thermal conductivity (W/mK) | 200 | 200 | 193 |
| Thermal expansion (×10⁻⁶/°C) | 23.4 | 23.8 | 23.2 |
| Specific heat (J/kgK) | 900 | 900 | 900 |
| Embodied carbon primary (kgCO2e/kg) | 8.20 | 8.20 | 8.20 |
| Embodied carbon recycled (kgCO2e/kg) | 0.50 | 0.50 | 0.50 |
| Euroclass | A1 | A1 | A1 |
| Melting point (°C) | 600-655 | 600-655 | 640-655 |

---

## 7. Zinc and Copper Properties

| Property | Zinc (titanium zinc) | Copper (C11000) | Bronze (CuSn8) |
|---|---|---|---|
| Density (kg/m³) | 7,130 | 8,900 | 8,800 |
| Yield strength (MPa) | 100-150 | 70-220 | 150-400 |
| Tensile strength (MPa) | 150-250 | 220-350 | 350-600 |
| Elastic modulus (GPa) | 75 | 117 | 103 |
| Thermal conductivity (W/mK) | 110 | 385 | 62 |
| Thermal expansion (×10⁻⁶/°C) | 22 | 16.5 | 17 |
| Creep temperature (°C) | > 20 | N/A | N/A |
| Embodied carbon (kgCO2e/kg) | 3.10 | 2.70 | 3.50 |
| Typical cladding thickness (mm) | 0.7-1.0 | 0.6-0.7 | 3-6 |
| Weight as cladding (kg/m²) | 5-7 | 5.5-6.5 | 25-50 |
| Patina color (mature) | Blue-grey | Green verdigris | Dark brown-black |
| Patina time (years) | 5-10 | 7-20 | 3-8 |
| Expected life (years) | 80-100 | 100-200 | 100-200 |
| Recyclability | ~95% | ~99% | ~95% |

---

## 8. Insulation Materials

| Material | Density (kg/m³) | λ (W/mK) | Specific Heat (J/kgK) | Fire Class | Embodied Carbon (kgCO2e/kg) | Moisture Resistance | Cost ($/m² at R=3.5) |
|---|---|---|---|---|---|---|---|
| Mineral wool (glass) | 12-80 | 0.032-0.040 | 840 | A1 | 1.20 | Hydrophobic-treated | $8-15 |
| Mineral wool (stone/rock) | 30-200 | 0.034-0.040 | 840 | A1 | 1.05 | Hydrophobic-treated | $10-18 |
| EPS (expanded polystyrene) | 15-35 | 0.031-0.038 | 1,450 | E (B with FR) | 2.50 | Closed-cell; good | $6-12 |
| XPS (extruded polystyrene) | 25-45 | 0.029-0.036 | 1,450 | E (B with FR) | 4.40 | Closed-cell; excellent | $12-22 |
| PIR (polyisocyanurate) | 30-45 | 0.020-0.025 | 1,400 | B-C | 4.20 | Foil-faced; excellent | $14-25 |
| PUR (polyurethane foam) | 30-80 | 0.022-0.028 | 1,400 | B-C | 4.00 | Good | $12-22 |
| Phenolic foam | 35-50 | 0.018-0.022 | 1,400 | B-C | 3.50 | Foil-faced; good | $18-30 |
| Wood fibre board | 110-240 | 0.038-0.050 | 2,100 | E | -1.10 | Vapour-open; fair | $15-28 |
| Cellulose (blown) | 30-65 | 0.035-0.040 | 2,000 | B-C | -1.30 | Vapour-open; fair | $5-10 |
| Sheep's wool | 15-25 | 0.035-0.040 | 1,800 | E (B with FR) | 0.20 | Vapour-open; good | $18-30 |
| Hemp fibre | 30-50 | 0.038-0.042 | 2,000 | E | -1.00 | Vapour-open; fair | $15-25 |
| Cork | 100-140 | 0.037-0.042 | 1,500 | E | -1.20 | Good | $20-35 |
| Aerogel blanket | 120-180 | 0.013-0.016 | 1,000 | A2-B | 5.00 | Hydrophobic | $80-150 |
| Vacuum insulation (VIP) | 160-200 | 0.004-0.008 | 800 | A2 | 6.50 | Sealed panel; fragile | $100-200 |

### 8.1 Insulation Thickness for Target U-value

**Insulation thickness (mm) required for U = 0.15 W/m²K wall (typical Passive House):**

| Material | λ (W/mK) | Required Thickness (mm) |
|---|---|---|
| PIR/PUR | 0.022 | 140 |
| Phenolic | 0.020 | 130 |
| XPS | 0.033 | 210 |
| Mineral wool | 0.035 | 225 |
| Wood fibre | 0.040 | 255 |
| Aerogel | 0.015 | 95 |

Note: above are insulation-only thicknesses; actual construction will include structural layers that contribute to overall U-value.

---

## 9. Composites and Specialty Materials

| Material | Density (kg/m³) | Tensile (MPa) | Compressive (MPa) | λ (W/mK) | Fire Class | Embodied Carbon (kgCO2e/kg) | Cost Range ($/m²) |
|---|---|---|---|---|---|---|---|
| GRP/GFRP (glass fibre) | 1,500-2,000 | 100-400 | 150-350 | 0.30 | B-C | 8.00 | $40-120 |
| CFRP (carbon fibre) | 1,400-1,600 | 600-1,500 | 400-700 | 5.0-10.0 | B | 25.00 | $100-400 |
| ETFE film (250 µm) | 1,750 | 40 | N/A | 0.24 | B-C | 6.50 | $250-500 (cushion system) |
| Fibre cement board | 1,200-1,800 | 6-15 | 30-50 | 0.30-0.60 | A1-A2 | 0.50-0.80 | $15-40 |
| Terracotta (extruded) | 1,800-2,100 | 5-10 (flexural) | 30-80 | 0.70-1.00 | A1 | 0.45 | $60-200 |
| Porcelain tile (large format) | 2,300-2,400 | 35-50 (flexural) | 200-400 | 1.00-1.30 | A1 | 0.70 | $30-120 |
| Bamboo (laminated) | 600-800 | 150-250 | 50-80 | 0.17 | D | -0.80 | $20-60 |
| Rammed earth | 1,800-2,200 | 0.5-1.5 | 1.5-4.0 | 0.50-1.00 | A1 | 0.005-0.02 | $80-200 (wall) |
| Hempcrete | 250-400 | 0.05-0.2 | 0.2-1.0 | 0.06-0.09 | B | -0.40 | $60-150 (wall) |
| Compressed earth block | 1,600-2,000 | 0.5-1.0 | 2.0-10.0 | 0.60-0.80 | A1 | 0.01-0.03 | $20-40 |

---

## 10. Summary Comparison — Embodied Carbon per Structural Function

For equivalent structural capacity (supporting a typical office floor, 5 kN/m² load, 7.5 m span):

| Structural System | Depth (mm) | Weight (kg/m²) | Embodied Carbon (kgCO2e/m²) | Fire Rating Achievable |
|---|---|---|---|---|
| RC flat slab (275 mm) | 275 | 660 | 120-160 | REI 120 (inherent) |
| RC flat slab (low-carbon mix) | 275 | 660 | 75-100 | REI 120 (inherent) |
| PT flat slab (225 mm) | 225 | 540 | 80-120 | REI 120 (inherent) |
| Steel composite (UB + slab) | 400 | 180 (steel) + 300 (slab) | 100-140 | REI 90 (with intumescent) |
| CLT floor (200 mm) | 200 | 100 | -50 to -70 (net negative) | REI 60 (with 30 mm char layer) |
| Glulam beam + CLT | 450 + 160 | 80 + 80 | -60 to -90 (net negative) | REI 60-90 |
| Precast hollow-core + steel | 250 + 200 | 230 + 120 | 90-130 | REI 120 |

**Key Insight:** Mass timber construction achieves net-negative embodied carbon for structure. Combined with low-carbon concrete for foundations and cores, total building embodied carbon can be reduced by 40-60% compared to all-concrete or all-steel alternatives.

---

## 11. Durability and Service Life Reference

| Material/Component | Typical Service Life (years) | Maintenance Interval | Replacement Cycle | Notes |
|---|---|---|---|---|
| Structural concrete frame | 100-150 | Inspection every 10 yr | N/A | Assuming adequate cover |
| Structural steel frame | 100+ | Recoat paint 15-25 yr | N/A | Hot-dip galvanized: 60+ yr maintenance-free |
| Structural timber (protected) | 100+ | Inspection every 5 yr | N/A | Must remain dry; MC < 20% |
| Clay brick facade | 100-150+ | Repoint every 50-80 yr | N/A | Depending on mortar and exposure |
| Natural stone cladding | 100-200+ | Clean every 10-20 yr | N/A | Granite virtually eternal |
| Zinc roofing/cladding | 80-100 | None (self-healing patina) | N/A | Pre-patinated shortens life slightly |
| Copper roofing | 100-200+ | None | N/A | Longest-lived metal cladding |
| Aluminum curtain wall | 40-60 | Seal replacement 20-30 yr | Gaskets 25-35 yr | Frame life > seal life |
| ETFE cushion | 25-50 | Inspect 5 yr; self-cleaning | Replace film 30-40 yr | Frame lasts longer |
| Painted steel cladding | 25-40 | Repaint 10-15 yr | Panel 30-50 yr | PVDF coating lasts longer |
| Single-ply membrane roof | 20-35 | Inspect annually | Replace 25-30 yr | TPO/PVC/EPDM |
| Window units (timber) | 30-50 | Repaint 5-8 yr | Replace 40-60 yr | Accoya extends to 50+ |
| Window units (aluminum) | 40-60 | Clean 5 yr; reseal 20 yr | N/A | Powder-coat life 25-30 yr |
| Sealants (silicone) | 15-25 | N/A | Replace 20-25 yr | Critical waterproofing element |
| External render/stucco | 20-40 | Repaint 8-12 yr | Patch/replace 30 yr | Cracking common in rigid renders |
| Timber cladding (softwood) | 15-30 | Oil/stain 2-5 yr | Replace 20-40 yr | Untreated: 10-15 yr |
| Timber cladding (hardwood) | 40-80 | Oil/stain 3-5 yr (optional) | N/A | Iroko, teak: 60+ yr untreated |

---

## 12. Acoustic Properties — Detailed Reference

### 12.1 Sound Absorption Coefficients (NRC and per-frequency α)

| Material / Assembly | 125 Hz | 250 Hz | 500 Hz | 1000 Hz | 2000 Hz | 4000 Hz | NRC |
|---|---|---|---|---|---|---|---|
| Painted concrete | 0.01 | 0.01 | 0.02 | 0.02 | 0.02 | 0.03 | 0.02 |
| Painted plasterboard on studs | 0.29 | 0.10 | 0.06 | 0.04 | 0.04 | 0.04 | 0.06 |
| Plastered brick | 0.01 | 0.02 | 0.02 | 0.03 | 0.04 | 0.05 | 0.03 |
| Timber floor (on joists) | 0.15 | 0.11 | 0.10 | 0.07 | 0.06 | 0.07 | 0.09 |
| Carpet on concrete | 0.02 | 0.06 | 0.14 | 0.37 | 0.60 | 0.65 | 0.29 |
| Carpet on underlay | 0.08 | 0.24 | 0.57 | 0.69 | 0.71 | 0.73 | 0.55 |
| Glass (single pane, 6 mm) | 0.18 | 0.06 | 0.04 | 0.03 | 0.02 | 0.02 | 0.04 |
| Curtains (medium weight, draped) | 0.07 | 0.31 | 0.49 | 0.75 | 0.70 | 0.60 | 0.56 |
| Timber slat ceiling (50% open) | 0.20 | 0.45 | 0.65 | 0.55 | 0.40 | 0.35 | 0.51 |
| Mineral wool tile (15 mm, ceiling) | 0.10 | 0.25 | 0.55 | 0.80 | 0.85 | 0.75 | 0.61 |
| Mineral wool tile (25 mm, ceiling) | 0.15 | 0.40 | 0.70 | 0.90 | 0.90 | 0.85 | 0.73 |
| Perforated metal (25% open) + 50 mm MW | 0.25 | 0.60 | 0.85 | 0.95 | 0.90 | 0.80 | 0.83 |
| Acoustic plaster (25 mm) | 0.15 | 0.35 | 0.60 | 0.70 | 0.65 | 0.60 | 0.58 |
| Upholstered seating (occupied) | 0.60 | 0.74 | 0.88 | 0.96 | 0.93 | 0.85 | 0.88 |

### 12.2 Airborne Sound Insulation (Rw) of Common Constructions

| Construction | Mass (kg/m²) | Rw (dB) | Notes |
|---|---|---|---|
| 100 mm dense concrete block (plastered both sides) | 220 | 45 | Single-leaf mass law |
| 200 mm dense concrete block (plastered) | 440 | 52 | |
| 215 mm brick (plastered both sides) | 420 | 50 | |
| 100 mm concrete slab | 240 | 46 | |
| 150 mm concrete slab | 360 | 50 | |
| 200 mm concrete slab | 480 | 53 | |
| 250 mm concrete slab | 600 | 55 | |
| 75 mm metal stud + 2×12.5 mm PB each side | 35 | 45-48 | With mineral wool in cavity |
| 2× 75 mm metal stud (staggered) + 2×15 mm PB each side | 55 | 55-60 | Acoustic wall system |
| 160 mm CLT | 80 | 33-36 | Bare; needs additional layers |
| 160 mm CLT + resilient bar + 2×12.5 mm PB | 110 | 52-56 | Standard acoustic upgrade |
| Double glazing (4-16-4) | 20 | 29 | Coincidence dip at 3.15 kHz |
| Double glazing (6-16-6) | 30 | 32 | |
| Acoustic laminated double (6.4-20-8.8) | 38 | 40-43 | Best window performance |
| Triple glazing (4-12-4-12-4) | 30 | 33-35 | |

---

## 13. Thermal Expansion Coefficients

| Material | Coefficient of Thermal Expansion (×10⁻⁶ /°C) | Movement per 10 m for ΔT = 40°C (mm) |
|---|---|---|
| Steel (carbon) | 12 | 4.8 |
| Stainless steel 304 | 17.3 | 6.9 |
| Aluminum | 23.4 | 9.4 |
| Copper | 16.5 | 6.6 |
| Zinc | 22 | 8.8 |
| Concrete | 10-12 | 4.0-4.8 |
| Brick (clay) | 5-8 | 2.0-3.2 |
| Limestone | 4-8 | 1.6-3.2 |
| Granite | 7-9 | 2.8-3.6 |
| Marble | 4-7 | 1.6-2.8 |
| Glass | 9 | 3.6 |
| Timber (along grain) | 3-5 | 1.2-2.0 |
| Timber (across grain) | 25-45 | 10.0-18.0 |
| GFRP | 10-20 | 4.0-8.0 |
| ETFE | 100-120 | 40.0-48.0 |
| PVC | 50-80 | 20.0-32.0 |

**Design Implication:** Movement joints required at intervals determined by material expansion rate and expected temperature range. Typical joint intervals: concrete 30-50 m, brick 10-15 m, aluminum cladding 6-8 m, zinc standing seam 10-12 m. ETFE requires accommodating large movements in fixing details.

---

## 14. Fire Classification Cross-Reference

### 14.1 European (Euroclass) vs. UK Legacy vs. US (ASTM)

| Euroclass (EN 13501-1) | Description | UK Legacy (BS 476) Approx. | ASTM E84 Approx. |
|---|---|---|---|
| A1 | Non-combustible | Non-combustible | — |
| A2-s1,d0 | Very limited combustibility, no smoke, no droplets | Class 0 | Class A (FSI 0-25) |
| B-s1,d0 | Limited combustibility | Class 0 | Class A (FSI 0-25) |
| B-s2,d0 | Limited combustibility, limited smoke | Class 1 | Class A-B |
| C-s2,d0 | Moderate contribution to fire | Class 1-2 | Class B (FSI 26-75) |
| D-s2,d0 | Significant contribution to fire | Class 3 | Class C (FSI 76-200) |
| E | High contribution to fire | Class 3-4 | Class C |
| F | No performance determined | — | — |

**Suffix Notation:**
- s1, s2, s3: smoke production (s1 = lowest)
- d0, d1, d2: flaming droplets (d0 = none)

### 14.2 Material Fire Classifications

| Material | Typical Euroclass | Notes |
|---|---|---|
| Concrete | A1 | Non-combustible in all forms |
| Steel | A1 | Non-combustible; loses strength at temperature |
| Clay brick | A1 | Non-combustible |
| Natural stone | A1 | Non-combustible |
| Glass | A1 | Non-combustible |
| Aluminum | A1 | Non-combustible; melts at ~660°C |
| Plasterboard | A2-s1,d0 | Paper facing adds minor combustibility |
| Mineral wool | A1-A2 | Non-combustible; binder may produce minor smoke |
| Timber (untreated) | D-s2,d0 | Combustible; predictable charring |
| Timber (FR treated) | B-s1,d0 | Fire retardant impregnation |
| CLT (with FR treatment) | B-s1,d0 to C | Depends on treatment depth |
| PIR insulation (foil-faced) | B-C | Depends on facer and formulation |
| EPS insulation | E-F | Highly combustible; must be protected |
| XPS insulation | E | Similar to EPS; melts and burns |
| Wood fibre insulation | E | Combustible; slow ignition |
| ETFE | B-s1,d0 | Melts and shrinks away from flame (self-venting) |
| HPL (compact laminate) | B-s2,d0 | Phenolic resin based |
| ACM (aluminum composite, PE core) | E-F | **CRITICAL: fire hazard**; banned on UK buildings > 18 m post-Grenfell |
| ACM (aluminum composite, FR core) | B-s1,d0 | Mineral-filled core; acceptable for high-rise |

---

## 15. Cost Reference Ranges (Indicative, 2024-2025)

| Material | Unit | Cost Range (USD) | Notes |
|---|---|---|---|
| Ready-mix concrete C30/37 | per m³ | $120-200 | Pump-delivered; varies by region |
| Structural steel (fabricated, erected) | per tonne | $3,000-5,500 | Including connections and erection |
| Steel rebar (cut, bent, fixed) | per tonne | $1,200-1,800 | |
| CLT panel (supplied) | per m³ | $800-1,500 | Excluding connections and crane |
| Glulam beam (supplied) | per m³ | $1,000-2,000 | Depending on grade and finish |
| Facing brick (supply + lay) | per m² | $80-200 | Standard to premium facing |
| Natural stone cladding (30 mm) | per m² | $150-600 | Limestone to granite |
| Aluminum curtain wall | per m² | $600-1,500 | Standard to high-performance |
| Structural glazing (point-fixed) | per m² | $800-2,000 | Including spider fittings |
| Zinc standing seam roofing | per m² | $80-160 | Supply + install |
| Copper standing seam roofing | per m² | $120-250 | Supply + install |
| Painted steel cladding (insulated) | per m² | $80-150 | Composite panel or profiled sheet |
| Terracotta rainscreen | per m² | $150-350 | Including subframe |
| Timber cladding (larch/cedar) | per m² | $60-120 | Supply + fix |
| ETFE cushion system | per m² | $250-500 | Including frame and inflation |
| Mineral wool insulation (150 mm) | per m² | $12-25 | Supply + fix |
| PIR insulation (120 mm) | per m² | $20-40 | Supply + fix |

**Note:** Costs are highly regional, subject to market conditions, and should be verified with local quantity surveyors. Figures above are order-of-magnitude guidance for feasibility and comparison only.
