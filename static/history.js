// DOM
document.addEventListener('DOMContentLoaded', function()
{



    // Getting each chain
    let chaindict = document.getElementsByClassName('chain')

    // Redirecting to boggle for each chain
    for (let i = 0; i < chaindict.length; i++)
    {
        // If tapped, redirect to dictionary
        chaindict[i].addEventListener('click', function()
        {
            let url = document.location.href

            url = url.replace('history', '')

            let chain = chaindict[i].innerHTML

            url = url + "boggle/" + encodeURIComponent(chain)

            document.location.href = url

            console.log(this)
        })
    }



})
