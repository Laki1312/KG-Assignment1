from pathlib import Path

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD

#Base namespace for the vocabulary
BASE = "http://kg-course.io/food-nutrition/"

# Define namespaces
SCHEMA = Namespace("https://schema.org/")
EX = Namespace(BASE)

g = Graph()

# Bind prefixes to namespaces for better readability
g.bind("schema", SCHEMA)
g.bind("ex", EX)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

# Output folder and file
OUT_DIR = Path(__file__).resolve().parents[1] / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_PATH = OUT_DIR / "KEN4256-vocabulary-TEAMX.ttl"


def add_property(prop, label, comment, domain=None, range_=None):
    # Declare it as an RDF property
    g.add((prop, RDF.type, RDF.Property))
    
    # Add human-readable label and description
    g.add((prop, RDFS.label, Literal(label)))
    g.add((prop, RDFS.comment, Literal(comment)))
    
    # Add domain and range if provided
    if domain is not None:
        g.add((prop, RDFS.domain, domain))
    if range_ is not None:
        g.add((prop, RDFS.range, range_))

# Custom property for Restaurant: hasTableBooking
add_property(
    EX.hasTableBooking,
    "has table booking",
    "Indicates whether the restaurant supports table booking.",
    domain=SCHEMA.Restaurant,
    range_=XSD.boolean
)

# Custom property for Restaurant: hasOnlineDelivery
add_property(
    EX.hasOnlineDelivery,
    "has online delivery",
    "Indicates whether the restaurant offers online delivery.",
    domain=SCHEMA.Restaurant,
    range_=XSD.boolean
)

# Custom property for Restaurant: isDeliveringNow
add_property(
    EX.isDeliveringNow,
    "is delivering now",
    "Indicates whether the restaurant is currently delivering.",
    domain=SCHEMA.Restaurant,
    range_=XSD.boolean
)

# Custom property: hasMenu
add_property(
    EX.hasMenu,
    "has order menu",
    "Indicates whether the restaurant provides an order menu option.",
    domain=SCHEMA.Restaurant,
    range_=XSD.boolean
)

# Custom property: ratingColor
add_property(
    EX.ratingColor,
    "rating color",
    "Visual color label associated with the restaurant rating.",
    domain=SCHEMA.Restaurant,
    range_=XSD.float
)

# Custom property: ratingText
add_property(
    EX.ratingText,
    "rating text",
    "Textual label associated with the restaurant rating.",
    domain=SCHEMA.Restaurant,
    range_=XSD.float
)

# Custom property: numberOfDishesInCuisines
add_property(
    EX.numberOfDishesInCuisines,
    "number of dishes in cuisines",
    "Number of dishes available within the listed cuisines for a restaurant.",
    domain=SCHEMA.Restaurant,
    range_=XSD.integer
)


# Custom property: averageCostForTwoUSD
add_property(
    EX.averageCostForTwoUSD,
    "average cost for two in USD",
    "Average cost for two people in USD.",
    domain=SCHEMA.Restaurant,
    range_=XSD.float
)

# Save the vocabulary as Turtle
g.serialize(destination=str(OUT_PATH), format="turtle")
print(f"Vocabulary written to: {OUT_PATH}")
