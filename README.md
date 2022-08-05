# Boggle

#### VIDEO DEMO : <URL https://youtu.be/SJ5L67cXax8>

#### DESCRIPTION :

My project is centered around the game Boggle. In Boggle, one or more players get a grid of 16 letters and must compete to find valid vords in the grid that :

- are at least three letters long,
- have each letter after the first being a horizontal, vertical, or diagonal neighbour of the one before it,
- and that use no letter box more than once.

It is quite a difficult game, but not using my Boggle app ! Indeed, it can generate all the valid vords in the board in very little time.

The main route of the app is the " / " route. On this route you can find an empty boggle board and a helper message. To fill the board, you can either type each letter (and I of course included defensive code to prevent non-alpha input) and then press enter or get a randomly generated board by pressing the button for that.

From here, the user is redirected to the " /boggle/&lt;letterInput&gt; " route. This route is flexible and can accept any valid letter-chain (once again, I included defensive code). Python code than extracts the letter-chain and runs the boggle function.

This function is the algorithmic part of my app. It is quite difficult to explain, but I part of the code and a partial explanation is provided in the engine tab of the app. For this app I optimised for pace and I needed a reduced time of computation because the function often needs to verify the validity of vords in a huge dictionary (a little under 300.000 entries). I therefore implemented a Trie object built from a Node object and implemented multiple mathods for each. Among them are :

 - Node.char (the char held by the node)
 - Node.end (the boolean held by the node telling if this node path is a valid entry)
 - Node.child (the children node of that node)

 for the Node object and :

 - Trie.add (adding a valid entry to populate the trie)
 - Trie.find (finding out if a vord is a valid entry)
 - Trie.prefix (finding out if there are in the trie (and, therefore, in the dictionary, entries having that prefix))

 for the Trie object. The boggle function returns a dict object in the format { "entry" : [boxbool] }, the entry being the vord and the boxbool being the path used in the grid to find that vord. The " /boggle/&lt;letterInput&gt; " route then renders the boggle template. Here, the dict of valid entries found on the grid are displayed, and their path is displayed on teh boggle grid if their &lt;div&gt; is hovered.

 Next comes the " /dictionary " route. It can be accessed either from the tab on the nvabar or from any vord in the " /boggle/&lt;letterInput&gt; " route. This is nothing more than a dictionary that can confirm if a vord is a valid entry and give the definition. Here a RegEx is used to filter from the definition only the necessary content.

 Next is the " /history " route. It is practical because it has a table that remembers the boards played. They are filtered for repetition and of course any previous board can be played again from that table

 The last route is the " /engine " route. I included the interesting code of my project and explained the functioning and the reasoning behind it.