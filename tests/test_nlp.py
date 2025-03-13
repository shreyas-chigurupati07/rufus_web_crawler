import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rufus_nlp import filter_relevant_text

# Sample extracted web content
raw_text = """
Tesla has launched its new electric car, the Tesla Model X Plaid, featuring a tri-motor setup 
that delivers an acceleration of 0-60 mph in just 2.5 seconds. It comes with a 333-mile range 
per full charge and supports supercharging at 250 kW. The car also includes an advanced 
Autopilot system with improved lane navigation, collision avoidance, and self-parking. 
Tesla’s new infotainment system features a 17-inch touchscreen, high-performance gaming, and voice controls.
"""

# User query
query = "What are the key features of the Tesla Model X Plaid?"

# Run filtering
filtered_output = filter_relevant_text(raw_text, query)

# Print result
print("\n".join(filtered_output))