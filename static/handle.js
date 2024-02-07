/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-02-07 23:59:27
 */
'use strict';
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    let elems = document.querySelectorAll('.modal');
    let instances = M.Modal.init(elems, '');
    const sliderEl = document.querySelector("#slider");
    const sliderValue = document.querySelector("#slider-range-value");

    sliderEl.addEventListener("input", (event) => {
        const tempSliderValue = event.target.value;
        sliderValue.textContent = tempSliderValue;
        const progress = (tempSliderValue / sliderEl.max) * 100;
        sliderEl.style.background = `linear-gradient(to right, #d90429ff ${progress}%, #edf2f4ff ${progress}%)`;
    });
});

window.onload = function () {
    const filterv3 = document.getElementById('filterv3');
    fetch('/filter_all_name')
        .then(res => res.json())
        .then(data => {
            let html = ''
            for (let i = 0; i < data.list.length; i++) {
                if (data.checked.indexOf(data.list[i]) != -1) {
                    html += `<label class="offon"><input type="checkbox" checked="checked"/><span>${data.list[i]}</span></label>`
                } else {
                    html += `<label class="offon"><input type="checkbox"/><span>${data.list[i]}</span></label>`
                }
            }
            filterv3.innerHTML = html
        });
};

function loadInsxRego() {
    fetch('/load_insx_rego')
        .then(res => res.json())
        .then(data => {
            const save = document.getElementById('insxrego')
            save.value = data.insxd
            M.textareaAutoResize(save);
        });
};

function saveInsxRego() {
    const save = document.getElementById('insxrego').value
    let save_json = { "insxd": save }
    fetch('/save_insx_rego', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(save_json)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        });
};

function upgradeClicked() {
    fetch('/handle')
        .then(res => res.json())
        .then(data => {
            const formattedData = `${data.message}, ${data.time}.`;
            document.getElementById('upgrade_data').innerHTML = formattedData;
        });
};

function doneClicked() {
    const rangeValue = document.getElementById('slider-range-value')
    const rego = document.getElementById('rego')
    const filterv3 = document.getElementById('filterv3');
    const labels = filterv3.getElementsByTagName('label');
    const onoff = rego.getElementsByTagName('input')[0]
    const checkboxStates = { 'rego': onoff.checked, 'range': Number(rangeValue.innerText) }
    for (let i = 0; i < labels.length; i++) {
        let ckb = labels[i].getElementsByTagName('input')[0];
        let span = labels[i].getElementsByTagName('span')[0];
        if (ckb.checked) {
            checkboxStates[span.innerHTML] = ckb.checked
        }
    }
    const json = JSON.stringify(checkboxStates);
    PostJson(json);
};

function PostJson(JSONA) {
    const navigation = document.getElementById('navigation')
    /* navigation.innerHTML = `<p>json data has been sent waiting for server response.</p>` */
    fetch('/handle_post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(JSONA)
    })
        .then(res => res.json())
        .then(data => {
            const jsdata = JSON.parse(data)
            let item = ''
            navigation.innerHTML = item
            /*
            for (let it in jsdata) {
                let ix = jsdata[it]
                item = `<div class="message anmin"><span class="r-text">${ix[0]}</span><span class="b-text">${ix[1]}</span></div>`
                navigation.innerHTML += item;
            }*/
            const indexData = [];
            for (let index in jsdata) {
                indexData.push(index);
            }
            const groupedData = [];
            for (let i = 0; i < indexData.length; i += 5) {
                groupedData.push(indexData.slice(i, i + 5));
            }
            console.log('GroupSize');
            const radioInputs = document.querySelectorAll('#GroupSize input[type="radio"]');
            console.log(radioInputs);
            for (let gd in groupedData) {
                item = `<div class="listmgs anmin">
                <div class="haed"><span class="a">Group</span> <span class="r">${Number(gd)+1}</span></div>
                <div class="spa"></div>`
                for (let id in groupedData[gd]){
                    let ix = jsdata[groupedData[gd][id]]
                    item+=`<div><span class="r">${ix[0]}</span> <span class="b">${ix[1]}</span></div>`
                }
                item += `</div><!--end message -->`
                navigation.innerHTML += item
            }
        });
};


