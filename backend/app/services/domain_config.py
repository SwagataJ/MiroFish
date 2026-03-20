"""
Domain Configuration Module
Provides domain-specific grounding for MiroFish simulations.
Currently supports: fashion_retail
"""

from typing import Dict, Any, Optional


FASHION_RETAIL_DOMAIN: Dict[str, Any] = {
    "name": "fashion_retail",
    "display_name": "Fashion Retail",
    "description": (
        "Fashion retail industry including brands, designers, influencers, "
        "consumers, retailers, and fashion media."
    ),

    # Entity type reference hints injected into the ontology generator prompt
    "entity_type_references": """
**Individual (specific)**:
- Designer: Fashion designer or creative director
- Influencer: Fashion influencer, content creator, or KOL
- Celebrity: Celebrity or public figure with fashion influence
- Consumer: End consumer, fashion enthusiast, or shopper
- Stylist: Professional stylist or fashion editor
- Journalist: Fashion journalist or critic

**Individual (fallback)**:
- Person: Any individual not fitting a more specific person type

**Organization (specific)**:
- Brand: Fashion brand or label (e.g., Zara, H&M, Gucci)
- Retailer: Retailer or e-commerce platform (e.g., ASOS, Nordstrom)
- FashionMagazine: Fashion magazine or media outlet (e.g., Vogue, Elle)
- Manufacturer: Clothing manufacturer, supplier, or textile producer

**Organization (fallback)**:
- Organization: Any organization not fitting a more specific type
""",

    # Edge type reference hints
    "edge_type_references": """
- COLLABORATES_WITH: Brand-designer or brand-influencer collaboration
- ENDORSES: Celebrity or influencer endorsing a brand or product
- SELLS: Retailer selling a brand's products
- REVIEWS: Influencer, magazine, or journalist reviewing a brand/product
- COMPETES_WITH: Competing brands or retailers
- SUPPLIES_TO: Manufacturer supplying to a brand or retailer
- REPRESENTS: Agent or manager representing a designer or celebrity
- PARTNERS_WITH: Co-branding or strategic partnerships
""",

    # Injected into the simulation context in the user message
    "simulation_context": (
        "This simulation is scoped to the **fashion retail industry**. "
        "All entities must be fashion industry stakeholders: brands, designers, influencers, "
        "consumers, retailers, manufacturers, or fashion media. "
        "Social media dynamics should reflect fashion discourse — trend launches, product drops, "
        "brand controversies, influencer campaigns, sustainability debates, and consumer reactions. "
        "Keep all entities and relationships grounded in the fashion retail world."
    ),

    # Additional entity types recognised as individual-type in the profile generator
    "individual_entity_types": [
        "designer", "influencer", "celebrity", "consumer", "stylist", "journalist"
    ],

    # Additional entity types recognised as group/institution-type in the profile generator
    "group_entity_types": [
        "brand", "retailer", "fashionmagazine", "manufacturer"
    ],
}


# Registry of all supported domains
DOMAIN_REGISTRY: Dict[str, Dict[str, Any]] = {
    "fashion_retail": FASHION_RETAIL_DOMAIN,
}


def get_domain_config(domain: Optional[str]) -> Optional[Dict[str, Any]]:
    """Return the domain config dict for the given domain key, or None."""
    if not domain:
        return None
    return DOMAIN_REGISTRY.get(domain)
