// Defining the N x N area
const AREA = 4

// Defining the letter #
let remainingNb = AREA * AREA

// Defining the input chain
let letterInput = ''



// Defining function to create boggle board
function createboggleb()
{
    let boggleb = document.getElementById("boggleb")

    // For each line
    for (let i = 0; i < AREA; i++)
    {
        // Creating div
        let div = document.createElement("div")
        div.className = "letter-div"

        // For each letter
        for (let j = 0; j < AREA; j++)
        {
            // Creating div
            let box = document.createElement("div")
            box.className = "letter-box"

            // Appending "letter-box" box to "letter-div" div
            div.appendChild(box)
        }

        // Appending "letter-div" div to "boggleb" div
        boggleb.appendChild(div)
    }
}



export { AREA, createboggleb }


