# 1. For each of the following string methods:
#   (a) replace
#   (b) split
#   (c) format
#   (d) join
#   (e) find
#   - Explain in your own words what the method does and give an example
#   - e.g. stringmethod1 = "upper"
# -         stringmethod1_explanation = "This method converts a string to upper case"
#           stringexample1 = "aisha"
#           print(stringexample1.upper()) ==> AISHA

example1 = """
<div class="newsPost_newsBlock__FZRHV"><p><p>Think of the most remarkable buildings you have been to.</p>
<p>Take away the lighting, power supply, heating/cooling, plumbing, and security systems. What would you have left? An uninhabitable dark structure!&nbsp;<br>The provision of these essential systems to make a building comfortable for use are what makeup MEP designs.&nbsp;</p>
<p>MEP (mechanical, electrical, and plumbing) design has evolved considerably from the very beginning. Mechanical, electrical, and plumbing systems have been an invaluable aspect of building design since the early days of construction. Over the years, advances in technology, building materials, and energy efficiency have contributed to the advancement of MEP design.</p>
<p>In the past, MEP design focused on the basic needs of a building, such as heating, ventilation, and lighting. The main goal was to ensure the functionality and habitability of the building.&nbsp;<br>&nbsp;<br>As technology advanced, MEP systems design changed. The introduction of computers and automation made the design more accurate and sustainable. Designers now consider the environmental impact of buildings and the cost of energy consumption, which led to the development of more energy-efficient and environmentally friendly systems.</p>
<p>Today, MEP system design is more complex than ever. The expectations of building owners and operators have increased, and increasingly complex systems are designed to meet these expectations. Smart systems, renewable energy sources, and advanced control systems are now integrated into MEP system design.<br>&nbsp;<br>One of the biggest trends in MEP design today is the use of smart building technology. Smart buildings use advanced control systems to optimize energy use, improve occupant comfort, and reduce utility bills. These systems can monitor water use, and energy use, adjust lighting and temperature based on actual need, and even predict maintenance needs before problems arise. By integrating these systems into MEP design, building owners can save on energy costs and improve the overall sustainability of their buildings.</p>
<p>Another trend in MEP design is the use of renewable energy sources. As the cost of renewable energy continues to decline, more and more buildings are incorporating solar panels, and other renewable energy sources into MEP systems. These systems can lessen the building's dependence on traditional energy sources and provide a more sustainable energy source.</p>
<p>Looking ahead, MEP design will likely continue to evolve. The integration of artificial intelligence and machine learning will likely play an important role in future MEP designs, making systems more accurate and efficient.<br>&nbsp;<br>In summary, the evolution of MEP design has come a long way over the years - from simple systems focused on functionality to today's energy-efficient systems incorporating smart technologies and renewable energy. Looking ahead, the role of MEP design in the building industry will continue to grow, and future innovations are sure to be exciting.</p>
<p>&nbsp;</p></p></div>
"""
plain_text = example1.replace('<p>', '<h1>').replace('</p>', '</h1>').replace('<div class="newsPost_newsBlock__FZRHV">', '').replace('</div>', '').replace('<br>', '').replace('&nbsp;', '')
# print(plain_text)

# example2 = input("Enter two numbers seperated by hashtag: ")
# print(example2.split('#'))

example3 = "This string will be formatted with a new {word}"
words = ['"Cake"', '"Bread"', '"Car"']
print(example3.format(word=words[2]))

# 2. For each of the following list methods:
#   (a) copy
#   (b) index
#   (c) extend
#   (d) insert
#   (e) reverse
#   - Explain in your own words what the method does and give an example
#   - e.g. listmethod1 = "append"
# -         listmethod1_explanation = "This method adds a new item to the end of the list"
#           listexample1 = ["aisha", "shedrack"]
#           print(listexample1.append("ahmad")) ==> ["aisha", "shedrack", "ahmad"]