import { AREA, createboggleb } from "/static/helper.js"



// DOM
document.addEventListener('DOMContentLoaded', function()
{



    // Defining the letter #
    let remainingNb = AREA * AREA

    // Defining the input chain
    let letterInput = ''



    // Create the boggle board
    createboggleb()



    // Listening for input of alpha, del, and enter
    document.addEventListener("keyup", function(e)
    {
        let input = String(e.key)

        // Removing lettter if input = del and boggle board not empty
        if (input === 'Backspace' && remainingNb !== AREA * AREA)
        {
            removeletter()
            return
        }

        // Running boggle if input = enter
        if (input == 'Enter' && remainingNb == 0)
        {
            runboggle()
        }

        let alpha = input.match(/^[a-z]$/gi)

        // Adding letter if input = alpha and boggle board not full
        if (alpha && alpha.length == 1 && remainingNb !== 0)
        {
            addletter(input)
        }
        else (remainingNb !== 0)
        {
            return
        }
    })



    // Removing letter from boggle board
    function removeletter()
    {
        // Getting appropriate box
        let box = document.getElementsByClassName('letter-box')[16 - remainingNb - 1]

        box.classList.remove('pop')

        // Removing letter
        box.textContent = ''
        box.classList.remove('filled-box')

        // Remove letter from 'letterInput'
        letterInput = letterInput.slice(0, -1)

        // Updating count
        remainingNb += 1
    }



    // Adding letter to boggle board
    function addletter(letter)
    {
        letter = letter.toUpperCase()

        // Getting appropriate box
        let box = document.getElementsByClassName('letter-box')[16 - remainingNb]

        box.classList.add('pop')

        box.textContent = letter
        box.classList.add('filled-box')

        // Add letter to 'letterInput'
        letterInput += letter

        remainingNb -= 1
    }



    //Running the boggle board
    function runboggle()
    {
        // redirecting by GET
        let url = document.location.href + "boggle/" + encodeURIComponent(letterInput)

        document.location.href = url
    }



    let randomtext = document.getElementById("randomtext")

    randomtext.addEventListener('click', function()
    {
        document.getElementById("hidden-form").submit()

        console.log(this)
    })



});




