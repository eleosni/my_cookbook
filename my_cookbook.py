import tkinter as tk
import requests
HEIGHT = 800
WIDTH = 800

def test_function(entry):
    print("this entry", entry)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
button = tk.Button(frame, text="Рецепт 1", bg="gray", command=lambda: test_function(entry.get()))
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
button1 = tk.Button(frame, text="Рецепт 2", bg="gray")
button1.place(relx=0.2, rely=0, relwidth=0.25, relheight=0.25)
button2 = tk.Button(frame, text="Рецепт 3", bg="gray")
button2.place(relx=0.4, rely=0, relwidth=0.25, relheight=0.25)
button3 = tk.Button(frame, text="Рецепт 4", bg="gray")
button3.place(relx=0.6, rely=0, relwidth=0.25, relheight=0.25)
button4 = tk.Button(frame, text="Рецепт 5", bg="gray")
button4.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.25)
button5 = tk.Button(frame, text="Рецепт 6", bg="gray")
button5.place(relx=0.2, rely=0.2, relwidth=0.25, relheight=0.25)
button6 = tk.Button(frame, text="Рецепт 6", bg="gray")
button6.place(relx=0.4, rely=0.2, relwidth=0.25, relheight=0.25)
button7 = tk.Button(frame, text="Рецепт 6", bg="gray")
button7.place(relx=0.6, rely=0.2, relwidth=0.25, relheight=0.25)








root.mainloop()
import json
import requests
str_json = """
{
  "recipes": [
    {
      "uuid": "fc988768-c1e9-11e6-a4a6-cec0c932ce01",
      "name": "Pan Roasted Chicken with Lemon, Garlic, Green Beans and Red Potatoes",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/w_300,c_fill,h_250/pan-roasted-chicken-with-lemon-garl-12.jpg"
      ],
      "lastUpdated": 524224800,
      "description": "Pan-roasted chicken with lemon, garlic, green beans and red potatoes",
      "instructions": "1. Preheat the oven to 230deg C. Coat a large baking dish or cast-iron skillet with 1 tbs of olive oil. Arrange the lemon slices in a single layer in the bottom of the dish or skillet.<br>2. In a large bowl, combine the remaining oil, lemon juice, garlic, salt and pepper; add the green beans and toss to coat. Using a slotted spoon or tongs, remove the green beans and arrange them on top of the lemon slices. Add the potatoes to the same olive oil mixture and toss to coat. Using a slotted spoon or tongs, arrange the potatoes along the inside edge of the dish or skillet on top of the green beans. Place the chicken in the same bowl with the olive oil mixture and coat thoroughly. Place the chicken, skin side up, in the dish or skillet. Pour any remaining olive oil mixture over the chicken.<br>3. Roast for 50 minutes. Remove the chicken from the dish or skillet. Place the beans and potatoes back in the oven for 10 minutes more or until the potatoes are tender.<br>4. Place a chicken breast on each of 4 serving plates; divide the green beans and potatoes equally. Serve warm.",
      "difficulty": 3
    },
    {
      "uuid": "8825cde8-630a-4027-9b9c-38b34bd4426b",
      "name": "Roasted Chicken with Whole Lemon And Ginger",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/roasted-chicken-with-whole-lemon-an.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/roasted-chicken-with-whole-lemon-an-2.jpg"
      ],
      "lastUpdated": 1481712335,
      "instructions": "Preheat oven to 190 C, 375 F, Gas Mark 5. Grate one of the lemons and place the zest in a bowl. Grate the root ginger and mix with the lemon zest and the salt. Prick the remaining lemon with a fork punchuring the skin, wash and place the whole lemon inside the chicken. Mix the remaining mixture with the olive oil and rub into the chicken liberally. Place the chicken on a roasting rack over a roasting tray. Fill with the water and cover with tin foil. Cook the chicken according to pack istructions. Remove the tin foil 15 minutes before end of cooking time to brown skin. Remove the chicken from the oven, allow to rest for approxinmately 5-10 minutes,Remove the lemon from inside the chicken and being very careful squeeze any remaining juices into the bottom of the roasting tin. Carefully remove any fat from the surface of the juices and discard. Pour the remaining juice into a small pan and taste for flavour. (If it is too sharp add 1-2 tablespoons of caster sugar and stir until it dissolves over a gentle heat). Carve the chicken and arrrange on a serving plate. Pour the juices over the meat. NOTES : Organic baked chicken with whole lemon and fresh ginger.Excellent with whole roast tomatoes and fresh watercress.",
      "difficulty": 3
    },
    {
      "uuid": "19262b24-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Meat Loaf",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/meat-loaf-26.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/meat-loaf-27.jpg"
      ],
      "lastUpdated": 1481715335,
      "description": "Yummy home made meat loaf, great for left overs.",
      "instructions": "Mix thyme, cayenne, nutmeg, Panko bread crumbs, salt, and pepper into a small bowl, set aside. Mix eggs, minced garlic, minced or chopped onion, and 1/4 cup BBQ sauce in a medium bowl.<br>Break up ground beef so its not blocked or clumped, mix in the egg mixture until evenly distributed throughout then add bread crumb mixture until evenly distributed.<br>Put into loaf pan.<br>Bake at 350 degrees for 60 minutes<br>Take out, Drain grease from pan<br>Add 1 cup BBQ sauce on top then,<br>Bake for 15-20 minutes,",
      "difficulty": 1
    },
    {
      "uuid": "19262e08-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Hearty Moroccan Chicken with Couscous",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/hearty-moroccan-chicken-with-c-5c758b.jpg"
      ],
      "lastUpdated": 1481712135,
      "description": "Try this Hearty Moroccan Chicken with Couscous recipe, or contribute your own.",
      "instructions": "1. In heavy large nonstick saucepan or Dutch oven, place olive oil over high heat. Add chicken and cook about 10 minutes, turning to brown on all sides. Stir in onion, 2. garlic, ginger, carrots, chickpeas, raisins, cinnamon, cumin, turmeric and water. Bring to a simmer, reduce heat and cook about 20 minutes.<br>3. Stir in zucchini and simmer an additional 10 minutes.<br>4. Remove cinnamon sticks. Serve in large bowls over couscous.",
      "difficulty": 2
    },
    {
      "uuid": "1926318c-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Minted Orzo with Tomatoes",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/minted-orzo-with-tomatoes-30dc99.jpg"
      ],
      "lastUpdated": 1471712335,
      "description": "",
      "instructions": "1. Cook orzo according to package directions. Drain, rinse with cold water, drain again, place in large bowl and set aside.<br>2. Heat oil in large nonstick skillet over medium-high heat; sauté onion until tender, stirring frequently, until browned, about 15 minutes.<br>3. In a large bowl, toss orzo with onion, broth, lemon juice and parsley.<br>     4. Cover and chill if making ahead. Bring to room temperature; stir in tomatoes and mint; season with salt and pepper to taste.",
      "difficulty": 2
    },
    {
      "uuid": "192633bc-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Goat Cheese Rolled in Dried Cranberries",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/goat-cheese-rolled-in-dried-cr-216282.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/goat-cheese-rolled-in-dried-cranber.jpg"
      ],
      "lastUpdated": 1481342335,
      "description": "Just in time for the holidays, this recipe is simple and easy! Only two ingredients and in five minutes, you have a gourmet and delicious appetizer.",
      "instructions": "Remove fresh Goat cheese from packaging and set aside.Evenly distribute cranberries on a sheet of parchment paper. Roll log into the cranberries and wrap with the parchment paper. Firmly roll wrapped log so cranberries adhere to the cheese. Place in refrigerator to chill. Unwrap log 30 minutes before serving. Serve with your favorite breads or crackers ",
      "difficulty": 4
    },
    {
      "uuid": "192635d8-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Tomato Puff Pastry Bites",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/tomato-puff-pastry-bites-3.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/tomato-puff-pastry-bites-bc48c5.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/tomato-puff-pastry-bites-4.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/swiss-cheese-fondue-1bb369.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/swiss-cheese-fondue.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/bloomin-onion-bread.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/royal-blend-chicken-salad-f2756c.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/lemon-artichoke-baked-orzo-a825b7.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cinnamon-applesauce-pancakes-634671.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/crme-brle-rice-pudding-649fda.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/goat-cheese-stuffed-mini-portobello.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/holiday-brussels-sprouts.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/deviled-eggs-12.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/deviledeggs-6747ac.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/garlic-chicken-bites.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/bruschetta-10.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/bruschetta-41.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/bruschetta-44.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/bruschetta-45.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/untitled-recipe-4667.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/baked-asparagus-with-parmesan--99fa77.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/spinach-artichoke-dip-4.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/spinach-artichoke-dip-42.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/spinach-artichoke-dip-45.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/appetizer-candied-nuts.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/brown-rice-and-black-bean-burr-ae246c.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/rice-and-turkey-stuffed-pepper-668dbb.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/italian-sushi-77727b.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/spicy-salmon-avocado-tower-ec8598.jpg"
      ],
      "lastUpdated": 1481711335,
      "description": "If you like tomatoes, you will love this little appetizer. You can make one or as many as you like. Great way to use some garden fresh tomatoes. You can easily sprinkle some feta cheese and olives after they are baked.",
      "instructions": "Preheat oven to 425 deg. Cut tomato slices. You don't want them to be too thin and yet you don't want them to be too thick either. Set aside.  Cut puff pastry into small squares that are roughly about the same size as your tomato slices. Place some parchment paper on a cookie sheet. Lay the puff pastry square on the parchment paper. Add about 1 TBS +/- of Jack cheese (or provolone, gouda, havarti, mozzarella). Add some sliced/chopped onion. I had some green onion from the garden and use the white tip only. But, you can easily add regular onion. Place a tomato slice on top. Add a pinch of Italian seasoning. Season with salt and pepper, if you like. If you are going to add feta cheese later, you might not need to add any salt. Bake in a preheated 425 oven for about 10-12 minutes. Please check them... you want them golden brown and nicely puffed. Depending on the puff pastry size, the cooking time will vary. Mine took 12 minutes. Sprinkle feta on top if you like.",
      "difficulty": 2
    },
    {
      "uuid": "192636c8-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Cauliflower Buffalo Bites",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cauliflower-buffalo-bites.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cauliflower-buffalo-bites-2.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/recipe-no-image.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cauliflower-buffalo-bites-6.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cauliflower-buffalo-bites-8.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/cauliflower-buffalo-bites-9.jpg"
      ],
      "lastUpdated": 1481711335,
      "description": "Very good, could replace having Buffalo chicken!",
      "instructions": "Preheat oven to 400. Put non stick aluminum foil on a sheet pan or coat it with cooking spray.  Combine the flour, water, paprika, garlic powder, salt and pepper in a large bowl.  Mix well.  Add the cauliflower to the mixture and coat well.  Drain off excess batter and lay on sheet pan.  Bake for 15-20 minutes and then turn over and cook for another 10-15 minutes.  Combine the hot sauce and butter in a bowl and mix well. Pour the sauce mixture over the cauliflower and mix well.  Cook for another 5-10 minutes or until lightly browned. Serve with blue cheese dressing and celery sticks. Enjoy!",
      "difficulty": 2
    },
    {
      "uuid": "1926397a-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Red Pepper Dip",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/red-pepper-dip-2.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/red-pepper-dip-3fe0d2.jpg"
      ],
      "lastUpdated": 1451712335,
      "description": "This is a very quick and easy dip. Because most of the ingredients can be kept on hand (especially if you keep a pot of fresh basil year round) it makes a delicious snack to whip up for unexpected guests.",
      "instructions": "In skillet saute garlic and onion in oil till tender and transparent.In food processor, blend remaining ingredients until nuts are finely chopped. With motor running add garlic and onion until incorporated. Salt and pepper to taste.Serve dip with appetizer toasts or crackers.",
      "difficulty": 1
    },
    {
      "uuid": "19263a92-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Ham or Sausage Quiche",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/ham-or-sausage-quiche.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/ham-or-sausage-quiche-2.jpg"
      ],
      "lastUpdated": 1481412335,
      "description": "Easy quiche - try it with different meat and cheese combinations.",
      "instructions": "Separate the eggs. Beat the egg whites until fluffy. Mix together cream cheese and egg yolks, then stir in the cheese, ham or sausage, and jalapenos. Fold in the beaten egg whites. Pour into unbaked pie crust and bake at 350 for 35 min.",
      "difficulty": 2
    },
    {
      "uuid": "19263d94-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Antipasto Skewers",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/antipasto-skewers-2.jpg"
      ],
      "lastUpdated": 1481332335,
      "description": "This recipe is an easy appetizer that works great for parties and small gatherings. You can add mozzarella and fresh tomatoes too, if you like.",
      "instructions": "1. First, thread each skewer with 1 pimento-stuffed olive.<br>2. Next, fold the bell pepper strips in half then thread one onto each skewer.<br>3. In a similar fashion, fold the salami rounds once or twice then thread one onto each skewer.<br>4. The black olives come next, followed by the artichoke hearts, the other half of the bell peppers and finally the other half of the pimento-stuffed olives.<br>5. Season with black pepper and sprinkle with chopped parsley before serving.",
      "difficulty": 5
    },
    {
      "uuid": "19263e8e-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Savory Pita Chips",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/savory-pita-chips-3.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/savory-pita-chips-0d91d9.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/savory-pita-chips-4.jpg"
      ],
      "lastUpdated": 1481112335,
      "description": "Tasty all by themselves, and even better dipped into homemade hummus! So much better than store-bought, and so easy and quick to make, that you'll never buy commercial pita chips again!",
      "instructions": "Preheat oven to 400F. Mix the garlic powder, garlic granules, onion powder, oregano, paprika, salt, and pepper in a small container (there will be some left over, so a spice jar makes a good container). One at a time, brush the pita breads with olive oil, cut into 8 wedges (same pattern as cutting a pie or a pizza). Arrange the pita wedges in a single layer on a baking sheet, and sprinkle with the seasoning mix. Bake in a 400F oven for 10 minutes.",
      "difficulty": 5
    },
    {
      "uuid": "19263fe2-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Caramelized French Onion Dip",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/caramelized-french-onion-dip.jpg"
      ],
      "lastUpdated": 1481562335,
      "description": "Makes: 1 cup",
      "instructions": "1. Heat olive oil in a small pan over medium-low heat. Add onion and garlic and cook until they turn brown in color, stirring occasionally, about 20 minutes. Take care not to burn the onions. Remove from heat and allow to cool.<br>2. In a bowl combine cooled onion and garlic, mayonnaise, sour cream, Worcestershire sauce, salt and pepper. Chill 30 minutes.",
      "difficulty": 1
    },
    {
      "uuid": "192640d2-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Chocolate Fudge Swirled Lemon Ricotta Tart",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/chocolate-fudge-swirled-lemon-ricotta-tart-1500280.jpg"
      ],
      "lastUpdated": 1481711235,
      "description": "Try this Chocolate Fudge Swirled Lemon Ricotta Tart recipe, or contribute your own.",
      "instructions": "9 graham crackers (or 2 cups graham cracker crumbs)<br>6 tablespoons salted butter; melted<br>1/4 cup cocoa powder<br>1/3 cup brown sugar<br>2/3 cup milk",
      "difficulty": 2
    },
    {
      "uuid": "192642da-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "Hot Chocolate Pudding",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/hot-chocolate-pudding.jpg",
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/hot-chocolate-pudding-6fd89c.jpg"
      ],
      "lastUpdated": 1481712935,
      "description": "Little chocolate puddings, fluffy outside and molten within, a cross between a soufflé and a sponge pudding. I make them with the best chocolate I can get my hands on. The hazelnut spread such as Nutella or Green and Black’s sounds an odd addition, but in fact lends a lingering, nutty depth. If you feel the need to offer cream (and well you might), you might like to make it a jug of pouring cream rather than the rich, thick sort.",
      "instructions": "Set the oven at 200°c/Gas 6 (390 degrees F). Lightly butter 4 small ramekins or ovenproof cups. Break the chocolate into rough pieces and leave to melt in a basin suspended over gently simmering water. Let it melt without stirring, occasionally poking any unmelted chocolate down into the liquid chocolate. Put the sugar into the bowl of the food mixer, separate the eggs and add the yolks to the sugar. Beat till thick and creamy. Whisk the egg whites till airy and almost stiff. Stir the butter into the chocolate and leave to melt then gently stir in the chocolate hazelnut spread. Fold the chocolate mixture into the egg and sugar then carefully fold in the beaten egg whites with a metal spoon. Take care not to over mix. Just firmly, calmly mix the egg white into the chocolate making certain there are no floating drifts of egg white. Scoop into the four buttered dishes and place on a baking sheet. Bake for 12-15 minutes till risen. The tops should be cracked and the centres still slightly wobbly.",
      "difficulty": 3
    },
    {
      "uuid": "5f2a8390-c1ef-11e6-a4a6-cec0c932ce01",
      "name": "English Toffee with Dark Chocolate and Almond",
      "images": [
        "https://bigoven-res.cloudinary.com/image/upload/t_recipe-256/english-toffee-with-dark-chocolate-.jpg"
      ],
      "lastUpdated": 1481712330,
      "description": "Try this English Toffee with Dark Chocolate and Almond recipe, or contribute your own.",
      "instructions": "Prepare a large baking sheet lined with parchment paper. In a deep, heavy-bottomed pan, heat the butter, sugar and salt over medium heat. Stir frequently until the butter is melted and the ingredients combine. Slowly bring the mixture to a boil. Let it simmer over medium heat. Stir occasionally with a wooden spatula until the color of the mixture changes to amber. Around 20 minutes. Remove toffee from heat, carefully spread it evenly over the baking sheet with a spatula. Sprinkle the chocolate chips over the hot toffee and allow to set for a few minutes to soften. Gently spread the chocolate to thinly coat the top of the toffee. Sprinkle the almonds over the chocolate layer. Use a sheet of clean parchment paper to gently pat the almonds into the chocolate. Place the toffee into the refrigerator for at least an hour to harden. Once chilled, carefully remove the toffee from the pan by lifting the hangs of the parchment paper, and break into pieces.",
      "difficulty": 1
    }
  ]
}
"""
print(type(str_json))
data = json.loads(str_json)
print(type(data))

