#load into Neo4j db
from neo4j import GraphDatabase
import os 
from dotenv import load_dotenv 

load_dotenv()

print(os.environ["NEO4J_URI"])