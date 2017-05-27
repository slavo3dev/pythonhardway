my_name = 'Slavo'
my_age = 35 # not a lie
my_height = 184 # cm
one_meter = 100
my_weight = 89 # kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Bold'

print ("Let's talk about %s." % my_name)
print ("He's %d cm or %r m tall." % (my_height,my_height/100))
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth
)
# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))