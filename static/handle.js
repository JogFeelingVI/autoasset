/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-01-26 22:08:04
 */
'use strict';
function upgradeClicked() {
    fetch('/handle')
        .then(res => res.json())
        .then(data => {
            const formattedData = `${data.message}, ${data.time}.`;
            document.getElementById('upgrade').innerHTML = formattedData;
        })
}

function updata(){
    fetch('/handle_post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            name: 'NLXY9291',
            lens: 50
        })
    })
        .then(res => res.json())
        .then(data => {
    
            const formattedData = `<span class="white-text">${data.message}</span>.`;
            document.getElementById('data').innerHTML = formattedData;
        })
}


