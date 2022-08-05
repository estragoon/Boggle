import { AREA, createboggleb } from "/static/helper.js"



// DOM
document.addEventListener('DOMContentLoaded', function()
{



    // Defining the letter #
    let remainingNb = AREA * AREA

    // Defining the input chain
    let path = document.location.href.split('/')

    let letterInput = path[path.length - 1].split('')

    // Create the boggle board
    createboggleb()

    let box = document.getElementsByClassName('letter-box')

    for (let i = 0; i < AREA * AREA; i++)
    {
        // Fill each box by the corresponding letter
        box[i].textContent = letterInput[i].toUpperCase()

        box[i].classList.add('filled-box')
    }



    // Getting each item
    let dictlist = document.getElementsByClassName('list-inline-item')

    // Colouring boggle board on hover of item
    for (let i = 0; i < dictlist.length; i++)
    {
        // For each item, get the boxbool
        let boxbool = dictlist[i].getAttribute('data-boxbool-list')

        boxbool = JSON.parse(boxbool)

        // Find length of item
        let len = dictlist[i].innerHTML.length

        // If hover, add 'path' to class list of each box in boxbool
        dictlist[i].addEventListener('mouseover', function()
        {
            for (let j = 0; j < boxbool.length; j++)
            {
                let box = document.getElementsByClassName('letter-box')[boxbool[j]]

                dictlist[i].classList.add('path' + len)

                box.classList.add('path' + len)
            }
        })

        // If leaving, remove 'path' from class list of each box in boxbool
        dictlist[i].addEventListener('mouseout', function()
        {
            for (let j = 0; j < boxbool.length; j++)
            {
                let box = document.getElementsByClassName('letter-box')[boxbool[j]]

                dictlist[i].classList.remove('path' + len)

                box.classList.remove('path' + len)
            }
        })

        // If tapped, redirect to dictionary
        dictlist[i].addEventListener('click', function()
        {
            let entry = dictlist[i].innerHTML

            document.getElementById("hidden-input").value = entry

            document.getElementById("hidden-form").submit()
        })
    }



})
