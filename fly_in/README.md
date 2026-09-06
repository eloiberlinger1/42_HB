- do parsing DONE

- define objects of business logic

- 





TODO ;

check parser 


Parser Constraints
The input file must respect the expected structure and syntax:
• The first line must define the number of drones using nb_drones: <positive_integer>.
• The program must be able to handle any number of drones.
• There must be exactly one start_hub: zone and one end_hub: zone.
• Each zone must have a unique name and valid integer coordinates.
• Zone names can use any valid characters but dashes and spaces.
• Connections must link only previously defined zones using connection: <zone1>-<zone2>
[metadata].
• The same connection must not appear more than once (e.g., a-b and b-a are con-
sidered duplicates).
• Any metadata block (e.g., [zone=... color=...] for zones, [max_link_capacity=...]
for connections) must be syntactically valid.
• Zone types must be one of: normal, blocked, restricted, priority. Any invalid
type must raise a parsing error.
• Capacity values (max_drones for zones, max_link_capacity for connections) must
be positive integers.
• Any other parsing error must stop the program and return a clear error message
indicating the line and cause.
It’s highly recommended to make your own map files on top of the ones
provided in the subject for handling edge cases and error handling